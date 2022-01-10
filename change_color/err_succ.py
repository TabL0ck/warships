import sys
sys.path.insert(1, "/home/arch/Documents/warship_bot")

from change_color.main import *

#
# Вывод сообщения об ошибке красным жирным шрифтом
#
def error_case(str):
    print(default_text(bald_text(red_color(str))))

#
# Вывод сообщения об успехе зеленым жирным шрифтом
#
def succ_case(str):
    print(default_text(bald_text(green_color(str))))

#
# Тесты
#
def main():
    error_case("[ERROR]")
    succ_case("[SUCCESS]")

if __name__ == "__main__":
    main()
