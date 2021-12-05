class Alarm:

    def __init__(self, state: bool) -> None:
        self.__state = state

    def get_state(self) -> bool:
        return self.__state

    def set_state(self, value: bool) -> None:
        if isinstance(value, bool):
            self.__state = value

