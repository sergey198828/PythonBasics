import unittest


# Unit test cases
class WordDistanceTestCase(unittest.TestCase):
    def test_not_strings(self):
        self.assertRaises(ValueError, word_distance, "b", None)
        self.assertRaises(TypeError, word_distance, 4, "a")

    def test_void_strings(self):
        expected_output = 0
        self.assertEqual(expected_output, word_distance("", ""))
        expected_output = 1
        self.assertEqual(expected_output, word_distance("", "a"))
        expected_output = 5
        self.assertEqual(expected_output, word_distance("abcde", ""))
        self.assertEqual(expected_output, word_distance("", "fghij"))

    def test_normal_strings(self):
        expected_output = 1
        self.assertEqual(expected_output, word_distance("kot", "skot"))
        expected_output = 4
        self.assertEqual(expected_output, word_distance("polynomi", "palyndrom"))


def word_distance(word1, word2):
    """Function
    Takes two words as strings
    Returns minimal distance between this strings"""

    # None is not permitted as argument
    if (word1 is None) or (word2 is None):
        raise ValueError("None is not permitted as argument")

    # Arguments must be a strings
    if (not isinstance(word1, str)) or (not isinstance(word2, str)):
        raise TypeError("Argument must be a string")

    # If one of words is empty return length of second word
    if len(word1) == 0:
        return len(word2)
    if len(word2) == 0:
        return len(word1)

    # Initializing matrix
    d = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

    # Initializing matrix
    for i in range(1, len(word1) + 1):
        d[i][0] = i

    for j in range(1, len(word2) + 1):
        d[0][j] = j

    # Dynamic calculation of all elements
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            d[i][j] = min([d[i-1][j], d[i-1][j-1], d[i][j-1]]) + (1 if word1[i-1] != word2[j-1] else 0)

    # Return final result
    return d[len(word1)][len(word2)]


if __name__ == '__main__':
    unittest.main()
