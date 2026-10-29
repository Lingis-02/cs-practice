def parse_event(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")

    parts = line.split(" ", 2)

    if len(parts) < 3:
        raise ValueError("Недостаточно элементов в строке")

    level = parts[1]
    if level != "DEBUG" and level != "INFO" and level != "WARNING" and level != "ERROR":
        raise ValueError("Неизвестный уровень лога")

    res = {}
    res["time"] = parts[0]
    res["level"] = parts[1]
    res["message"] = parts[2]
    return res


def count_levels(lines) -> dict:
    stats = {}
    stats["DEBUG"] = 0
    stats["INFO"] = 0
    stats["WARNING"] = 0
    stats["ERROR"] = 0
    stats["BROKEN"] = 0

    for line in lines:
        if line.strip() == "":
            continue
        try:
            parsed = parse_event(line)
            level = parsed["level"]
            stats[level] = stats[level] + 1
        except ValueError:
            stats["BROKEN"] = stats["BROKEN"] + 1

    return stats


def top_errors(lines, n: int) -> list:
    error_counts = {}

    for line in lines:
        if line.strip() == "":
            continue
        try:
            parsed = parse_event(line)
            if parsed["level"] == "ERROR":
                msg = parsed["message"]
                if msg in error_counts:
                    error_counts[msg] = error_counts[msg] + 1
                else:
                    error_counts[msg] = 1
        except ValueError:
            continue

    unique_messages = list(error_counts.keys())

    for i in range(len(unique_messages)):
        for j in range(len(unique_messages) - 1):
            msg1 = unique_messages[j]
            msg2 = unique_messages[j + 1]
            count1 = error_counts[msg1]
            count2 = error_counts[msg2]

            if count1 < count2:
                unique_messages[j], unique_messages[j + 1] = unique_messages[j + 1], unique_messages[j]
            elif count1 == count2:
                if msg1 > msg2:
                    unique_messages[j], unique_messages[j + 1] = unique_messages[j + 1], unique_messages[j]

    result = []
    for i in range(min(n, len(unique_messages))):
        msg = unique_messages[i]
        count = error_counts[msg]
        pair = [msg, count]
        result.append(pair)

    return result


def format_report(counts: dict, errors: list) -> str:
    lines = []
    lines.append("Отчёт по журналу")
    lines.append("")

    levels = ["BROKEN", "DEBUG", "ERROR", "INFO", "WARNING"]
    for level in levels:
        lines.append(level + ": " + str(counts[level]))

    lines.append("")
    lines.append("Частые ошибки:")

    if len(errors) == 0:
        lines.append(" - Нет ошибок")
    else:
        for item in errors:
            msg = item[0]
            count = item[1]
            lines.append(" - " + msg + " — " + str(count))

    lines.append("")
    lines.append("Уровни — по алфавиту, в конце текста перевод строки.")

    report_text = ""
    for line in lines:
        report_text = report_text + line + "\n"

    return report_text