class Animal:
    def __init__(self,name="animal") -> None:
        self.name = name
    
    def __str__(self) -> str:
        return self.name


if __name__=="__main__":
    a = Animal()
    print(a)
