def default_text(str):
    return str + "\033[0m"


#
# Change color of the text
#
def black_color(str):
    return "\033[30m" + str

def red_color(str):
    return "\033[31m" + str

def green_color(str):
    return "\033[32m" + str

def yellow_color(str):
    return "\033[33m" + str

def blue_color(str):
    return "\033[34m" + str

def purple_color(str):
    return "\033[35m" + str

def turquoise_color(str):
    return "\033[36m" + str

def white_color(str):
    return "\033[37m" + str


#
# Change color of the background text
#
def black_background(str):
    return "\033[40m" + str

def red_background(str):
    return "\033[41m" + str

def green_background(str):
    return "\033[42m" + str

def yellow_background(str):
    return "\033[43m" + str

def blue_background(str):
    return "\033[44m" + str

def purple_background(str):
    return "\033[45m" + str

def turquoise_bacground(str):
    return "\033[46m" + str

def white_background(str):
    return "\033[47m" + str


#
# Effect of the text
#
def bald_text(str):
    return "\033[1m" + str

def faded_text(str):
    return "\033[2m" + str

def italic_text(str):
    return "\033[3m" + str

def underline_text(str):
    return "\033[4m" + str

def rare_blinking_text(str):
    return "\033[5m" + str

def freq_blinking_text(str):
    return "\033[6m" + str

def swap_text_and_background(str):
    return "\033[7m" + str


#
# Test
#
def main():
    print(default_text(red_color(freq_blinking_text("Red blinking text"))))
    print("Normal text")

if __name__ == "__main__":
    main()