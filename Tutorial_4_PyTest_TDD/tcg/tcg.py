from game import Game

def main():

    game = Game('player1', 'player2')

    while not game.end:
        game.start_turn()

        turn = game.play_turn()
        while turn:
            turn = game.check_opponent()
            if not game.end:
                print(game.player.name + '\'s turn:')
                turn = game.play_turn()
        
        if not game.end:
            game.change_player()

    game.close()



if __name__ == '__main__':
    main()