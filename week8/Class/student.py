class Student:

    # Defino la clase, la defino con ella misma y las variables que la componen.
    def __init__(self, name, house, patronus):
        self.name = name
        self.house = house
        self.patronus = patronus


    # Defino como se muestra al imprimir mi clase.
    def __str__(self) -> str:
        return f"{self.name} from {self.house}"  

    # Defino una funcion propia para darle uso a la clase.
    def charm(self):
        match self.patronus:
            case "Stag":
                 return '🐎'      
            case "Otter":
                return '🦦'
            case "Dog":
                return '🐶'
            case _:
                return '🪶'

    @classmethod
    def create(cls):
        while True:
            name = input('Name: ').capitalize()
            house = input('House: ').capitalize()
            patronus = input('Patronus: ').capitalize()
            try:
                return cls(name, house, patronus)

            # Si la clase me devuelve el error que indique, lo muestra en pantalla.
            except ValueError as e:
                print(f"Error: {e}")

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
         if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
            raise ValueError("Invalid House")
         self._house = house

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

def main():
    student = Student.create()
    print(
            f"{student}\n"
            "Expecto Patronum! \n"
            f"{student.charm()}"
        )

if __name__ == "__main__":
    main()