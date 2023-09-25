"""
Rock, Scissors, paper
"""

first_player = input()
second_player = input()

if first_player == second_player:
    print("Ничья")
elif first_player == "камень" and second_player != "бумага":
    print("Тимур")
elif first_player == "ножницы" and second_player != "камень":
    print("Тимур")
elif first_player == "бумага" and second_player != "ножницы":
    print("Тимур")
else:
    print("Руслан")
