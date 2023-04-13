from algorithms.seaser import encrypt, decrypt



def test_seaser_encrypt():
    assert encrypt("Hello, World", 5) == "Mjqqt, btwqi"
    assert encrypt("Python is a high-level, general-purpose programming language", 3) == 'SBwkrq lv d kljk-ohyho, jhqhudo-sxusrvh surjudpplqj odqjxdjh'
    assert encrypt("Mohammad Jalalnia was born in 1995", 7) == "Tvohtthk Qhshsuph Dhz ivyu pu 1995"

def test_seaser_decrypt():
    assert decrypt("Mjqqt, btwqi", 5) == "Hello, World"
    assert decrypt("SBwkrq lv d kljk-ohyho, jhqhudo-sxusrvh surjudpplqj odqjxdjh", 3) == "Python is a high-level, general-purpose programming language"
    assert decrypt("Tvohtthk Qhshsuph Dhz ivyu pu 1995", 7) == "Mohammad Jalalnia was born in 1995"

