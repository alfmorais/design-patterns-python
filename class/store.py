class Store:

    tax = 1.03

    def __init__(self, address: str) -> None:
        self.__address = address

    def show_address(self) -> None:
        print(self.__address)

    @classmethod
    def sales(cls) -> int:
        return 40 * cls.tax

    @classmethod
    def change_tax(cls, new_tax: int) -> None:
        cls.tax = new_tax


loja_praia = Store("Praia")
loja_downtown = Store("downtown")

loja_praia.show_address()
loja_downtown.show_address()

print(loja_praia.sales())
print(loja_downtown.sales())

loja_downtown.change_tax(1.50)
print(loja_praia.sales())