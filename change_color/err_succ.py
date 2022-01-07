import sys
sys.path.insert(1, "/home/arch/Documents/warship_bot")

from change_color.main import *
#
#Warship_DEBUG_text
#
def error_case(str):
    print(default_text(bald_text(red_color(str))))

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
