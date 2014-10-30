#!/usr/bin/env python3


class Base:

    def check_find_dict(self):
        pass


class BaseList(Base):

   def check_find_dict(self):
        word = 'dd'
        list_fd1 = [['aa', 2], ['dd', 1], ['d', 4]]
        list_fd2 = [['aa', 2], ['cc', 1], ['d', 4]]
        self.assertTrue(dictionary.find_in_dict(word, list_fd1) == 1, 'find word in freq dict test1 list: [false]')
        self.assertTrue(dictionary.find_in_dict(word, list_fd2) == None, 'find word in freq dict test2 list: [false]')
 

class BaseDict(Base):

    def check_find_dict(self):
        word = 'dd'
        dict_fd1 = {'aa': 2, 'dd': 1, 'd': 4}
        dict_fd2 = {'aa': 2, 'cc': 1, 'd': 4}
        self.assertTrue(dictionary.find_in_dict(word, dict_fd1) == True, 'find word in freq dict test1 dict: [false]')
        self.assertTrue(dictionary.find_in_dict(word, dict_fd2) == None, 'find word in freq dict test2 dict: [false]')


class TestFreqDict(unittest.TestCase):

    def check_realisation(self, chosen_implementation)
        dictionary = chosen_implenetation
        dictionary.check_find_dict()

    def test_list_impl(self):
        self.check_realisation(BaseList)

    def test_dict_impl(self):
        self.check_realisation(BaseDict)

if __name__ == '__main__':
    unittest.main()
