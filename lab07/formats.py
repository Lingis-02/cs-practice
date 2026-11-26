import json


def csv_to_records(text):
    if text.strip() == "":
        return []

    raw_lines = text.strip().split("\n")
    lines = []
    for line in raw_lines:
        if line.strip() != "":
            lines.append(line.strip())

    if len(lines) < 2:
        return []

    header_line = lines.pop(0)
    headers = []
    for h in header_line.split(","):
        headers.append(h.strip())

    records = []
    for line in lines:
        values = line.split(",")
        row = {}
        for j in range(len(headers)):
            row[headers[j]] = values[j].strip()
        records.append(row)

    return records



def convert_value(text):
    val = text.strip()
    low = val.lower()

    if low == "true" or low == "yes":
        return True
    if low == "false" or low == "no":
        return False

    if val.startswith("-"):
        num_part = val[1:]
    else:
        num_part = val
    if num_part.isdigit():
        return(int(val))

    return val


def parse_settings(lines):
    settings = {}
    current_key = ""

    for line in lines:
        comment_index = line.find("#")
        if comment_index != -1:
            line = line[:comment_index]

        clean = line.strip()
        if clean == "":
            continue

        if clean.startswith("-") and current_key != "":
            item = clean[1:].strip()
            settings[current_key].append(convert_value(item))
        elif ":" in clean:
            key, _, val = clean.partition(":")
            key = key.strip()
            val = val.strip()

            if val == "":
                settings[key] = []
                current_key = key
            else:
                settings[key] = convert_value(val)
                current_key = ""

    return settings



def merge_by_key(rows, extra, key="id"):
    result = []

    for row in rows:
        new_row = {}
        for k in row:
            new_row[k] = row[k]

        row_id = row.get(key)
        if row_id in extra:
            extra_info = extra[row_id]
            for k in extra_info:
                if k not in new_row:
                    new_row[k] = extra_info[k]

        result.append(new_row)

    return result



def records_to_json(records):
    return json.dumps(records, indent=2, sort_keys=True, ensure_ascii=False)



