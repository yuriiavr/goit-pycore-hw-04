def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1

        average = total / count if count > 0 else 0
        return total, average
    
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except ValueError:
        print("Помилка у форматі даних у файлі.")
        return None

path_to_file = 'salaries.txt'

total, average = total_salary(path_to_file)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

