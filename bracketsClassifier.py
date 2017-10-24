import unittest


# Unit test cases
class BracketsClassifierTestCase(unittest.TestCase):

    def setUp(self):
        self.classifier = BracketsClassifier()

    def test_not_string(self):
        self.assertRaises(TypeError, self.classifier.match, 1)

    def test_valid_string(self):
        expected_output = True
        self.assertEqual(self.classifier.match("(a{b+c}-[d/e])"), expected_output)

    def test_invalid_string(self):
        expected_output = False
        self.assertEqual(self.classifier.match("(a{b+c}-[d/e]("), expected_output)


class BracketsClassifier:
    """Class has a match method which taking string expression as argument"""

    def match(self, expr):
        # Argument must be a string
        if not isinstance(expr, str):
            raise TypeError("Argument must be a string")
        # We will need a stack for validation
        stack = []
        # Looking at sting char by char
        for c in expr:
            # If character is opening bracket then put it to stack
            if c in ['(', '{', '[']:
                stack.append(c)
            # If character is closing bracket then pop last open bracket from stack and match
            if c in [')', '}', ']']:
                last_open_bracket = stack.pop()
                if (c == ')' and last_open_bracket != '(') or (c == '}' and last_open_bracket != '{') or (c == ']' and last_open_bracket != '['):
                    return False
        # If not found any violations check if stack is empty and return true if yes
        return len(stack) == 0


if __name__ == '__main__':
    unittest.main()
