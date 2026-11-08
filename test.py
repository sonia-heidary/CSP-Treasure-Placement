from main import Grid

def test():
    """
    this function tests the performance of the program in different modes
    :return: nothing
    """
    print("level: easy, method: random")
    Grid("easy", "random")
    print("-------------------------------")
    print("level: medium, method: random")
    Grid("medium", "random")
    print("-------------------------------")
    print("level: hard, method: random")
    Grid("hard", "random")
    print("-------------------------------")
    print("level: easy, method: backtracking")
    Grid("easy", "backtracking")
    print("-------------------------------")
    print("level: medium, method: backtracking")
    Grid("medium", "backtracking")
    print("-------------------------------")
    print("level: hard, method: backtracking")
    Grid("hard", "backtracking")

test()