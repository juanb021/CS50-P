class Wizzard:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} is a Wizzard"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

class Student(Wizzard):
    def __init__(self, name, house) -> None:
        super().__init__(name)
        self.house = house

    def __str__(self) -> str:
        return f"{self.name} from {self.house}"

class Professor(Wizzard):
    def __init__(self, name, subject) -> None:
        super().__init__(name)
        self.subject = subject

    def __str__(self) -> str:
        return f"{self.name} from {self.subject}"

student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "DADA")
wizzard = Wizzard("Albus Dumbledore")

print(
    "\n"
    f"{wizzard} \n"
    f"{student} \n"
    f"{professor} \n"
)