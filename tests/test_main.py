from unittest import TestCase

from main import first_task, second_task, third_task
from second import create_folder


class First_TestCase(TestCase):
    def test_first_task(self):
        geo_logs = [
            {'visit1': ['Белгород', 'Россия']},
            {'visit2': ['Шанхай', 'Китай']},
            {'visit3': ['Казань', 'Россия']},
            {'visit4': ['Астрахань', 'Россия']}]
        real_res = first_task(geo_logs)
        expect_result = [[['Белгород', 'Россия']], [['Казань', 'Россия']], [['Астрахань', 'Россия']]]
        self.assertEqual(real_res, expect_result)

    def test_second_task(self):
        ids = {'user1': [515, 3, 289, 54, 3],
               'user2': [54, 312, 3, 289, 515]}
        real_res = second_task(ids)
        expect_result = [289, 3, 515, 54, 312]
        self.assertEqual(real_res, expect_result)

    def test_third_task(self):
        queries = [
            'очень хочу спать',
            'ключевая ставка',
            'заклятие часть два',
            'курс по программированию',
            'репетитор по английскому языку для экзамена'
        ]
        real_res = third_task(queries)
        expect_result = {3: 60.0, 2: 20.0, 6: 20.0}
        self.assertEqual(real_res, expect_result)

class Second_TestCase(TestCase):
    def test_YA_folder(self):
        response = create_folder('Папка')
        expect_code = '<Response [201]>'
        self.assertEqual(str(response), expect_code)
