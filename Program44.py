#constructors
class person:
    name= "Ankush"
    occupation="software developer"
    networth= 10

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person()
a.info()