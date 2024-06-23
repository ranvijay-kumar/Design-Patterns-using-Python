from typing import Any
import unittest


class Singleton(type):
    _instances = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self) -> None:
        self.population = {}
        f = open('capitals.txt','r')
        lines = f.readlines()
        for i in range(0, len(lines),2):
            self.population[lines[i].strip()]= int(lines[i+1].strip())
        f.close()

class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for c in cities:
            result+= Database().population[c]
        return result
    
class SingletonTests(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1,db2)

    def test_singleton_total_population(self):
        rf = SingletonRecordFinder()
        names = ['Seoul','Mexico City']
        tp = rf.total_population(names)
        self.assertEqual(17500000+17400000,tp)
    

if __name__ == "__main__":
    unittest.main()