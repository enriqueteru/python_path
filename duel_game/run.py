from random import randint
import Player as Player

player1 = Player.Player(input("Enter player 1 name: "))
player2 = Player.Player(input("Enter player 2 name: "))
player1.set_powers("fire")
player2.set_powers("snow")


def Game(player1: Player, player2: Player):
    player1.tell_storie()
    player2.tell_storie()
    winner = ""

    while player1.get_health() > 0 and player2.get_health() > 0:
        player1.set_strike(randint(1, 50))
        print(
            player2.name
            + " attack to "
            + player1.name
            + " total health: "
            + str(player1.get_health())
        )
        player2.set_strike(randint(1, 50))
        print(
            player1.name
            + " attack to "
            + player2.name
            + " total health: "
            + str(player2.get_health())
        )
    else:
        if player1.get_health() > 0:
            winner = player1.name
        elif player1.get_health() == 0 and player2.get_health() == 0:
            winner = "No winners all dead"
        else:
            winner = player2.name
        return print(winner)


Game(player1, player2)
