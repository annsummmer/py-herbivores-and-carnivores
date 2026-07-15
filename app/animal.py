class Animal:
    alive: list[Animal] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def was_bitten(self) -> None:
        self.health -= 50

    def handle_death(self) -> None:
        """Removes instance from the list."""
        Animal.alive = [
            animal
            for animal in Animal.alive
            if self.name != animal.name
        ]

    def __repr__(self) -> str:
        """User-friendly representation for print()."""
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")
