import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walk_ = Runner('Egor')
        for i in range(10):
            walk_.walk()
        self.assertEqual(walk_.distance, 50)

    def test_run(self):
        run_ = Runner('Sergey')
        for j in range(10):
            run_.run()
        self.assertEqual(run_.distance, 100)

    def test_chalange(self):
        walk_ = Runner('Egor')
        run_ = Runner('Sergey')
        for i in range(10):
            walk_.walk()
        for j in range(10):
            run_.run()
        self.assertNotEqual(walk_.distance, run_.distance, 'test is failed')
