import abc


class EasyEDAComponent:
    @abc.abstractmethod
    def render(self) -> str:
        ...
