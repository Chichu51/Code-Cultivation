# File: ft_garden_data.py
# Description: Definition of a Plant class to store its name, height, and age.
# Author: Chichu

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.height}cm, {self.age} days old"
        )


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant1 = Plant("rose", 25, 30)
    plant2 = Plant("sunflower", 80, 45)
    plant3 = Plant("cactus", 15, 120)
    plant1.show()
    plant2.show()
    plant3.show()
