import unittest
import module_12_2


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = module_12_2.Runner("Усэйн",10)
        self.r2 = module_12_2.Runner("Андрей",9)
        self.r3 = module_12_2.Runner("Ник", 3)


    def tearDown(self):
        # Сбрасываем расстояние участников после каждого теста
        self.r1.reset_distance()
        self.r2.reset_distance()
        self.r3.reset_distance()

    def testRunUN(self):
        t1 = module_12_2.Tournament(90, self.r1, self.r3)
        results = t1.start()
        self.all_results[1] = results
        self.assertTrue(list(results.values())[-1] == "Ник")

    def testRunAN(self):
        t1 = module_12_2.Tournament(90, self.r2, self.r3)
        results = t1.start()
        self.all_results[2] = results
        self.assertTrue(list(results.values())[-1] == "Ник")

    def testRunUAN(self):
        t1 = module_12_2.Tournament(90, self.r1, self.r3, self.r3)
        results = t1.start()
        self.all_results[3] = results
        self.assertTrue(list(results.values())[-1] == "Ник")

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)


if __name__ == "__main__":
    unittest.main()