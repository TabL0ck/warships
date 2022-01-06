from change_color.main import *
#
#Warship_DEBUG_text
#
def error_case(str):
    return default_text(bald_text(red_color(str)))

def succ_case(str):
    return default_text(bald_text(green_color(str)))

#
# Test
#
def main():
    print(error_case("[ERROR]"))
    print(succ_case("[SUCCESS]"))

if __name__ == "__main__":
    main()
