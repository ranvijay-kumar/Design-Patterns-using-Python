# class Creature:
#     def __init__(self, strength=10, agility=10, intelligence=10):
#         self.strength = strength
#         self.agility = agility
#         self.intelligence = intelligence
#
#     @property
#     def sum_of_stats(self):
#         return self.strength + self.intelligence + self.agility
#
#     @property
#     def max_stat(self):
#         return max(self.strength, self.intelligence, self.agility)
#
#     @property
#     def average_stat(self):
#         return self.sum_of_stats / 3.0

class Creature:
    def __init__(self, strength=10, agility=10, intelligence=10):
        self.stats = [strength, agility, intelligence]

    @property
    def sum_of_stats(self):
        return sum(self.stats)

    @property
    def max_stat(self):
        return max(self.stats)

    @property
    def average_stat(self):
        return self.sum_of_stats/len(self.stats)