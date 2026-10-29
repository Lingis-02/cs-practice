def parse_record(line):
    clean_line = line.rstrip('\r\n')

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
            "temp": temp,
            "date": date_str}
