class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # List of three-digit strings with the same consecutive digits.
        same_digit_numbers = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"]

        # Check whether the 'num' string contains the 'same_digit_number' string or not.
        def contains(same_digit_number):
            # Iterate through the characters of 'num' up to the third-to-last character.
            for index in range(len(num) - 2):
                # Check if the current triplet in 'num' matches 'same_digit_number'.
                if num[index] == same_digit_number[0] and \
                   num[index + 1] == same_digit_number[1] and \
                   num[index + 2] == same_digit_number[2]:
                    # Return True if a match is found.
                    return True
            # Return False if no match is found in 'num'.
            return False

        # Iterate over all 'same_digit_numbers' and check if the string 'num' contains it.
        for same_digit_number in same_digit_numbers:
            if contains(same_digit_number):
                # Return the current 'same_digit_number' if found.
                return same_digit_number

        # No 3 consecutive same digits are present in the string 'num'.
        return ""
