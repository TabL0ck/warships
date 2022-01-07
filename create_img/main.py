import sys
sys.path.insert(1, "/home/arch/Documents/warship_bot")

import config
from PIL import Image
from change_color.err_succ import error_case, succ_case
# Путь к составным частям поля
path_to_parts = "/home/arch/Documents/warship_bot/create_img/parts/"
path_to_save = "/home/arch/Documents/warship_bot/create_img/new.png"

# Создание нового объекта Image
pics = Image.new('RGB', (1100,550))

# Создание объектов Image для каждой части
alphabet = Image.open(path_to_parts+"alphabet.png")
numbers = Image.open(path_to_parts+"numbers.png")
blank_tile = Image.open(path_to_parts+"blank_tile.png")
ship_tile = Image.open(path_to_parts+"ship_tile.png")
miss_tile = Image.open(path_to_parts+"miss_tile.png")
hit_tile = Image.open(path_to_parts+"hit_tile.png")

#
# Создание и сохранение пикчи
#
def create_img(path_to_save):

    # Добавление основной, НЕ меняющейся части, пикчи
    pics.paste(alphabet,(0,0))
    pics.paste(numbers,(0,50))
    pics.paste(alphabet,(550,0))
    pics.paste(numbers,(550,50))

    # Добавление тайлов для игрока
    for i in range(1,11):
        for j in range(1,11):
            pics.paste(blank_tile,(50*i,50*j))

    # Добавление тайлов для соперника
    for i in range(1,11):
        for j in range(1,11):
            pics.paste(blank_tile,(550 + 50*i,50*j))

    # Сохранение пикчи
    pics.save(path_to_save)
    if config.DEBUG:
        succ_case("[SUCCESS] Image has been created")

#
# Выбор тайлов для каждой клетки у игрока
#
def choose_player_tile():
    pass

#
# Тесты
#
def main():
    create_img(path_to_save=path_to_save)

if __name__ == "__main__":
    main()