import unittest


# Unit test cases
class MinProductTestCase(unittest.TestCase):
    def test_not_list(self):
        self.assertRaises(TypeError, min_product, "Typo")

    def test_void_list(self):
        self.assertRaises(ValueError, min_product, [])

    def test_one_list(self):
        self.assertRaises(ValueError, min_product, [1])

    def test_two_list(self):
        expected_output = -1
        self.assertEqual(expected_output, min_product([1, -1]))

    def test_positive_list_no_zero(self):
        expected_output = 2
        self.assertEqual(expected_output, min_product([3, 3, 1, 2, 2]))

    def test_positive_list_with_zero(self):
        expected_output = 0
        self.assertEqual(expected_output, min_product([3, 1, 2, 0]))

    def test_negative_list_no_zero(self):
        expected_output = 1
        self.assertEqual(expected_output, min_product([-3, -1, -1, -2]))

    def test_negative_list_with_zero(self):
        expected_output = 0
        self.assertEqual(expected_output, min_product([-3, -1, -2, 0]))

    def test_general_list(self):
        expected_output = -10
        self.assertEqual(expected_output, min_product([10, 0, -1]))


def min_product(arr):
    """Takes array of real numbers
    Returns minimal product of 2 elements
    Raise an exception if not enough elements"""

    # Argument must be a list
    if not isinstance(arr, list):
        raise TypeError("Argument must be a list")

    # Special cases:
    # Len(arr)<2 - undefined
    if len(arr) < 2:
        raise ValueError("Array length must be greater or equal to 2")
    # Len(arr)=2 - arr[0]*arr[1]
    if len(arr) == 2:
        return arr[0] * arr[1]
    # Loop once over array to find if zero presented as well as 2 maximum and 2 minimum elements (initialize with
    # first 2)
    has_zero = True if (arr[0] == 0 or arr[1] == 0) else False
    if arr[0] >= arr[1]:
        min1, min2, max1, max2 = arr[1], arr[0], arr[0], arr[1]
    else:
        min1, min2, max1, max2 = arr[0], arr[1], arr[1], arr[0]
    for i in arr[2:]:
        if i == 0 and not has_zero:
            has_zero = True
        if i < min1:
            min2, min1 = min1, i
            continue
        if i < min2:
            min2 = i
        if i > max1:
            max2, max1 = max1, i
            continue
        if i > max2:
            max2 = i
    # Regular cases:
    # Arr has positives and negatives - min(arr)*max(arr)
    if min1 < 0 < max1:
        return min1 * max1
    # Arr has only positives without zero min1(arr)*min2(arr)
    if not has_zero:
        if min1 > 0:
            return min1*min2
    # Arr has only negatives without zero max1(arr)*max2(arr)
        else:
            return max1 * max2
    # Arr has only positives and zero or only negatives and zero - 0
    return 0


if __name__ == '__main__':
    unittest.main()


