#
# Основной класс кораблей, в котором прописана логика существования корабля
#
class ship:

    # Атрибут, который показывает мертв ли кораблик
    _status = None
    #Координаты корабля
    _xy_cord = None
    # Клетки вокруг корабля
    _cells_around_ship = None

    _dead_cells = None

    # Инит, пока что только присваивает кораблю статус "живой"
    def __init__(self):
        self.status = True
        self._xy_cord = []
        self._cells_around_ship = []
        self._dead_cells = []

    # Геттер для координат
    @property
    def xy_cord(self):
        return self._xy_cord

    @xy_cord.setter
    def xy_cord(self, xy):
        # Проверка xy на тип
        if not isinstance(xy, tuple):
            raise TypeError("xy must be tuple")
        # Проверка xy на длину
        elif len(xy) != 2:
            raise ValueError("xy must have only 2 args")
        # Проверка x на тип
        elif not isinstance(xy[0], int):
            raise TypeError("x must be int")
        # Проверка y на тип
        elif not isinstance(xy[1], int):
            raise TypeError("y must be int")
        # Проверка x на принадлежность к [0-9]
        elif xy[0] < 0 or xy[0] > 9:
            raise ValueError("x must be in range [0-9]")
        # Проверка y на принадлежность к [0-9]
        elif xy[1] < 0 or xy[1] > 9:
            raise ValueError("y must be in range [0-9]")
        # Добавление координаты в массив
        else:
            self._xy_cord.append((xy[0],xy[1]))

    # Геттер массива клеток вокруг корабля
    @property
    def cells_around_ship(self):
        return self._cells_around_ship


    # Сеттер массива клеток вокруг корабля
    @cells_around_ship.setter
    def cells_around_ship(self, xy):
        # Проверка типа xy
        if not isinstance(xy, tuple):
            raise TypeError("xy must be tuple")
        # Проверка длины xy
        elif len(xy) != 2:
            raise ValueError("xy must have only 2 values")
        # Проверка типа x
        elif not isinstance(xy[0], int):
            raise TypeError("x must be int")
        # Проверка принадлежности x к [0-9]
        elif xy[0] < 0 or xy[0] > 9:
            raise ValueError("x must be in range [0-9]")
        # Проверка типа y
        elif not isinstance(xy[1], int):
            raise TypeError("y must be int")
        # Проверка принадлежности y к [0-9]
        elif xy[1] < 0 or xy[1] > 9:
            raise ValueError("y must be in range [0-9]")
        # Добавление xy в массив cells_arround_ship
        else:
            self._cells_around_ship.append(xy)

    #Геттер массива мертвых клеток
    @property
    def dead_cells(self):
        return self._dead_cells

    #Сеттер массива мертвых клеток
    @dead_cells.setter
    def dead_cells(self, xy):
        # Проверка типа xy
        if not isinstance(xy, tuple):
            raise TypeError("xy must be tuple")
        # Проверка длины xy
        elif len(xy) != 2:
            raise ValueError("xy must have only 2 values")
        # Проверка типа x
        elif not isinstance(xy[0], int):
            raise TypeError("x must be int")
        # Проверка принадлежности x к [0-9]
        elif xy[0] < 0 or xy[0] > 9:
            raise ValueError("x must be in range [0-9]")
        # Проверка типа y
        elif not isinstance(xy[1], int):
            raise TypeError("y must be int")
        # Проверка принадлежности y к [0-9]
        elif xy[1] < 0 or xy[1] > 9:
            raise ValueError("y must be in range [0-9]")
        # Добавление xy в массив cells_arround_ship
        else:
            self._dead_cells.append(xy)

    # Геттер для статуса
    @property
    def status(self):
        return self._status

    # Сеттер для статуса, лучше не ошибайся, а то словишь исключение
    @status.setter
    def status(self, value):
        # Проверка value на тип 
        if not isinstance(value, bool):
            raise TypeError("_status can be only bool")
        # Запись value в status
        else:
            self._status = value

    # Обработчик удара
    def hit(self, cord):
        # Проверка типа cord
        if not isinstance(cord, str):
            raise TypeError("hitting cord must be str")
        # Проверка длины cord
        elif len(cord) != 2:
            raise ValueError("hitting cord must have only 2 symbol")
        # Проверка первого символа на значения [a-j]
        elif ship.char_to_int(cord[0].lower()) == 666:
            raise ValueError("first symbol must be in range [a-j]")
        # Проверка второго символа cord на возможность представить в типе int
        elif not ship.convert_to_int(cord[1]):
            raise TypeError("second symbol must be converted to int")
        # Проверка попадания по кораблю возвращает True при попадании и False при промахе
        else:
            hit_x = ship.char_to_int(cord[0].lower())
            hit_y = int(cord[1])
            item = (hit_x, hit_y)
            if item in self.xy_cord:
                self.dead_cells = (hit_x, hit_y)
                for item in self.xy_cord:
                    if item not in self.dead_cells:
                        self.create_unuseable_cells(hit_x, hit_y)
                        return True
                self.status = False
                self.create_unuseable_cells(hit_x, hit_y)
                return True
            else:
                return False

        
    #
    # Ваууу, в питоне 3.10 завезли матч кейс
    # Функция, которая преобразовывает буквенную координату в числовую
    #
    @staticmethod
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
    
    #
    # Функция проверяющая возможность конвертнуть char в int
    #
    @staticmethod
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
            ship.__init__(self)
            self.xy_cord = (ship.char_to_int(cord[0].lower()), int(cord[1]))

    
    # Заполнение массива клеток вокруг корабля
    def create_unuseable_cells(self, x, y):

        if not isinstance(x, int):
            raise TypeError("x must be int")
        elif x > 9 or x < 0:
            raise ValueError("x must be in range [0-9]")
        elif not isinstance(y, int):
            raise TypeError("y must be int")
        elif y > 9 or y < 0:
            raise ValueError("y must be in range [0-9]")

        for i in range(x-1, x+2):
            if i < 0 or i > 9:
                continue
            for j in range(y-1, y+2):
                if j < 0 or j > 9 or (i == x and j == y):
                    continue
                else:
                    self.cells_around_ship = (i,j)

#
# Класс двойных кораблей
#
class ship_2x(ship):

    # Инит, присваивает координаты кораблику с переменной cord которая имеет тип str
    def __init__(self, cord):
        # Проверка cord на тип str
        if not isinstance(cord, str):
            raise TypeError("cord can be only str")
        # Проверка cord на длину
        elif len(cord) != 5:
            raise ValueError("cord lenght always must be 5")
        # Проверка первого символа на значения [a-j]
        elif ship.char_to_int(cord[0].lower()) == 666:
            raise ValueError("first symbol must be in range [a-j]")
        # Проверка второго символа cord на возможность представить в типе int
        elif not ship.convert_to_int(cord[1]):
            raise TypeError("second symbol must be converted to int")
        # Проверка третьего символа на -
        elif cord[2] != "-":
            raise ValueError("third symbol must be -")
        # Проверка четвертого символа на значения [a-j]
        elif ship.char_to_int(cord[3].lower()) == 666:
            raise ValueError("fourth symbol must be in range [a-j]")
        # Проверка пятого символа cord на возможность представить в типе int
        elif not ship.convert_to_int(cord[4]):
            raise TypeError("fifth symbol must be converted to int")

        # Проверка допустимости создания корабля в виде полоски
        if abs(ship.char_to_int(cord[0].lower()) - ship.char_to_int(cord[3].lower())) == 1:
            a = True
        else:
            a = False

        if abs(int(cord[1]) - int(cord[4])) == 1:
            b = True
        else:
            b = False

        if (a == b) :
            raise ValueError("cord must be with length or width equal 2, and sceond param equal 1")

        # Создание объекта
        else:
            ship.__init__(self)
            start_x = ship.char_to_int(cord[0].lower())
            start_y = int(cord[1])
            end_x = ship.char_to_int(cord[3].lower())
            end_y = int(cord[4])

            if start_x > end_x - 1:
                start_x, end_x = end_x, start_x
            if start_y > end_y - 1:
                start_y, end_y = end_y, start_y

            for i in range (start_x, end_x + 1):
                for j in range(start_y, end_y + 1):
                    self.xy_cord = (i, j)

    # Заполнение массива клеток вокруг корабля
    def create_unuseable_cells(self, x, y):

        if not isinstance(x, int):
            raise TypeError("x must be int")
        elif x > 9 or x < 0:
            raise ValueError("x must be in range [0-9]")
        elif not isinstance(y, int):
            raise TypeError("y must be int")
        elif y > 9 or y < 0:
            raise ValueError("y must be in range [0-9]")

        for i in range(x-1, x+2):
            if i < 0 or i > 9:
                continue
            for j in range(y-1, y+2):
                if j < 0 or j > 9 or (i,j) in self.xy_cord or (i,j) in self.cells_around_ship:
                    continue
                else:
                    self.cells_around_ship = (i,j)
            


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

    # Массивы клеток


    # Пока что пустой инит, мб так и останеться пустым...не знаю
    def __init__(self):
        pass

    #
    # Геттеры для одинарных кораблей
    #
    @property
    def first_1x_ship(self):
        return self._first_1x_ship

    @property
    def second_1x_ship(self):
        return self._second_1x_ship

    @property
    def third_1x_ship(self):
        return self._third_1x_ship

    @property
    def fourth_1x_ship(self):
        return self._fourth_1x_ship

    #
    # Сеттеры для одинарных кораблей
    #
    @first_1x_ship.setter
    def first_1x_ship(self,cord):
        self._first_1x_ship = ship_1x(cord)

    @second_1x_ship.setter
    def second_1x_ship(self,cord):
        self._second_1x_ship = ship_1x(cord)
    
    @third_1x_ship.setter
    def third_1x_ship(self, cord):
        self._third_1x_ship = ship_1x(cord)
    
    @fourth_1x_ship.setter
    def fourth_1x_ship(self, cord):
        self._fourth_1x_ship = ship_1x(cord)
        


#
# Тесты
#
def main():
    obj = ship_2x("c3-c4")
    obj.hit("c3")
    print(obj.cells_around_ship)
    obj.hit("c4")
    print(obj.cells_around_ship)

if __name__ == "__main__":
    main()