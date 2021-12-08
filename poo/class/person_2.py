class Person:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def driver(self, veiculo: str) -> None:
        print(f"Dirigindo um(a) {veiculo}")

    def single(self) -> None:
        print("I need your love...")

    def say_my_age(self) -> int:
        return self.age


person = Person("Alfredo", 29)
person.driver("Honda Civic")
person.single()
person.say_my_age()
