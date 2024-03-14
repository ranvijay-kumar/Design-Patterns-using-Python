class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    idList= []
    lastId=-1
    
    def create_person(self, name):
        self.lastId+=1
        self.idList.append(self.lastId)
        return Person(self.lastId,name)