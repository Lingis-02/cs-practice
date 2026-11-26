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


