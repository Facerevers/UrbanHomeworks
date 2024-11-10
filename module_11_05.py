import inspect

class Table:
    def __init__(self, color, ctl, typet):          # Задаём поля для объекта класа Table:
        self.color = color                          # Цвет
        self.ctl = ctl                              # Количество ножек
        self.typet = typet                          # Тип стола (обеденый, журнальный и т.п.)

    def print_info(self):                           # Функция для распеатывания информации об объекте
        print(f"Color of this table: {self.color}")
        print(f"Count of legs of this table: {self.ctl}")
        print(f"Type of this tablr: {self.typet}")

    def recolored(self, new_color):                 # Функция для смены цвета объекта
        self.color = new_color

    def add_leg(self, leg_cnt):                     # Функция для добавления ножек к объекту
        self.ctl += leg_cnt

    def del_leg(self, leg_cnt):                     # Функция для удаления ножек из объекта
        if self.ctl - leg_cnt < 3:                  # Ножек не может быть меньше 3-х
            print("A table cannot have less than three legs!")
        else:
            self.ctl -= leg_cnt



def introspection_info(obj):
    print(type(obj))                    # Получаем тип объекта
    print(hasattr(obj, "ctl"))          # Проверяем, есть-ли у объекта атрибут "ctl"
    print(dir(obj))                     # Выводим на печать все возможные методы и атрибуты
    print(callable(obj))                # Можно-ли вызвать объект?
    print(inspect.ismodule(obj))        # Является-ли объект модулем?
    print(inspect.isclass(obj))         # Является-ли объект классом?
    print(isinstance(obj, Table))       # Принадлежит-ли объект класу "Table"?


t1 = Table("black",4,"dining")
t1.recolored("red")
t1.add_leg(2)
t1.del_leg(4)
t1.print_info()

introspection_info(t1)