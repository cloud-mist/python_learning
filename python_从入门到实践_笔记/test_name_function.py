import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''测试name_function。py'''

    def test_first_last_name(self):
        '''测试只有姓名的例子'''    
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_flm_name(self):
        formatted_name = get_formatted_name('wolf','mozart', 'amad')
        self.assertEqual(formatted_name, 'Wolf Amad Mozart')

unittest.main()