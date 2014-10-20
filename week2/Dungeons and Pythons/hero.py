from entity import Entity


class Hero(Entity):
    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.nickname = nickname
        self.max_health = health

    def known_as(self):
        return "{} the {}".format(self.name, self.nickname)


