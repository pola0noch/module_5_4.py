# Домашняя работа по уроку "Атрибуты и методы объекта."
class House:
    houses_history = []
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)
    def go_to(self, new_floor):
        for i in range(1, (new_floor + 1)):
            if new_floor >= self.number_of_floors or new_floor <= 1:
                print("Такого этажа не существует.")
                break
            else:
                print(i)
#Домашняя работа по уроку "Специальные методы классов"
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}.")

# Домашняя работа по уроку "Перегрузка операторов."
    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, House):
           return self.number_of_floors == other and self.number_of_floors == other
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other

# Домашняя работа по уроку "Различие атрибутов класса и экземпляра."

    def __new__(cls, *args):
        house_name = args[0]
        cls.houses_history.append(house_name)
        return super(House, cls).__new__(cls)
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
