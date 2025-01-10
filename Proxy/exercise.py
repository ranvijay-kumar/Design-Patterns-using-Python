from unittest import TestCase


class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return 'drinking'

    def drive(self):
        return 'driving'

    def drink_and_drive(self):
        return 'driving while drunk'


class ResponsiblePerson:
    def __init__(self, person):
        self._person = person
        self._age = person.age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def drink(self):
        if self.age < 18:
            return 'too young'
        return self._person.drink()

    def drive(self):
        if self.age < 16:
            return 'too young'
        return self._person.drive()

    def drink_and_drive(self):
        return 'dead'


class Evaluate(TestCase):
    def test_exercise(self):
        p = Person(10)
        rp = ResponsiblePerson(p)

        self.assertEqual('too young', rp.drive())
        self.assertEqual('too young', rp.drink())
        self.assertEqual('dead', rp.drink_and_drive())

        rp.age = 20

        self.assertEqual('driving', rp.drive())
        self.assertEqual('drinking', rp.drink())
        self.assertEqual('dead', rp.drink_and_drive())
