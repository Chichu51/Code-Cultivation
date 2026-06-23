# File: ft_plant_secutity.py
# Description: Creation of secure system (protection
#               and encapsulation sensitive data)
# Author: Chichu

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self.set_height(height)
        self.set_age(age)

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(
                f"{self._name.capitalize()}: "
                "Error, height can’t be negative\n"
                "Height update rejected"
            )
        else:
            self._height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(
                f"{self._name.capitalize()}: "
                "Error, age can’t be negative\n"
                "Age update rejected"
            )
        else:
            self._age = new_age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(
            f"{self._name.capitalize()}: "
            f"{round(self._height, 1)}cm, {self._age} days old"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = Plant("rose", 15.0, 10)
    print("Plant created: ", end="")
    plant1.show()
    print()

    plant1.set_height(25.0)
    print(f"Height updated: {plant1.get_height()}cm")
    plant1.set_age(30)
    print(f"Age updated: {plant1.get_age()} days")
    print()

    plant1.set_height(-25.0)
    plant1.set_age(-30)
    print()

    print("Current state: ", end="")
    plant1.show()
