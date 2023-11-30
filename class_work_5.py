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









