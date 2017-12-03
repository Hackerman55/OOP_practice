import unittest

class TestMatrix(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_matrix(self):
        result = [[1 for i in range(2)] for j in range(2)]
        self.assertEqual(result, [[1, 1], [1, 1]])

    def test_table(self):
        result = [[1 for i in range(2)] for j in range(2)]
        s = "\n"
        for i in range(2):
            for j in range(2):
                s += str(result[i][j])+" "
            s += "\n"
        self.assertEqual(s, "\n1 1 \n1 1 \n")

    def test_main_diagonal(self):
        result = 0
        m = [[1 for i in range(2)] for j in range(2)]
        for i in range(2):
            result += m[i][i]
        self.assertEqual(result, 2)

    def test_transposition(self):
        new = [[0 for i in range(2)] for j in range(2)]
        m = [[i for i in range(2)] for j in range(2)]
        for i in range(2):
            for j in range(2):
                new[i][j] = m[j][i]
        self.assertEqual(new, [[0, 0], [1, 1]])


if __name__ == '__main__':
    unittest.main()