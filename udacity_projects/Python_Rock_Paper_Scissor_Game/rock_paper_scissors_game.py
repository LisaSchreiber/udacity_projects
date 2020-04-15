"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            HumanPlayerMove = input("Choose: 'Rock' 'Paper' or "
                                    "'Scissors'?\n").lower()
            if HumanPlayerMove not in moves:
                print("Try Again!")
            else:
                break
        return HumanPlayerMove


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.p1_score += 1
        elif beats(move2, move1):
            self.p2_score += 1
        else:
            print("Tie")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        num_round = input("Please enter  number of rounds to play: ")
        for round in range(int(num_round)):
            print(f"Round {round}:")
            self.play_round()
        if self.p1_score > self.p2_score:
            print("Player 1 won!")
        elif self.p2_score > self.p1_score:
            print("Player 2 won!")
        else:
            print("This game has no Winner!")
        print(f"The score of Player 1 is {self.p1_score}")
        print(f"The score of Player 2 is {self.p2_score}.")
        print("Game over!")


if __name__ == '__main__':
    p1 = HumanPlayer()
    p2 = RandomPlayer()
    game = Game(p1, p2)
    game.play_game()
