# File: ft_plant_growth.py
# Description: simulation plant growth over time
# Author: Chichu

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 0.8

    def old(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{round(self.height, 1)}cm, {self.age} days old"
        )


if __name__ == "__main__":
    day = 1
    print("=== Garden Plant Growth ===")
    plant1 = Plant("rose", 25.0, 30)
    growth_total = plant1.height
    plant1.show()
    while day <= 7:
        print(f"=== Day {day} ===")
        plant1.grow()
        plant1.old()
        plant1.show()
        day += 1
    growth_total = plant1.height - growth_total
    print(f"Growth this week: {round(growth_total, 1)}cm")
