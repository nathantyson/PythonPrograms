"""
Pgm9_TicTacToe.py
CSCI 220
Sammi Ramsden and Nathan Tyson
Homework Assignment 9

Purpose Statement/ Specifications:
This program creates a small tic tac toe game. It accepts user names as input and input to determine the position of
the play (1-9) and the character being played. The game will continue until one player has won or until there are no
more spaces left to play.

Design:
- Create build_board() which returns a list of numbers (1-9) to be manipulated later.
- Create display_board(numbers) which takes as a parameter a list of numbers and creates a tic tac toe board out of them
- Create fill_spot(numbers, position, character) which takes a list of numbers and the positional input from the user
  and matches them, swapping out the number for the character input from the user
- Create legal_spot(spot, character) which determines if the position of the spot is between 1 and 9 and if the
  character is either 'x' or 'o'.
- Create if_won(board) which accepts a list of numbers and determines if a winning combination of them is made by
  comparing the elements of the list that would constitute a win.
- Create if_over(board) which accepts a list of numbers and counts the number of 'x' and 'o' characters. If this total
  is 9 (the total number of spots on the board), then there are no more viable moves
- Create play_game() asks for the players names and assigns them either x or o and builds a starting board using
  display_board(build_board()).
- Generate games until there is a win or game over. Ask the user every time for position and character input, checking
  if it is a viable input, changing the board if it is, and checking again if someone has won or the game is over.
- If someone won, stop generating games and display the name of the winner
- If no one won and there are no moves left, stop generating games and display there are no moves left
"""


# Return the list of numbers to be used on the board
def build_board():
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return numbers


# Create a tic tac toe board
def display_board(numbers):
    bar = " | "
    line = '-' * 10

    board = numbers[0] + bar + numbers[1] + bar + numbers[2] + "\n" + line + "\n" + \
            numbers[3] + bar + numbers[4] + bar + numbers[5] + "\n" + line + "\n" + \
            numbers[6] + bar + numbers[7] + bar + numbers[8]

    print(board)


# Replace the number in the number list with the character x or o
def fill_spot(numbers, position, character):
    for i in range(len(numbers)):
        if position == numbers[i]:
            numbers[i] = character


# Determine if the spot is between 1 and 9 and the character is x or o
def legal_spot(spot, character):
    if 1 <= spot <= 9 and ((character == 'x') or (character == 'o')):
        return True
    else:
        return False


# Determine if a game is won
def if_won(board):
    # Horizontal winnings
    if board[0] == board[1] == board[2]:
        return True
    elif board[3] == board[4] == board[5]:
        return True
    elif board[6] == board[7] == board[8]:
        return True

    # Vertical winnings
    elif board[0] == board[3] == board[6]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[5] == board[8]:
        return True

    # Diagonal winnings
    elif board[0] == board[4] == board[8]:
        return True
    elif board[2] == board[4] == board[6]:
        return True

    # No winnings
    else:
        return False


# Determine if the game is over
def if_over(board):
    # Count the number of letters to determine if there are any more available moves (numbers)
    num_x = board.count('x')
    num_y = board.count('o')

    if num_x + num_y == 9:
        return True
    else:
        return False


def play_game():
    # Get names of players and assign characters
    player1 = input("Enter name of player 1:  ")
    player2 = input("Enter name of player 2: ")

    print("\n{}, you are x's \n{}, you are o's \n".format(player1, player2))
    input("Press enter to start game \n")

    # Show board using the original number list
    num_list = build_board()
    display_board(num_list)

    keep_going = True
    while keep_going:
        # Get position and character and replace in the number list
        print()
        pos = str(input("Enter a position (1-9): "))
        cha = input('Enter character (x or o): ').lower()
        print()

        # Determine if the spot if legal, if so change the board
        if legal_spot(int(pos), cha):
            fill_spot(num_list, pos, cha)
            num_list = num_list
            display_board(num_list)

            # If someone has won, end the game
            if if_won(num_list):
                if cha == 'x':
                    print("\n{} wins!".format(player1))
                    keep_going = False
                if cha == 'o':
                    print("\n{} wins!".format(player2))
                    keep_going = False

            # If the board is full, end the game
            elif if_over(num_list):
                print("\nNo more moves :( \n{} and {} tied!".format(player1, player2))
                keep_going = False

        elif not legal_spot(int(pos), cha):
            print("Illegal Move!")


def main():
    play_game()


main()
