import re
import unittest


# Unit test cases
class ValidateLoginTestCase(unittest.TestCase):
    def test_non_string_login(self):
        self.assertRaises(TypeError, login_validation, 4.1)

    def test_void_login(self):
        expected_output = ['Login length must be between 1 and 20 symbols', 'Login must start from letter', 'Login must \
end by letter or digit']
        self.assertEqual(expected_output, login_validation(""))

    def test_one_invalid_character(self):
        expected_output = ['Only letters, digits, minus and dot are permitted', 'Login must start from letter', 'Login \
must end by letter or digit']
        self.assertEqual(expected_output, login_validation("&"))

    def test_start_with_digit(self):
        expected_output = ['Login must start from letter']
        self.assertEqual(expected_output, login_validation("1-.1"))

    def test_all_good(self):
        expected_output = []
        self.assertEqual(login_validation("a-1"), expected_output)
        self.assertEqual(login_validation("a.a"), expected_output)

    def test_start_with_digit_invalid_character_inside_end_by_invalid_character(self):
        expected_output = ['Only letters, digits, minus and dot are permitted', 'Login must start from letter', 'Login \
must end by letter or digit']
        self.assertEqual(login_validation("1a.+9$"), expected_output)


def login_validation(login):
    """Function
    Takes login as string
    Returns result of compliance validation as array of strings, void array means pass"""

    # Argument must be a string
    if not isinstance(login, str):
        raise TypeError("Argument must be a string")

    result = []
    # Check for length
    if len(login) < 1 or len(login) > 20:
        result.append("Login length must be between 1 and 20 symbols")
    # Check if has only appropriate letters
    if not re.match(r"^[A-Za-z0-9.-]*$", login):
        result.append("Only letters, digits, minus and dot are permitted")
    # Check first character
    if not re.match(r"^[A-Za-z]", login):
        result.append("Login must start from letter")
    # Check last character
    if not re.match(r".*[A-Za-z0-9]$", login):
        result.append("Login must end by letter or digit")
    return result


if __name__ == '__main__':
    unittest.main()
