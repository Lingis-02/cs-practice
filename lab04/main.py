import sys
from stats import read_valid, average_by_city, warmest_city




def main():
    lines = sys.stdin.read().splitlines()

    total_parsed = 0
    errors_count = 0

    for line in lines:
        clean = line.strip('\r\n')
        parts = clean.split(';')

        if clean == "":
            continue

        if len(parts) != 3:
            errors_count = errors_count + 1
            continue

        city, temp_str, date_str = parts[0], parts[1], parts[2]

        if city.strip() == "" or date_str.strip() == "":
            errors_count = errors_count + 1
            continue

        try:
            float(temp_str)
        except ValueError:
            errors_count = errors_count + 1
            continue

        total_parsed = total_parsed + 1

    valid_records = read_valid(lines)
    leader_city = warmest_city(valid_records)

    leader_temp = 0.0
    if leader_city != "":
        all_averages = average_by_city(valid_records)
        leader_temp = all_averages[leader_city]

    print(total_parsed)
    print(errors_count)
    print(f"{leader_temp:.1f}")

main()