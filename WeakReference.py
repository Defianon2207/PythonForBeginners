from dataclasses import dataclass

@dataclass
class Person:
    name: str
    weight: int = 70
    rollNumber: int | None = None

    def __repr__(self):
        return f"Person({self.name})"


Raju = Person("John Doe",70)
print(Raju.name, Raju.weight, Raju.__class__.__name_, Raju.rollNumber)  # Output: John Doe 70 Person

