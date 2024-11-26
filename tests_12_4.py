import unittest
import logging
import module_12_4
logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8', format="%(asctime)s|%(levelname)s|%(message)s")

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(False,"It's fine!")
    def test_walk(self):
        try:
            r1 = module_12_4.Runner("Vova",5)
        except ValueError as err:
            logging.warning("Неверная скорость для Runner", err)
        else:
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50)


    @unittest.skipIf(False,"It's fine!")
    def test_run(self):
        try:
            r2 = module_12_4.Runner("1234", 6)
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner", err)
        else:
            logging.info('"test_run" выполнен успешно')
            for i in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100)


    @unittest.skipIf(False,"It's fine!")
    def test_challenge(self):
        r3 = module_12_4.Runner("Vasya",2)
        r4 = module_12_4.Runner("Yura",4)
        for i in range(10):
            r3.run()
            r4.walk()
        self.assertNotEqual(r3.distance, r4.distance)


if __name__ == "__main__":
    unittest.main()