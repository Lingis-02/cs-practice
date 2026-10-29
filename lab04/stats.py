def parse_record(line):
    clean_line = line.strip('\r\n').strip()

    if clean_line == "":
        raise ValueError("Ошибка во введённых данных. Пустая строка.")

    parts = clean_line.split(';')

    if len(parts) != 3:
        raise ValueError("Ошибка во введённых данных. Количество полей не равно трем.")

    city = parts[0].strip()
    temp_str = parts[1].strip()
    date_str = parts[2].strip()

    if city == "" or date_str == "":
        raise ValueError("Ошибка во введённых данных. Поле город или дата пусто.")

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("Ошибка во введённых данных. Температура не является числом")

    return {"city": city,
            "temperature": temp,
            "date": date_str}




def read_valid(lines):
    valid_records = []

    for line in lines:
        if line.strip('\r\n').strip() == "":
            continue

        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            pass

    return valid_records




def average_by_city(records):
    sums = {}
    cnts = {}

    for r in records:
        city = r["city"]
        temp = r["temperature"]

        if city not in sums:
            sums[city] = temp
            cnts[city] = 1
        else:
            sums[city] = sums[city] + temp
            cnts[city] = cnts[city] + 1

    averages = {}
    for city in sums:
        averages[city] = (sums[city]) / (cnts[city])

    return averages




def warmest_city(records):
    if not records:
        return ""

    avg_temps = average_by_city(records)

    sorted_cities = sorted(avg_temps.keys(), key = lambda city: (-avg_temps[city], city))
    
    return sorted_cities[0]
