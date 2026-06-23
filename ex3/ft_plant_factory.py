# File: ft_plant_factory.py
# Description: creation and print 5 plants
# Author: Chichu

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(
            f"{(self.name.capitalize())}: "
            f"{self.height}cm, {self.age} days old"
        )


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant1 = Plant("rose", 25.0, 30)
    plant2 = Plant("oak", 200.0, 365)
    plant3 = Plant("cactus", 5.0, 90)
    plant4 = Plant("sunflower", 80.0, 45)
    plant5 = Plant("fern", 15.0, 120)
    print("Created: ", end="")
    plant1.show()
    print("Created: ", end="")
    plant2.show()
    print("Created: ", end="")
    plant3.show()
    print("Created: ", end="")
    plant4.show()
    print("Created: ", end="")
    plant5.show()
