import random

character = {
    "name": "",
    "inventory": 'Hidden Blade',
    "money": 100,
    "health": 100,
    "experience": 0,
    "tribe": "",
    "skills": {}
}

tribes = {
    "Римлянин": {"parkour": 2, "stealth": 1, "combat": 2},
    "Египтянин": {"parkour": 1, "stealth": 3, "combat": 1},
    "Викинг": {"parkour": 1, "stealth": 1, "combat": 4},
    "Грек": {"parkour": 3, "stealth": 2, "combat": 1},
    "Турок": {"parkour": 1, "stealth": 2, "combat": 3},
    "Спартанец": {"parkour": 2, "stealth": 2, "combat": 3}
}

tribes_names = set(tribes.keys())

enemies = "Enemy Soldier", "Enemy Assassin", "Enemy Spy", "Enemy Gladiator"
enemy_stats = {
    "Enemy Soldier": {"parkour": 1, "stealth": 1, "combat": 2, "health": 20},
    "Enemy Assassin": {"parkour": 2, "stealth": 2, "combat": 1, "health": 15},
    "Enemy Spy": {"parkour": 1, "stealth": 2, "combat": 1, "health": 15},
    "Enemy Gladiator": {"parkour": 2, "stealth": 2, "combat": 3, "health": 25}
}

locations = {
    "магазин": {
        "предметы_на_продажу": ['Меч', 'Эликсир здоровья', 'Эликсир хитрости', 'Усиление борьбы', 'Щит', 'Зелье хитрости', 'Боевое усиление'],
        "стоимости": [50, 25, 40, 30, 75, 50, 60]
    },
    "тренировочная_зона": {
        "навыки_для_прокачки": ["паркур", "хитрость", "борьба"],
        "стоимость_тренировки": [10, 15, 20]
    },
    "храм": {
        "благословение": ["восстановление здоровья", "улучшение навыков"],
        "стоимость_благословения": [30, 50]
    }
}


def introduction_game():
    character["name"] = input("Введите имя вашего персонажа: ")
    print(f"\nДобро пожаловать в мир Assassin's Creed, {character['name']}!\n")


def choose_tribe():
    print("Выберите свое племя.")
    for tribe in tribes:
        skill_set = ', '.join(f"{skill}: {level}" for skill, level in tribes[tribe].items())
        print(f"{tribe} ({skill_set})\n")

    tribe = ""
    while tribe not in tribes_names:
        tribe = input("Введите название вашего племени: ")

    character["tribe"] = tribe
    character["skills"] = tribes[tribe]
    print(f"\nВы выбрали племя {tribe} . А  теперь, давайте начнем путешествие!\n")

def experience_bonus():
    if character["experience"] >= 100:
        character["experience"] -= 100
        print("\nПоздравляем! Вы получили бонус за достижение 100 очков опыта.")
        for skill in character['skills'].keys():
            character['skills'][skill] += 1
        print("Ваши умения улучшены благодаря вашему опыту.\n")

def game_loop():
    while True:
        print(f"\nCharacter skills: {character['skills']}")
        random_encounter = random.choice([False, True])
        if random_encounter:
            enemy_encounter()

        experience_bonus()

        print("What would you like to do?\n")
        actions = ["Обзор окружения", "Улучшить навыки", "Сдвиг", "Отдых", "Посетить место", "Проверить инвентарь"]
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action}\n")

        action = int(input("Выберите действие: "))
        if action == 1:
            observation()
        elif action == 2:
            skill_enhancement()
        elif action == 3:
            move_on()
        elif action == 4:
            rest()
        elif action == 5:
            location_visit()
        elif action == 6:
            check_inventory()
        else:
            print("Неизвестная опция. Попробуйте еще раз.")


def observation():
    print("Наблюдение: Вы проходите через великий город Рим, полный суеты.\n")


def skill_enhancement():
    print(f"Ваши текущие навыки: {character['skills']}")
    skills = list(character['skills'].keys())
    for i, skill in enumerate(skills, 1):
        print(f"{i}. Усилите {skill}\n")
    skill_choice = int(input("Какой навык улучшить? "))
    skill_training(skills[skill_choice - 1])


def skill_training(skill):
    if character['money'] > 10:
        character['money'] -= 10
        character['skills'][skill] += 1
        print(f"\nВы улучшили {skill} навык!\n")
    else:
        print("У вас не достаточно денег для тренировки этого навыка.\n")


def enemy_encounter():
    enemy = random.choice(enemies)
    enemy_skills = enemy_stats[enemy]
    print(f"Враг {enemy} появляется!\n")

    if character['skills']['stealth'] > enemy_skills['stealth']:
        print(f"Вы успешно пробрались мимо {enemy}.\n")

    elif character['skills']["combat"] >= enemy_skills['combat']:
        print(f"Вы вступаете в бой с {enemy}!")

        fight_loop(enemy, enemy_skills)


def fight_loop(enemy, enemy_skills):
    enemy_health = enemy_skills['health']

    while enemy_health > 0 and character['health'] > 0:

        player_attack = character['skills']['combat']
        enemy_health -= player_attack

        print(f"Вы нанесли удар {character['inventory']}, нанеся {player_attack} урона {enemy}!\n")

        if enemy_health <= 0:
            print(f"Вы победили {enemy}!")
            character["experience"] += 10
        else:
            enemy_attack = enemy_skills['combat']
            character['health'] -= enemy_attack
            print(f" {enemy} наносит ответный удар, нанося {enemy_attack} урона вам!")

            if character['health'] <= 0:
                print(f"{enemy} победил вас. Игра окончена.")
                exit()


def move_on():
    print("Вы двигаетесь дальше, исследуя город.\n")


def rest():
    if character["health"] < 75:
        character["health"] += 25
        print(
            f"Вы нашли спокойный уголок и восстановили свои силы. Ваше здоровье теперь {character['health']}\n")
    else:
        print("У вас уже максимальное здоровье, продолжайте искать приключения!\n")


def location_visit():
    print("\nКуда бы вы хотели отправиться?\n")
    for location in locations.keys():
        print(f"{location}\n")

    chosen_location = input("Войти в: ")

    if chosen_location in locations.keys():
        if chosen_location == "магазин":
            visit_market()
        elif chosen_location == "тренировочная_зона":
            skill_enhancement()
        elif chosen_location == "храм":
            visit_temple()


def check_inventory():
    print(f"\nВаш инвентарь: {character['inventory']}")
    print(f"Ваши деньги: {character['money']}\n")


def visit_market():
    print("\nПродавец предлагает вам следующие товары:\n")
    for item, price in zip(locations['магазин']['предметы_на_продажу'], locations['магазин']['стоимости']):
        print(f"{item}: {price} \n")

    chosen_item = input("Выберите товар: ")

    if chosen_item in locations['магазин']['предметы_на_продажу']:
        purchase_item(chosen_item)
    else:
        print("Продавец не может вам это предоставить.\n")


def purchase_item(item):
    item_index = locations['магазин']['предметы_на_продажу'].index(item)
    item_price = locations['магазин']['стоимости'][item_index]

    if character['money'] >= item_price:
        character['money'] -= item_price

        if item not in character['inventory']:
            character['inventory'] = item

        print(f"\nВы купили {item}!\n")
    else:
        print("\nУ вас недостаточно денег.\n")


def visit_temple():
    print("Жрец предлагает вам следующие услуги:\n")
    for service, price in zip(locations['храм']['благословение'], locations['храм']['стоимость_благословения']):
        print(f"{service}: {price}\n")

    chosen_service = input("Выберите услугу: ")

    if chosen_service in locations['храм']['благословение']:
        grant_blessing(chosen_service)
    else:
        print("Жрец не может вам это предоставить.\n")


def grant_blessing(blessing):
    blessing_index = locations['храм']['благословение'].index(blessing)
    blessing_price = locations['храм']['стоимость_благословения'][blessing_index]

    if character['money'] >= blessing_price:
        character['money'] -= blessing_price
        print("\nЖрец вручает вам благословение!\n")

        if blessing == 'восстановление здоровья':
            character['health'] = 100
            print("Здоровье восстановлено до максимума.\n")
        elif blessing == 'улучшение навыков':
            for skill in character['skills'].keys():
                character['skills'][skill] += 1
            print("Все навыки были улучшены!\n")

    else:
        print("\nУ вас недостаточно денег.\n")


def main():
    introduction_game()
    choose_tribe()
    game_loop()


if __name__ == "__main__":
    main()