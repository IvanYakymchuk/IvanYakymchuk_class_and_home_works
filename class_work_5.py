import random as rd



class Work_of_art:
    def __init__(self, name, year, author, genre):
        self.name = name
        self.year = year
        self.author = author
        self.genre = genre

    def entering(self):
        self.name = input()
        self.year = input()
        self.author = input()
        self.genre = input()

    def __str__(self):
        return f"художній твір, назва якого '{self.name}'. " \
               f"Датований {self.year} роком. Автор - {self.author}. Жанр - {self.genre}"

class Technique:
    def __init__(self, name_of_tech, material):
        self.name_of_tech = name_of_tech
        self.material = material

    def entering(self):
        self.name_of_tech = input()
        self.material = input()

    def __str__(self):
        return f"Назва техніки - {self.name_of_tech} " \
               f"Матеріал - {self.material}"

class Painting(Work_of_art, Technique):

    def __init__(self, name, year, author, genre, name_of_tech, material, width, heigth, price):
        super(Work_of_art).__init__(name, year, author, genre)
        super(Technique).__init__(name_of_tech, material)
        self.width = width
        self.heigth = heigth
        self.price = price

    def entering(self):
        Work_of_art.entering(self)
        Technique.entering(self)
        self.width = input()
        self.heigth = input()
        self.price = int(input())

    def __str__(self):
        return super(Work_of_art,self).__str__() + super(Technique,self).__str__() +\
            f"ширина - {self.width}, висота - {self.heigth}, ЦІНА - {self.price}"

    def see_price(self):
        return self.price

    def change_price(self):
        self.price = int(input())

class Sorted:
    def __init__(self, obj) -> None:
        self.obj = obj
        self.obj = self.__iter__()

    def __iter__(self):
        return iter(sorted(self.obj))

class SortedSet(Sorted, set):
    def __init__(self, obj):
        Sorted.__init__(self, obj)

    def __str__(self):
        return set(self.obj).__str__()

class Point:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def input(self):
        self.x = float(input('x = '))
        self.y = float(input('y = '))

class CompareMixin:
    def __eq__(self, other):
        return not (self.__lt__(other) or other.__lt__(self))

    def __gt__(self, other):
        return other.__lt__(self)

    def __ne__(self, other):
        return self.__lt__(other) or other.__lt__(self)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return not other.__lt__(self)


class Point2(Point, CompareMixin):
    pass


class XOrderPoint2(Point2):
    def __lt__(self, other):
        return self.x < other.x

class YOrderPoint2(Point2):
    def __lt__(self, other):
        return self.y < other.y

class DistOrderPoint2(Point2):
    def __lt__(self, other):
        return (self.x**2 + self.y**2)**0.5 < (other.x**2 + other.y**2)**0.5

if __name__ == "__main__":

    numbers_of_paintings = int(input())
    painting_list = []
    for _ in range(numbers_of_paintings):
        painting = Painting()
        painting.entering()
        painting_list.append(painting)



    for painting in painting_list:
        print (painting)

    number_of_people = int(input())
    lst_of_buyers = []
    for _ in range(number_of_people):
        person = input()
        lst_of_buyers.append(person)

    for painting in painting_list:

        prices = {person: rd.randint(1,1000) for item in lst_of_buyers}
        maxp = 1
        for k,v in prices:
            if maxp<v:
                ind_max = k
                maxp = v


        max_price = maxp
        if max_price < painting.see_price():
            continue

        print(f"{ind_max} придбав {painting} за {maxp}")

#до 18_8
    s = SortedSet([3,6,-8,1,9,-4,2])
    print(s)
#до 18_10

     n = int(input('n = '))
    points_list = []
    for _ in range(n):
        a = DistOrderPoint2()
        a.input()
        points_list.append(a)
    points_list = sorted(points_list)[::-1]
    for i in points_list:
        print(i)










