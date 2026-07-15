from app.animal import Animal


class Carnivore(Animal):

    def bite(self, target: Animal) -> None:
        if isinstance(target, Carnivore) or target.hidden:
            return

        target.was_bitten()

        if target.health <= 0:
            target.handle_death()
