import unittest
from ship import player, ship, ship_1x, ship_2x
from change_color.main import green_color, bald_text, default_text

class test_ship(unittest.TestCase):

    #
    # Проверка status
    #
    def test_status(self):
        # Проверка на тип
        with self.assertRaises(TypeError):
            ship().status = "c/vrs/xd"
        # Проверка на правильность отображения
        self.assertEqual(ship().status, True)

    #
    # Проверка xy_cord
    #
    def test_xy_cord(self):
        # Проверка xy на тип
        with self.assertRaises(TypeError):
            ship().xy_cord = [1,2]
            ship().xy_cord = 1
        # Проверка xy на длину
        with self.assertRaises(ValueError):
            ship().xy_cord = (1,2,3)

        # Проверка x на тип
        with self.assertRaises(TypeError):
            ship().xy_cord = ("c/vrs/xd", 2)
        # Проверка x на принадлежность к [0-9]
        with self.assertRaises(ValueError):
            ship().xy_cord = (-1,2)

        # Проверка y на тип
        with self.assertRaises(TypeError):
            ship().xy_cord = (1 , "c/vrs/xd")
        # Проверка y на принадлежность к [0-9]
        with self.assertRaises(ValueError):
            ship().xy_cord = (1,10)

    #
    # Проверка клеток вокруг корабля
    #
    def test_cells_around_ship(self):

        # Проверка xy на тип
        with self.assertRaises(TypeError):
            ship().cells_around_ship = [1,2]
            ship().cells_around_ship = 1

        # Проверка xy на количество значений
        with self.assertRaises(ValueError):
            ship().cells_around_ship = (1,2,3)

        # Проверка x на тип
        with self.assertRaises(TypeError):
            ship().cells_around_ship = ("c/vrs/xd", 2)
        # Проверка y на тип
        with self.assertRaises(TypeError):
            ship().cells_around_ship = (1, "c/vrs/xd")

        # Проверка x на принадлежность к [0-9]
        with self.assertRaises(ValueError):
            ship().cells_around_ship = (10, 1)
        # Проверка y на принадлежность к [0-9]
        with self.assertRaises(ValueError):
            ship().cells_around_ship = (1, -1)

    #
    # Проверка мертвых клеток
    #
    def test_cells_around_ship(self):

        # Проверка xy на тип
        with self.assertRaises(TypeError):
            ship().dead_cells = [1,2]
            ship().dead_cells = 1

        # Проверка xy на количество значений
        with self.assertRaises(ValueError):
            ship().dead_cells = (1,2,3)

        # Проверка x на тип
        with self.assertRaises(TypeError):
            ship().dead_cells = ("c/vrs/xd", 2)
        # Проверка y на тип
        with self.assertRaises(TypeError):
            ship().dead_cells = (1, "c/vrs/xd")

        # Проверка x на принадлежность к [0-9]
        with self.assertRaises(ValueError):
            ship().dead_cells = (10, 1)
        # Проверка y на принадлежность к [0-9]
        with self.assertRaises(ValueError):
            ship().dead_cells = (1, -1)

    #
    # Проверка функции преобразования буквенной координаты в символьную
    #
    def test_char_to_int(self):

        # Проверка на ввод допустимых значений
        self.assertEqual(ship.char_to_int("b"), 1)
        # Проверка на ввод недопустимых значений
        self.assertEqual(ship.char_to_int("c/vrs/xd"), 666)

    #
    # Проверка функции, которая проверяет возможность конвертировать str в int
    #
    def test_convert_to_int(self):

        # Проверка при вводе строки, которую можно представить в виде int
        self.assertEqual(ship.convert_to_int("322"), True)
        # Проверка при вводе строки, которую нельзя представить в виде int
        self.assertEqual(ship.convert_to_int("c/vrs/xd"), False)


class test_ship_1x(unittest.TestCase):

    #
    # Проверка создания обхекта
    #
    def test_create(self):

        # Проверка на ошибочный тип cord
        with self.assertRaises(TypeError):
            ship_1x(1)
        # Проверка на длину cord
        with self.assertRaises(ValueError):
            ship_1x("c/vrs/xd")
        # Проверка x на принадлежность к [a-j]
        with self.assertRaises(ValueError):
            ship_1x("t1")
        # Проверка y на возможность конвертации в int
        with self.assertRaises(TypeError):
            ship_1x("at")

    #
    # Проверка взаимодействия с статусом
    #
    def test_status(self):

        # Проверка get_status
        self.assertEqual(ship_1x("b2").status, True)
        # Проверка set_status
        with self.assertRaises(TypeError):
            ship_1x("b2").status = "c/vrs/xd"



    #
    # Проверка создания массива клеток вокруг корабля
    #
    def test_create_unuseable_cells(self):

        # Проверка x на тип
        self.assertRaises(TypeError, ship_1x("b2").create_unuseable_cells, "c/vrs/xd", 2)
        # Проверка y на тип
        self.assertRaises(TypeError, ship_1x("b2").create_unuseable_cells, 1, "c/vrs/xd")

        # Проверка функции на правильность вывода
        obj = ship_1x("a0")
        obj.hit("a0")
        self.assertEqual(obj.cells_around_ship, [(0,1),(1,0),(1,1)])

        obj = ship_1x("j9")
        obj.hit("j9")
        self.assertEqual(obj.cells_around_ship, [(8,8),(8,9),(9,8)])

        obj = ship_1x("c3")
        obj.hit("c3")
        self.assertEqual(obj.cells_around_ship, [(1,2),(1,3),(1,4),(2,2),(2,4),(3,2),(3,3),(3,4)])

        obj = ship_1x("c3")
        obj.hit("b2")
        self.assertEqual(obj.cells_around_ship, [])

    #
    # Проверка удара по кораблю
    #
    def test_hit(self):

        # Проверка на верный тип аргумента
        self.assertRaises(TypeError, ship_1x("b2").hit, 1)
        # Проверка на длину аргумента
        self.assertRaises(ValueError, ship_1x("b2").hit, "c/vrs/xd")
        # Проверка первого символа на принадлежность к [a-j]
        self.assertRaises(ValueError, ship_1x("b2").hit, "l1")
        # Проверка второго символа на возможность преобразовать в int
        self.assertRaises(TypeError, ship_1x("b2").hit, "ak")

        # Проверка возвращаемого значения после попадания
        self.assertEqual(ship_1x("b2").hit("b2"), True)
        # Проверка возвращаемого значения после промаха
        self.assertEqual(ship_1x("b2").hit("b3"), False)

        # Проверка статуса корабля после попадания
        obj = ship_1x("b2")
        obj.hit("b2")
        self.assertEqual(obj.status, False)
        # Проверка статуса корабля после промаха
        obj = ship_1x("b2")
        obj.hit("b3")
        self.assertEqual(obj.status, True)


class test_ship_2x(unittest.TestCase):

    #
    # Проверка создания обхекта
    #
    def test_create(self):

        # Проверка на ошибочный тип cord
        with self.assertRaises(TypeError):
            ship_2x(1)
        # Проверка на длину cord
        with self.assertRaises(ValueError):
            ship_2x("c/vrs/xd")
        # Проверка x_start на принадлежность к [a-j]
        with self.assertRaises(ValueError):
            ship_2x("t1-a1")
        # Проверка y_start на возможность конвертации в int
        with self.assertRaises(TypeError):
            ship_2x("at-a1")
        # Проверка 3 символа cord на -
        with self.assertRaises(ValueError):
            ship_2x("a0@a1")
        # Проверка x_end на принадлежность к [a-j]
        with self.assertRaises(ValueError):
            ship_2x("a1-t1")
        # Проверка y_end на возможность конвертации в int
        with self.assertRaises(TypeError):
            ship_2x("a1-at")
        # Проверка на невозможность создания корабля 1x1
        with self.assertRaises(ValueError):
            ship_2x("a0-a0")
        # Проверка на невозможность создания корабля Nx1 где N больше 2х
        with self.assertRaises(ValueError):
            ship_2x("c0-a0")
            ship_2x("a0-c0")
        # Проверка на невозможность создания корабля 1xM где M больше 2х
        with self.assertRaises(ValueError):
            ship_2x("a2-a0")
            ship_2x("a0-a2")

    #
    # Проверка удара по кораблю
    #
    def test_hit(self):

        # Проверка на верный тип аргумента
        self.assertRaises(TypeError, ship_2x("b2-b1").hit, 1)
        # Проверка на длину аргумента
        self.assertRaises(ValueError, ship_2x("b2-b1").hit, "c/vrs/xd")
        # Проверка первого символа на принадлежность к [a-j]
        self.assertRaises(ValueError, ship_2x("b2-b1").hit, "l1")
        # Проверка второго символа на возможность преобразовать в int
        self.assertRaises(TypeError, ship_2x("b2-b1").hit, "ak")

        # Проверка возвращаемого значения после попадания
        self.assertEqual(ship_2x("b2-b1").hit("b2"), True)
        # Проверка возвращаемого значения после промаха
        self.assertEqual(ship_2x("b2-b1").hit("b3"), False)

        # Проверка статуса корабля после попадания
        obj = ship_2x("b2-b1")
        obj.hit("b2")
        self.assertEqual(obj.status, True)
        obj.hit("b1")
        self.assertEqual(obj.status, False)
        # Проверка статуса корабля после промаха
        obj = ship_2x("b2-b1")
        obj.hit("b3")
        self.assertEqual(obj.status, True)

    #
    # Проверка создания массива клеток вокруг корабля
    #
    def test_create_unuseable_cells(self):

        # Проверка x на тип
        self.assertRaises(TypeError, ship_2x("b2-a2").create_unuseable_cells, "c/vrs/xd", 2)
        # Проверка y на тип
        self.assertRaises(TypeError, ship_2x("b2-a2").create_unuseable_cells, 1, "c/vrs/xd")

        # Проверка функции на правильность вывода
        obj = ship_2x("a0-b0")
        obj.hit("a0")
        self.assertEqual(obj.cells_around_ship, [(0,1),(1,1)])
        obj.hit("b0")
        self.assertEqual(obj.cells_around_ship, [(0,1),(1,1),(2,0),(2,1)])

        obj = ship_2x("j9-i9")
        obj.hit("j9")
        self.assertEqual(obj.cells_around_ship, [(8,8),(9,8)])
        obj.hit("i9")
        self.assertEqual(obj.cells_around_ship, [(8,8),(9,8),(7,8),(7,9)])

        obj = ship_2x("c3-c4")
        obj.hit("c3")
        self.assertEqual(obj.cells_around_ship, [(1,2),(1,3),(1,4),(2,2),(3,2),(3,3),(3,4)])
        obj.hit("c4")
        self.assertEqual(obj.cells_around_ship, [(1,2),(1,3),(1,4),(2,2),(3,2),(3,3),(3,4),(1,5),(2,5),(3,5)])

        obj = ship_2x("c3-c4")
        obj.hit("b2")
        self.assertEqual(obj.cells_around_ship, [])



if __name__ == "__main__":
    unittest.main()
