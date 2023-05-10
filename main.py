"""This program counts the number of vowels in a string."""

def count_vowels(string:str) -> int:
    """
    Takes in a string and returns the number of vowels in the string.
    Args:
        string (str): The string to count vowels in.
    Returns:
        int: The number of vowels in the string.
    """
    string = string.lower()
    Result = string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u")
    return Result
