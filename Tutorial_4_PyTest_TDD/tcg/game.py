from player import Player

class Game():

    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.player = self.player1
        self.opponent = self.player2
        self.end = False

    def change_player(self):
        if self.player == self.player1:
            self.player = self.player2
            self.opponent = self.player1

        else:
            self.player = self.player1
            self.opponent = self.player2

    def start_turn(self):
        self.player.set_active()

    def check_opponent(self):
        self.end = self.opponent.is_dead()
        return not self.end

    def play_turn(self):
        self.player.print_hp()
        self.player.print_hand()
        self.player.print_mana()
        
        if self.player.has_playable_cards():
            card = input('Use a card or \'pass\': ')

            if card == 'pass':
                print('You passed')
                continue_turn = False

            else:
                out = self.player.use_card(int(card))
                if out == 'error':
                    print ('\nError, use a valid card\n')
                    return self.play_turn()
                else:
                    self.opponent.damage(int(card))
                    continue_turn = True
                

        else:
            print('You have no playable cards )^:')
            continue_turn = False

        input('intro to continue...')
        print('\n')
        return continue_turn

    def close(self):
        print(self.player.name + ' is the winner, congrats!')