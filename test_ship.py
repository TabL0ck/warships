import unittest
from ship import player, ship, ship_1x

class test_player(unittest.TestCase):
    
    #
    # Создание обхекта для тестирования
    #
    def setUp(self):

        self.test_player = player()

    #
    # Проверка на правильность вывода кораблей 1x
    #
    def test_create_ship_1x(self):

        # Проверка правильности вывода первого 1x корабля
        self.test_player.set_first_1x_ship("a0")
        self.assertEqual(self.test_player.get_first_1x_ship(), self.test_player._first_1x_ship)

        # Проверка правильности вывода второго 1x корабля
        self.test_player.set_second_1x_ship("b1")
        self.assertEqual(self.test_player.get_second_1x_ship(), self.test_player._second_1x_ship)

        # Проверка правильности вывода третьего 1x корабля
        self.test_player.set_third_1x_ship("c2")
        self.assertEqual(self.test_player.get_third_1x_ship(), self.test_player._third_1x_ship)

        # Проверка правильности вывода четвертого 1x корабля
        self.test_player.set_fourth_1x_ship("d3")
        self.assertEqual(self.test_player.get_fourth_1x_ship(), self.test_player._fourth_1x_ship)

class test_ship(unittest.TestCase):

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
    # Проверка взаимодействия с координатами
    #
    def test_cord(self):

        # Проверка get_x
        self.assertEqual(ship_1x("b2").get_x_cord(), 1)
        # Проверка get_y
        self.assertEqual(ship_1x("b2").get_y_cord(), 2)
        # Проверка на вызов исключения объекта с неверным типом аргумента cord
        self.assertRaises(TypeError, ship_1x, 1)
        # Проверка на вызов исключения объекта с неверной длиной аргумента cord
        self.assertRaises(ValueError, ship_1x, "c/vrs/xd")
        # Проверка на вызов исключния объекта с неверным первым символом строки cord
        self.assertRaises(ValueError, ship_1x, "17")
        # Проверка на вызов исключения объекта с неверным типом второго символа строки cord
        self.assertRaises(TypeError, ship_1x, "aa")

        # Проверка set_x
        self.assertRaises(TypeError, ship_1x("b2").set_x_cord, "c/vrs/xd") # Проверка на верный тип аргумента
        self.assertRaises(ValueError, ship_1x("b2").set_x_cord, -1) # Проверка на ввод аргумента <0
        self.assertRaises(ValueError, ship_1x("b2").set_x_cord, 10) # Проверка на ввод аргумента >9

        # Проверка set_y
        self.assertRaises(TypeError, ship_1x("b2").set_y_cord, "c/vrs/xd") # Проверка на верный тип аргумента
        self.assertRaises(ValueError, ship_1x("b2").set_y_cord, -1) # Проверка на ввод аргумента <0
        self.assertRaises(ValueError, ship_1x("b2").set_y_cord, 10) # Проверка на ввод аргумента >9
    
    #
    # Проверка взаимодействия с статусом
    #
    def test_status(self):

        # Проверка get_status
        self.assertEqual(ship_1x("b2").get_status(), True)
        # Проверка set_status
        self.assertRaises(TypeError, ship_1x("b2").set_status, "c/vrs/xd") # Проверка на тип аргумента


if __name__ == "__main__":
    unittest.main()
