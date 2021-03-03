# 1st_task
from time import sleep

# Зеленый свет горит 7 секунд
my_Dict = {"Red": 7,
           "Yellow": 2,
           "Green": 7}


class TrafficLight:
    # Сначала всегда горит красный, затем мы меняем цвет
    __color = "Red"

    def running(self):
        """Тянем продолжительность сигнала из нашего словаря по ТЕКУЩЕМУ ЗНАЧЕНИЮ
        атрибута color. Внизу бесконечный цикл"""
        while True:
            TrafficLight.__color = "Red"
            print(TrafficLight.__color)
            sleep(my_Dict.get(TrafficLight.__color))
            TrafficLight.__color = "Yellow"
            print(TrafficLight.__color)
            sleep(my_Dict.get(TrafficLight.__color))
            TrafficLight.__color = "Green"
            print(TrafficLight.__color)
            sleep(my_Dict.get(TrafficLight.__color))


my_Traffic_Light = TrafficLight()
my_Traffic_Light.running()

# 4th_task

class Car:

    is_police = False

    def __init__(self, name, color):
        """Любая машина сначала не заведена, но при этом,
        полицейские машины создаются отдельно.
        is_on и speed - сначала всегда False/0, is_police - поле КЛАССА, а не экземпляра"""
        self.name = name
        self.is_on = False
        self.speed = 0
        self.color = color

    def switch_on(self):
        """Заводим машину.
        Когда машина заведена она начинает движение с низкой скоростью"""
        if self.is_on:
            print("Машина уже заведена")
        else:
            self.is_on = True
            self.speed = 1
            print("Машина заведена")
        return

    def switch_off(self):
        """Выключаем двигатель - скорость падает до нуля"""
        if self.is_on:
            self.is_on = False
            self.speed = 0
            print("Выключили двигатель")
        else:
            print("Машина и так не заведена")
        return

    def go(self):
        """Начинаем движение и указываем скорость"""
        if self.is_on:
            print("Машина начала движение")
            our_speed = int(input("С какой скоростью газанем?): "))
            self.speed = our_speed
        else:
            print("Сначала заведите машину")
        return

    def stop(self):
        """Завершаем движение"""
        if self.is_on:
            print("Машина прекратила движение")
            self.speed = 0
        else:
            print("Сначала заведите машину")
        return

    def turn(self):
        if self.is_on:
            side_of_turn = input("Куда повернуть?\n"
                                 "Требуется формат 'лево'/'право': ")

            print(f"Машина повернула на{side_of_turn}")
        else:
            print("Сначала заведите машину")
        return

    def show_speed(self):
        print(f"Сейчас ваша скорость {self.speed}")
        return


my_Car = Car("Волга", "Белый")
my_Car.switch_on()
my_Car.go()
my_Car.turn()
my_Car.show_speed()


class TownCar(Car):

    speed_limit = 60

    def show_speed(self):
        """С полями класса не понял(
        Но возможно имелось ввиду то, что я сделал"""

        super().show_speed()
        if self.speed > TownCar.speed_limit:
            print("Нарушаете!!!")
        return


class WorkCar(Car):

    speed_limit = 40

    def show_speed(self):
        super().show_speed()
        if self.speed > WorkCar.speed_limit:
            print("Нарушаете!!!")
        return


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police = True


# 2nd_task

weight_Of_Road = int(input("Введите массу асфальта: "))
thickness_Of_Road = int(input("Введите толщину асфальта: "))


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def def_weight(self):
        final_weight = weight_Of_Road * thickness_Of_Road * self._length * self._width
        print(f"Итоговая масса составляет {final_weight}")
        return


my_Road = Road(30, 40)
my_Road.def_weight()

# 3d_task


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.bonus = bonus
        self.wage = wage
        self._income = {"wage": self.wage,
                        "bonus": self.bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя сотрудника - {self.name} {self.surname}")
        return

    def get_total_income(self):
        """Можно суммировать элементы словаря. Но зачем?"""
        print(f"Итоговый доход сотрудника {self.wage + self.bonus}")
        return


first_Worker = Position("Сергей", "Бычков", "Аналитик", 10000, 20000)
first_Worker.get_full_name()
first_Worker.get_total_income()

# 5th_task


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")
        return


class Pen(Stationery):

    def draw(self):
        """Если будем делать через super - будет два сообщения, поэтому"""
        print("Сюда можно вставить любое сообщение")
        return


class Pencil(Stationery):

    def draw(self):
        print("Сюда можно вставить, правда, любое сообщение")
        return


class Handle(Stationery):

    def draw(self):
        print("Обещаю, что можно вставить и правда любое сообщение!")
        return


my_Pencil = Pencil("Я карандаш!")
my_Pen = Pen("Я ручка!")
my_Handle = Handle("Я маркер!")

my_Pencil.draw()
my_Pen.draw()
my_Handle.draw()













