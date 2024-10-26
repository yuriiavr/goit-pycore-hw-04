def get_cats_info(path):
    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": int(age)
                }
                cats.append(cat_info)
    
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except ValueError:
        print("Помилка у форматі даних у файлі.")
        return None

    return cats

path_to_file = 'cats.txt'

cats_info = get_cats_info(path_to_file)
print(cats_info)