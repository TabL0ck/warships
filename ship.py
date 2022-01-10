#
# Основной класс игрока с хранением координат кораблей и их статусов
#
class player:

    # Атрибуты, хранящие в себе все данные о кораблях
    _first_1x_ship = None
    _second_1x_ship = None
    _third_1x_ship = None
    _fourth_1x_ship = None
    _first_2x_ship = None
    _second_2x_ship = None
    _third_2x_ship = None
    _first_3x_ship = None
    _second_3x_ship = None
    _single_4x_ship = None

    # Пока что пустой инит, мб так и останеться пустым...не знаю
    def __init__(self):
        pass

    #
    # Сеттеры для одинарных кораблей
    #
    def set_first_1x_ship(self,cord):
        self._first_1x_ship = ship_1x(cord)

    def set_second_1x_ship(self,cord):
        self._second_1x_ship = ship_1x(cord)
    
    def set_third_1x_ship(self, cord):
        self._third_1x_ship = ship_1x(cord)
    
    def set_fourth_1x_ship(self, cord):
        self._fourth_1x_ship = ship_1x(cord)
        
    #
    # Геттеры для одинарных кораблей
    #
    def get_first_1x_ship(self):
        return self._first_1x_ship

    def get_second_1x_ship(self):
        return self._second_1x_ship

    def get_third_1x_ship(self):
        return self._third_1x_ship

    def get_fourth_1x_ship(self):
        return self._fourth_1x_ship

#
# Основной класс кораблей, в котором прописана логика существования корабля
#
class ship:

    # Атрибут, который показывает мертв ли кораблик
    _status = None

    # Инит, пока что только присваивает кораблю статус "живой"
    def __init__(self):
        self.set_status(True)

    # Сеттер для статуса, лучше не ошибайся, а то словишь исключение
    def set_status(self, value):
        if not isinstance(value, bool):
            raise TypeError("_status can be only bool")
        else:
            self._status = value
    
    # Геттер для статуса
    def get_status(self):
        return self._status

    #
    # Ваууу, в питоне 3.10 завезли матч кейс
    # Функция, которая преобразовывает буквенную координату в числовую
    #
    def char_to_int(char):
        match char:
            case "a":
                return 0
            case "b":
                return 1
            case "c":
                return 2
            case "d":
                return 3
            case "e":
                return 4
            case "f":
                return 5
            case "g":
                return 6
            case "h":
                return 7
            case "i":
                return 8
            case "j":
                return 9
            case _:
                return 666
    
    def convert_to_int(symbol):
        try:
            int(symbol)
            return True
        except ValueError:
            return False

#
# Класс одинарных кораблей
#
class ship_1x(ship):

    # Атрибуты координат x и y, всего две так как это одинарный корабль
    # Важно: только int
    _x_cord = None
    _y_cord = None

    # Инит, присваивает координаты кораблику с переменной cord которая имеет тип str
    def __init__(self, cord):

        # Проверка cord на тип str
        if not isinstance(cord, str):
            raise TypeError("cord can be only str")
        # Проверка cord на длину
        elif len(cord) != 2:
            raise ValueError("cord lenght always must be 2")
        # Проверка первого символа на значения [a-j]
        elif ship.char_to_int(cord[0].lower()) == 666:
            raise ValueError("first symbol must be in range [a-j]")
        # Проверка второго символа cord на возможность представить в типе int
        elif not ship.convert_to_int(cord[1]):
            raise TypeError("second symbol must be converted to int")
        # Создание объекта
        else:
            self.set_x_cord(ship.char_to_int(cord[0].lower()))
            self.set_y_cord(int(cord[1]))
            ship.__init__(self)

    # Геттеры для координат, только int и не больше 9
    def set_x_cord(self, value):
        if not isinstance(value, int):
            raise TypeError("_x_cord can be only int")
        elif value > 9 or value < 0:
            raise ValueError("_x_cord can only be in range [0-9]")
        else:
            self._x_cord = value
            
    def set_y_cord(self, value):
        if not isinstance(value, int):
            raise TypeError("_y_cord can be only int")
        elif value > 9 or value < 0:
            raise ValueError("_y_cord can only be in range [0-9]")
        else:
            self._y_cord = value
    
    # Геттеры для координат
    def get_x_cord(self):
        return self._x_cord
    
    def get_y_cord(self):
        return self._y_cord

    # Метод чисто так подебажить, больше он не нужен
    def show_cord(self):
        print(f"x = {self._x_cord}  y = {self._y_cord}")

#
# Тесты
#
def main():
    oj = player()
    oj.set_first_1x_ship("b2")

if __name__ == "__main__":
    main()