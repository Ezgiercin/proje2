from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat

    @abstractmethod
    def make_sound(self):
        pass

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Habitat: {self.habitat}"


class Mammal(Animal):
    def __init__(self, name, age, habitat, tüy_rengi):
        super().__init__(name, age, habitat)
        self.tüy_rengi = tüy_rengi

    def make_sound(self):
        return "Gürültülü bir kükreme!"

    def get_info(self):
        return super().get_info() + f", Tüy Rengi: {self.tüy_rengi}"


class Bird(Animal):
    def __init__(self, name, age, habitat, kanat_genisligi):
        super().__init__(name, age, habitat)
        self.kanat_genisligi = kanat_genisligi

    def make_sound(self):
        return "Keskin ve tiz çığlık!"

    def get_info(self):
        return super().get_info() + f", Kanat Genişliği: {self.kanat_genisligi} cm"


def main():
    tiger = Mammal("Kaplan", 5, "Orman", "Turuncu")
    eagle = Bird("Kartal", 3, "Dağ", 200)

    animals = [tiger, eagle]

    for animal in animals:
        print(animal.get_info())
        print("Ses:", animal.make_sound())
        print("-")


if __name__ == "__main__":
    main()
