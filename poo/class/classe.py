from typing import Type

class Interruptor:

    def __init__(self, comodo: str) -> None:
        self.__comodo = comodo

    def acender(self):
        print("acendendo {}".format(self.__comodo))

    def apagar(self):
        print("apagando {}".format(self.__comodo))


class Pessoa:

    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()

    def dormir(self):
        print("foi dormir...")


lhama = Pessoa()
interrupor_quarto = Interruptor("Quarto")

interrupor_quarto.acender()
interrupor_quarto.apagar()

lhama.acender_luz(interrupor_quarto)

