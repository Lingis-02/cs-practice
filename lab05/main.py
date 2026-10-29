import os
from logstats import count_levels, top_errors, format_report


def main():
    file_name = input().strip()

    if not os.path.exists(file_name):
        return

    log_file = open(file_name, mode="r", encoding="utf-8")
    counts = count_levels(log_file)
    log_file.close()

    log_file = open(file_name, mode="r", encoding="utf-8")
    errors = top_errors(log_file, 3)
    log_file.close()

    total_parsed = counts["DEBUG"] + counts["INFO"] + counts["WARNING"] + counts["ERROR"] + counts["BROKEN"]
    print(total_parsed)
    print(counts["ERROR"])
    print(counts["BROKEN"])

    report_text = format_report(counts, errors)

    report_file = open("report.txt", mode="w", encoding="utf-8")
    report_file.write(report_text)
    report_file.close()


main()