"""
S — Single Responsiblity Principle (Princípio da responsabilidade única)
O — Open-Closed Principle (Princípio Aberto-Fechado)
L — Liskov Substitution Principle (Princípio da substituição de Liskov)
I — Interface Segregation Principle (Princípio da Segregação da Interface)
D — Dependency Inversion Principle (Princípio da inversão da dependência)
"""

class Circo:

    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()


class Malabarista:

    def apresentar_show(self):
        print("Malabarista apresentando seu show")


class Palhaco:

    def apresentar_show(self):
        print("Palhaço apresentando seu show")


circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()

circo.apresentar(malabarista)
circo.apresentar(palhaco)
