import unittest
from collections.abc import Set
from collections import UserDict
from collections import KeysView
from collections import ItemsView


class Test_1(unittest.TestCase):
    def test_hash_Set(self):
        class OneTwoThreeSet(Set):
            def __init__(self):
                self.contents = [1, 2, 3]
            def __contains__(self, x):
                return x in self.contents
            def __len__(self):
                return len(self.contents)
            def __iter__(self):
                return iter(self.contents)
            def __hash__(self):
                return self._hash()
        a, b = OneTwoThreeSet(), OneTwoThreeSet()
        self.assertTrue(hash(a) == hash(b))
        # print("\nhash(a) == hash(b)\na -> {!r}\nb -> {!r}".format(a, b))
        self.assertTrue(a == b)
        # print("\na == b\na -> {!r}\nb -> {!r}".format(a, b))
        # print("id(a)->{}\tid(b)->{}".format(id(a), id(b)))
        # print("hash(a)->{}\thash(b)->{}".format(hash(a), hash(b)))

    def test_MutableMapping_subclass(self):
        # Test issue 9214
        mymap = UserDict()
        mymap['red'] = 5
        self.assertIsInstance(mymap.keys(), Set)
        self.assertIsInstance(mymap.keys(), KeysView)
        self.assertIsInstance(mymap.items(), Set)
        self.assertIsInstance(mymap.items(), ItemsView)
    
        mymap = UserDict()
        mymap['red'] = 5
        z = mymap.keys() | {'orange'}
        self.assertIsInstance(z, set)
        list(z)
        mymap['blue'] = 7               # Shouldn't affect 'z'
        self.assertEqual(sorted(z), ['orange', 'red'])
    
        mymap = UserDict()
        mymap['red'] = 5
        z = mymap.items() | {('orange', 3)}
        self.assertIsInstance(z, set)
        list(z)
        mymap['blue'] = 7               # Shouldn't affect 'z'
        self.assertEqual(sorted(z), [('orange', 3), ('red', 5)])


if __name__ == "__main__":
    unittest.main()
