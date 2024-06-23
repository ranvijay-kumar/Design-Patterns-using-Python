class Address:
    def __init__(self,city,street_adress,country) -> None:
        self.city = city
        self.street_adress = street_adress
        self.country = country
    
    def __str__(self) -> str:
        return f'{self.street_adress}, {self.city}, {self.country}'


class Person:
    def __init__(self,name, address) -> None:
        self.name = name
        self.address = address
    
    def __str__(self) -> str:
        return f'{self.name} lives at {self.address}'

john = Person("John", address= Address("123 London Road", "London","UK"))
print(john)    
