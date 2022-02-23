"""Текстовая игра «герой и чудовища»."""

import random
import sys

"""счетчик поверженных героем чудовищ"""
monster_counter = 0
"""текущее состояние здоровье героя"""
hp = 11
"""текущая сила удара героя """
attack = 12


def random_monster() -> tuple[int, int]:
    """У чудовища есть случайное число здоровья и атаки."""
    life_points = random.randint(1, 10)
    impact_force = random.randint(1, 18)
    return life_points, impact_force


def actions_with_monster(monster_hp: int, monster_attack: int) -> None:
    """Встреча с монстром."""
    global hp
    global monster_counter

    while True:
        try:
            a = int(input("Выберите действие: 1-атаковать чудовище, 2-убежать "))
            if a == 1:
                print("В БОЙ!!! \n")
                while hp > 0 and monster_hp > 0:
                    hp = hp - monster_attack
                    monster_hp = monster_hp - attack
                if hp > 0:
                    print(f"У Вас осталось {hp} здоровья ")
                    monster_counter = monster_counter + 1
                    print("Вы победили монстра! \n")
                else:
                    print("Вы пали в честной битве! ПОРАЖЕНИЕ")
                    sys.exit()
            elif a == 2:
                print("Бежим отсюда!!! \n")
                break
            else:
                continue
        except TypeError:
            print("Вы ввели не целое число, ошибка")
            continue
        break


def actions_with_sword(impact_force: int) -> None:
    """Действия с мечом."""
    global attack

    while True:
        try:
            a = int(
                input(
                    "Выберите действие: 1-взять новый меч и выбросить старый, 2- пройти мимо меча"
                )
            )
            if a == 1:
                attack = impact_force
                print(
                    f"Вы решили взять новый мечь. Теперь сила Вашей атаки {impact_force} \n"
                )
            elif a == 2:
                print(f"Вы не взяли новый мечь. Сила Вашей атаки осталась {attack} \n")
                break
            else:
                print("Введите 1 или 2: ")
                continue
        except TypeError:
            print("Вы ввели не целое число, ошибка")
            continue
        break


def game() -> None:
    """Функция, которая запускает игру."""
    global monster_counter
    global hp
    global attack

    while monster_counter < 10 or hp > 0:
        print("Новый ход")
        """ Перед рыцарем случайно возникает либо очередное чудовище,
         либо увеличивающее случайное число здоровья яблочко,
         либо совершенно новый меч со случайной силой атаки"""
        print(
            f"У Вас {hp} здоровья и {attack} сила удара. \n Вы убили {monster_counter} монстра \n"
        )
        event = random.randint(1, 3)
        if event == 1:
            monster_hp, monster_attack = random_monster()
            print(
                f"Вы встретили чудовище c {monster_hp} здоровья и силой удара {monster_attack}. Выступить в БОЙ?"
            )
            actions_with_monster(monster_hp, monster_attack)
        elif event == 2:
            life_points = random.randint(1, 7)
            hp = hp + life_points
            print(
                f"Вы съели ЯБЛОКО с {life_points} здоровья. Теперь у вас {hp} жизней \n"
            )
        elif event == 3:
            sword_attack = random.randint(5, 15)
            print(f"Вы нашли МЕЧ c силой удара {sword_attack} \n")
            actions_with_sword(sword_attack)
        if hp <= 0 or monster_counter == 10:
            break
    if monster_counter == 10 and hp > 0:
        print("ПОБЕДА")
        sys.exit()
    elif hp <= 0 and monster_counter <= 10:
        print("ПОРАЖЕНИЕ")
        sys.exit()


game()
