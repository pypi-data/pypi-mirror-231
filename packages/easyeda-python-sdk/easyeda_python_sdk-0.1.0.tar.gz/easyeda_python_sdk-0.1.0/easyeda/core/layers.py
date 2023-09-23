from easyeda.core import EasyEDAComponent


class Layer(EasyEDAComponent):
    def __init__(self, id_: int, name: str, color: str, visible: bool, active: bool, config: bool):
        self.id = id_
        self.name = name
        self.color = color
        self.visible = visible
        self.active = active
        self.config = config

    def render(self):
        return f"{self.id}~{self.name}~{self.color}~{self.visible}~{self.active}~{self.config}"
