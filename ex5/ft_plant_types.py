# File: ft_plant_types.py
# Description: Make parent class
#               to have different kind of plant
# Author: Chichu

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def old(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}:"
            f" {round(self.height, 1)}cm, {self.age} days old"
            )


class Flower(Plant):
    def __init__(self, name, height, age,
                 color: str, bloom: bool) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloom = bloom

    def blooming(self) -> None:
        if self.bloom:
            self.bloom = False
        else:
            self.bloom = True
            print(f"[asking the {self.name} to bloom]")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color.capitalize()}")
        if self.bloom:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age,
                 trunk_diameter: float, shade: bool) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = shade

    def produce_shade(self) -> None:
        if self.shade is False:
            self.shade = True
            print(f"[asking the {self.name} to produce shade]")
            print(
                f"Tree {self.name.capitalize()}"
                f" now produces a shade of {round(self.height, 1)}cm"
                f" long and {round(self.trunk_diameter, 1)}cm wide."
                )
        else:
            self.shade = False
            print(f"[asking the {self.name} to not produce shade]")
            print(
                f"Tree {self.name.capitalize()}"
                " not produces shade"
                )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age,
                 harvest_season: str, nutritional_value: int,
                 growth_rate: float) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        self. growth_rate = growth_rate

    def grow(self) -> None:
        self.height += self.growth_rate
        super().old()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season.capitalize()}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    i: int
    i = 0
    print("=== Garden Plant Types ===")
    plant1 = Flower("rose", 15.0, 10, "red", False)
    print("=== Flower")
    plant1.show()
    plant1.blooming()
    plant1.show()
    print()

    plant2 = Tree("oak", 200.0, 365, 5.0, False)
    print("=== Tree")
    plant2.show()
    plant2.produce_shade()
    print()

    Plant3 = Vegetable("tomato", 5.0, 10, "april", 0, 2.1)
    print("===Vegetable")
    Plant3.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        Plant3.grow()
    Plant3.show()
