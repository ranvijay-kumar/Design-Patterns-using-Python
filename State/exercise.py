import unittest


class CombinationLock:
    def __init__(self, combination):
        self.failed = None
        self.digit_entered = None
        self.status = None
        self.combination = combination
        self.reset()

        # todo

    def reset(self):
        self.status = 'LOCKED'
        self.digit_entered = 0
        self.failed = False
        # todo - reset lock to LOCKED state

    def enter_digit(self, digit):
        if self.status == "LOCKED":
            self.status = ""
        self.status += str(digit)
        if self.combination[self.digit_entered] != digit:
            self.failed = True
        self.digit_entered += 1
        if self.digit_entered == len(self.combination):
            self.status = "ERROR" if self.failed else "OPEN"
        # todo


class FirstTestSuite(unittest.TestCase):
    def test_success(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(3)
        self.assertEqual('123', cl.status)
        cl.enter_digit(4)
        self.assertEqual('1234', cl.status)
        cl.enter_digit(5)
        self.assertEqual('OPEN', cl.status)

    def test_failure(self):
        cl = CombinationLock([1, 2, 3])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(5)
        self.assertEqual('ERROR', cl.status)
