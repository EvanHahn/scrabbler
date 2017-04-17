import unittest
from can_spell import can_spell

class Test(unittest.TestCase):
    def test_can_spell(self):
        self.assertTrue(can_spell('', ''))
        self.assertTrue(can_spell('a', ''))
        self.assertTrue(can_spell('abc', ''))
        self.assertTrue(can_spell('a', 'a'))
        self.assertTrue(can_spell('abc', 'a'))
        self.assertTrue(can_spell('abc', 'ba'))
        self.assertTrue(can_spell('abc', 'cab'))
        self.assertTrue(can_spell('?', 'a'))
        self.assertTrue(can_spell('?', 'x'))
        self.assertTrue(can_spell('??', 'ab'))
        self.assertTrue(can_spell('??', 'xy'))
        self.assertTrue(can_spell('ab?', 'a'))
        self.assertTrue(can_spell('ab?', 'ba'))
        self.assertTrue(can_spell('ab?', 'abc'))
        self.assertTrue(can_spell('ab?', 'abx'))
        self.assertTrue(can_spell('ab??', 'xabx'))

        self.assertFalse(can_spell('abc', 'd'))
        self.assertFalse(can_spell('abc', 'abcc'))
        self.assertFalse(can_spell('abc', 'abcd'))
        self.assertFalse(can_spell('ab?', 'abcd'))
        self.assertFalse(can_spell('ab?', 'dog'))
        self.assertFalse(can_spell('?', 'ab'))
        self.assertFalse(can_spell('??', 'abs'))

if __name__ == '__main__':
    unittest.main()
