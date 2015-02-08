#!/usr/bin/env python3
''' This program makes test of program send_comand_to_server. '''

import unittest
from send_comand_to_server import SshDataGetter as SDG

class TestSShDataGetter(unittest.TestCase):
    message = 'was: {}, should: {}'
    string = "$telnet -c 'echo xx' username ip password"
    words = ["$telnet", "-c", "username", "ip", "password", "echo xx"]

    def test_split_to_values(self):
        ''' Method makes a test of split_to_values in
            send_comand_to_server.py.
        '''
        SDG_object = SDG()
        result = SDG_object.split_to_values(self.string)
        assert result == self.words, self.message.format(result, self.words)

    def test_get_values(self):
        ''' Method makes tests of get_values in send_comand_to_server.py. '''
        SDG_object = SDG()
        SDG_object.get_values(self.string)
        assert SDG_object.username == self.words[2], self.message.format(
            SDG_object.username, self.words[2]
            )
        assert SDG_object.ip == self.words[3], self.message.format(
            SDG_object.ip, self.words[3]
            )
        assert SDG_object.password == self.words[4], self.message.format(
            SDG_object.password, self.words[4]
            )
        assert SDG_object.comand == self.words[5], self.message.format(
            SDG_object.comand, self.words[5]
            )


if __name__ == '__main__':
    unittest.main()
