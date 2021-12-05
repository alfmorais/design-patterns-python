class Myclass:

    def __init__(self, estado) -> None:
        self.estado = estado

    @staticmethod
    def method_static():
        print("I am here in method static function :)")


obj = Myclass(True)
obj.method_static()
Myclass.method_static()


class Error:

    @staticmethod
    def protocolo():
        print("Erro de Protocolo")

    @staticmethod
    def entrada():
        print("entrada errada")