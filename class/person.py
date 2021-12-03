class Person:

    def __init__(self, name, age, document):
        self.name = name
        self.age = age
        self.__document = document  # document is private data

    def print_document(self):
        print(self.__document)

    def run(self):
        print("I am run")

    def __show_document(self):
        print(self.__document)

    def drink(self, beer):
        if beer == "beer":
            self.__show_document
        print("I am drinking {}".format(beer))


ronaldo = Person("Ronaldo", 32, "19925150000")
print(ronaldo.name)
print(ronaldo.age)
# print(ronaldo.document) > Can not be printed because is private information
ronaldo.print_document()
# ronaldo.__show_document() > Can not be printed because is private information
ronaldo.drink("beer")
ronaldo.drink("coca-cola")