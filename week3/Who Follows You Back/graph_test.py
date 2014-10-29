from graph import Graph
import unittest


class GraphTest(unittest.TestCase):
    def setUp(self):
        self.g = Graph()
        self.g.add_edge("I", "M")
        self.g.add_edge("M", "K")
        self.g.add_edge("I", "K")
        #print(self.g)

    def test_add_edge(self):
        d = {"I": ["M", "K"], "M": ["K"], "K": []}
        self.assertDictEqual(d, self.g.edges)

    def test_get_neighbours_for(self):
        l = ["M", "K"]
        n = self.g.get_neighbours_for("I")
        self.assertListEqual(l, n)

    def test_dfs(self):
        s = set(["I", "M", "K"])
        self.assertSetEqual(s, self.g.dfs("I"))

    def test_path_between_true(self):
        self.assertTrue(self.g.path_between("I", "M"))

    def test_path_between_false(self):
        self.g.add_edge("L","I")
        self.assertFalse(self.g.path_between("I", "L"))


if __name__ == '__main__':
    unittest.main()
