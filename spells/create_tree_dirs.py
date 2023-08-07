import os
from tree_file import films_titles
from create_award_films import awards

dir_main = "Harry_Potter"  # Задаємо назву головної директорії "Harry_Potter"

if not os.path.exists(dir_main):  # Перевіряємо, чи не існує вже директорія з такою назвою
    os.mkdir(dir_main)  # Якщо директорії не існує, створюємо її
    print("Створена директорія")  # Виводимо повідомлення про створення директорії
else:
    print("Директорія вже існує")  # Якщо директорія вже існує, виводимо повідомлення


os.chdir(dir_main)  # Змінюємо поточну робочу директорію на "Harry_Potter"


title_film = []  # Створюємо пустий список для збереження назв фільмів

    # Проходимо по списку фільмів з "films_titles['results']"
for i in films_titles['results']:
    # Замінюємо пробіли та двокрапки у назві фільму на підкреслення і зберігаємо в список "title_film"
    update_title = i['title'].replace(' ', '_').replace(':', '')
    title_film.append(update_title)
    os.makedirs(update_title, exist_ok=True)  # Створюємо директорію для фільму з такою назвою

os.chdir('..')  # Перехід на рівень вище (виходимо з "Harry_Potter")

path_sub_list = []  # Створюємо пустий список для збереження шляхів до піддиректорій

    # Проходимо по списку назв фільмів
for title in title_film:
    # Проходимо по кодах символів від 'A' до 'Z'
    for i in range(ord('A'), ord('Z')):
        path_sub_dir = dir_main + '/' + title + '/' + chr(i)  # Формуємо шлях до піддиректорії
        #print(path_sub_dir)
        os.makedirs(path_sub_dir, exist_ok=True)  # Створюємо піддиректорію (при потребі)

            # Проходимо по списку нагород (awards) і перевіряємо, чи відповідає шлях певним умовам
        for j in awards:
            if path_sub_dir[-1:] == j['award_name'][:1] and j['title_film'] == path_sub_dir[(len(dir_main)):-2].replace('/', ''):
                # Якщо шлях відповідає умові, зберігаємо його у список "path_sub_list"
                path_sub_list.append(os.path.join(path_sub_dir, j['award_name']))


        # Проходимо по списку шляхів до піддиректорій
for i in path_sub_list:
     #print(path_sub_list)
     #print(i[i.rfind('/'):].replace('/',''))
     #print(i[(len(dir_main)): i.rfind('/') -1].replace('/',''))
     with open(i + '.txt', 'w', encoding='UTF-8') as file_award:  # Відкриваємо файл для запису
            # Проходимо по списку нагород і записуємо відповідну нагороду у відповідний файл
        for j in awards:
            if j['award_name'] == i[i.rfind('/'):].replace('/','') and \
                j['title_film'] == i[(len(dir_main)): i.rfind('/') -1].replace('/',''):
                file_award.write(j['award'] + '\n')
