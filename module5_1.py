class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > int(self.number_of_floors) or new_floor < 1:
            print('Такого этажа не существует')
        else:
            i = 1
            for i in range(1, new_floor+1):
                print(int(i))
                i += 1


# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h1.go_to(5)
# h2.go_to(10)

h3 = House('Фазенда в Джунглях', 4)
h3.go_to(4)
h3.go_to(7)
h3.go_to(0)
