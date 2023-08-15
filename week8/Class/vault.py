class Vault:
    def __init__(self, galleons=0, sickles=0,knuts=0) -> None:
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self) -> str:
        return f"\n{self.galleons} Galleons, {self.sickles} Sickles and {self.knuts} Knuts \n"
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles,knuts)

potter = Vault(100,50, 25)
print(potter)

weasley = Vault(25, 15, 100)
print(weasley)

total = potter + weasley
print(total)