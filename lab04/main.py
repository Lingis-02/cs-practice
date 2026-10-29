import sys
from stats import read_valid, average_by_city, warmest_city

def main():
    raw_lines = sys.stdin.read().splitlines()

    meaningful_lines = sum(1 for line in raw_lines if line.strip('\r\n').strip() != "")

    valid_records = read_valid(raw_lines)

    total_parsed = len(valid_records)
    errors_count = meaningful_lines - total_parsed

    print(total_parsed)
    print(errors_count)

    if valid_records:
        leader_city = warmest_city(valid_records)
        all_averages = average_by_city(valid_records)
        leader_temp = all_averages[leader_city]
        print(f"{leader_temp:.1f}")
    else:
        print("0.0")


main()