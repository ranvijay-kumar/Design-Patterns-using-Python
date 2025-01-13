from abc import ABC
import unittest


class Creature(ABC):
    def __init__(self, game, attack, defense):
        self.game = game
        self.attack = attack
        self.defense = defense
        pass

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, attack):
        self._attack = attack

    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, defense):
        self._defense = defense

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        self._game = game

    def handle(self):
        pass


class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, attack, defense)

    @property
    def attack(self):
        bonusDefense = 0
        bonusAttack = 0
        for creature in self.game.creatures:
            if isinstance(creature, GoblinKing):
                bonusAttack += 1
                pass
            elif isinstance(creature, Goblin):
                bonusDefense += 1
                pass
        return self._attack + bonusAttack

    @attack.setter
    def attack(self, attack):
        self._attack = attack

    @property
    def defense(self):
        bonusDefense = 0
        bonusAttack = 0
        for creature in self.game.creatures:
            if isinstance(creature, GoblinKing):
                bonusAttack += 1
                bonusDefense += 1
                pass
            elif isinstance(creature, Goblin):
                bonusDefense += 1
                pass
        return self._defense + bonusDefense - 1

    @defense.setter
    def defense(self, defense):
        self._defense = defense


class GoblinKing(Goblin):
    def __init__(self, game):
        super().__init__(game, 3, 3)

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, attack):
        self._attack = attack

    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, defense):
        self._defense = defense


class Game:
    def __init__(self):
        self.creatures = []


class FirstTestSuite(unittest.TestCase):
    def test(self):
        game = Game()
        goblin = Goblin(game)
        game.creatures.append(goblin)

        self.assertEqual(1, goblin.attack)
        self.assertEqual(1, goblin.defense)

        goblin2 = Goblin(game)
        game.creatures.append(goblin2)

        self.assertEqual(1, goblin.attack)
        self.assertEqual(2, goblin.defense)

        goblin3 = GoblinKing(game)
        game.creatures.append(goblin3)

        self.assertEqual(2, goblin.attack)
        self.assertEqual(3, goblin.defense)
