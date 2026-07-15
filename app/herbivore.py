from app.animal import Animal


class Herbivore(Animal):
    def hide(self) -> None:
        """Toggles the hidden state of the herbivore."""
        self.hidden = not self.hidden
