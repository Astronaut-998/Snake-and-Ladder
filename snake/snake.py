# Snakes and Ladders -v2.1
# please install -.-> pip install termcolor


from os import name, system
from random import choice, randrange, seed
from time import sleep

from termcolor import colored


class Player:
    useable_colors = ["blue", "green", "magenta", "red"]  # noqa: RUF012
    players_numbers = 1

    def __init__(self, clr: "str" = "", plc: "int" = 0):
        self.number = Player.players_numbers
        Player.players_numbers += 1
        self.color = clr
        Player.useable_colors.remove(clr)
        self.place = plc

    def move(self, num: "int"):
        self.place += num

    def move_back(self, num: "int"):
        self.place -= num

    def dice(self):
        seed()
        self.new_dice = randrange(1, 7)
        self.move(self.new_dice)
        sleep(1)
        system("cls" if name == "nt" else "clear")
        if self.place <= 100:
            print(
                "Player",
                colored(f"[{self.number}]", self.color, attrs=["bold"]),
                f"Dice number is {self.new_dice} and new place is {self.place}",
            )
        else:
            self.move_back(self.new_dice)
            print(
                "Player",
                colored(f"[{self.number}]", self.color, attrs=["bold"]),
                f"your place is {self.place}",
            )


class Bot(Player):
    def __init__(self, plc: "int" = 0):
        self.color = choice(Player.useable_colors)
        self.useable_colors.remove(self.color)
        self.number = Player.players_numbers
        Player.players_numbers += 1
        self.place = plc


class Snake(Player):
    def __init__(self, sting_power, place):
        self.sting_power = sting_power * (-1)
        self.place = place

    def sting(self, ply_name: Player):
        ply_name.move(self.sting_power)


class Ladder(Player):
    def __init__(self, Lifting_power, place):
        self.Lifting_power = Lifting_power
        self.place = place

    def Lift(self, ply_name: Player):
        ply_name.move(self.Lifting_power)


snk1, snk2, snk3, snk4, snk5, snk6, snk7, snk8 = (
    Snake(22, 25),
    Snake(58, 59),
    Snake(37, 69),
    Snake(8, 76),
    Snake(26, 83),
    Snake(18, 91),
    Snake(68, 95),
    Snake(18, 98),
)
lad1, lad2, lad3, lad4, lad5, lad6, lad7 = (
    Ladder(11, 4),
    Ladder(70, 7),
    Ladder(22, 9),
    Ladder(19, 19),
    Ladder(3, 50),
    Ladder(19, 62),
    Ladder(10, 75),
)
snakes = [snk1, snk2, snk3, snk4, snk5, snk6, snk7, snk8]
ladders = [lad1, lad2, lad3, lad4, lad5, lad6, lad7]
snakes_places = [n.place for n in snakes]
ladder_places = [n.place for n in ladders]
board = [i for i in range(1, 101)]


def print_board_2(board: list["int"], pl1: Player, pl2: Player):
    print()
    for n in board:
        if n in snakes_places:
            print(colored("[S]", "cyan", attrs=["italic"]), end="")
        elif n in ladder_places:
            print(colored("[L]", "yellow", attrs=["italic"]), end="")
        elif n == pl1.place and n == pl2.place:
            print(colored(f"[{pl1.number}", pl1.color, attrs=["bold"]), end="")
            print(colored(f"{pl2.number}]", pl2.color, attrs=["bold"]), end="")
        elif n == pl1.place:
            print(colored(f"[{pl1.number}]", pl1.color, attrs=["bold"]), end="")
        elif n == pl2.place:
            print(colored(f"[{pl2.number}]", pl2.color, attrs=["bold"]), end="")
        else:
            if n % 10 == n:
                print(f"[0{n}]", end="")
            else:
                print(f"[{n}]", end="")
        if n % 10 == 0:
            print()
    print()


win = False


def play(ply: Player):
    global win
    if ply.__class__.__name__ == "Player":
        print(
            colored(f"[{ply.number}]", ply.color, attrs=["bold"])
            + " it's your turn ..."
        )
        input("Please press Enter key to Rolling the dice ... ")
    ply.dice()
    if ply.place == 100:
        system("cls" if name == "nt" else "clear")
        win = True
        print(
            colored(f"[{ply.number}]", ply.color, attrs=["bold"])
            + f" {ply.__class__.__name__} Wins ..."
        )
        print(colored("Game finished ...", "red", attrs=["bold"]))
    elif ply.place in snakes_places:
        snakes[snakes_places.index(ply.place)].sting(ply)
        print(
            colored(f"[{ply.number}]", ply.color, attrs=["bold"])
            + f" Getting bitten by a snake ... and it's new place is {ply.place}"
        )
    elif ply.place in ladder_places:
        ladders[ladder_places.index(ply.place)].Lift(ply)
        print(
            colored(f"[{ply.number}]", ply.color, attrs=["bold"])
            + f" was carried up via the ladder ... and it's new place is {ply.place}"
        )


def color_choose(colors):
    while True:
        i = 1
        for clr in colors:
            print(f"{i}:{clr}", end=" " * 4)
            i += 1
        print()
        try:
            color = int(input("Enter your number -> "))
        except ValueError:
            print("Please enter a NUMBER ...")
            system("cls" if name == "nt" else "clear")
            continue
        if 0 < color < len(colors) + 1:
            break
        print("Please enter a NUMBER from the list above ...")
        system("cls" if name == "nt" else "clear")
    return color


# Game
game_mode = int(
    input(
        "Select game mod ...\n1. player vs bot \t 2. player vs player \t 3. Exit\n-> "
    )
)
match game_mode:
    case 1:
        print("Welcom , Please select your color ...")
        colors = ["blue", "green", "magenta", "red"]
        color = color_choose(colors)
        players_color = colors[color - 1]
        player1 = Player(players_color, 0)
        bot1 = Bot(0)
        print_board_2(board, player1, bot1)
        while True:
            play(player1)
            if win:
                break
            print_board_2(board, player1, bot1)
            input("Please press enter to continue ...")
            play(bot1)
            if win:
                break
            print_board_2(board, player1, bot1)
    case 2:
        print("Welcom , Please select your color player1 with number 1,2,3,4...")
        colors = ["blue", "green", "magenta", "red"]
        color1 = color_choose(colors)
        players_color1 = colors[color1 - 1]
        colors.remove(players_color1)
        player1 = Player(players_color1)
        system("cls" if name == "nt" else "clear")
        print("Welcom , Please select your color player2 with number 1,2,3 ...")
        color2 = color_choose(colors)
        players_color2 = colors[color2 - 1]
        player2 = Player(players_color2)
        print_board_2(board, player1, player2)
        while True:
            play(player1)
            if win:
                break
            print_board_2(board, player1, player2)
            play(player2)
            if win:
                break
            print_board_2(board, player1, player2)
    case _:
        print("goodby")
        sleep(1)
        system("cls" if name == "nt" else "clear")
sleep(5)
