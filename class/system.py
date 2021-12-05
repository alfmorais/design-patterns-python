class System:

    def catalog(self, name: str, age: int) -> None:
        if self.__check_data(name, age):
            self.__save_user(name, age)
        else:
            self.__show_err()

    def __check_data(self, name: str, age: int) -> bool:
        if isinstance(name, str) and isinstance(age, int):
            return True
        else:
            return False

    def __save_user(self, name: str, age: int) -> None:
        print("acessando o banco de dados...")
        print("Cadastrar o usuário {}, idade {}.".format(name, age))

    def __show_err(self) -> None:
        print("dados inválidos")