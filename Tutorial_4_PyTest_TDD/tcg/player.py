import random

class Player():

    def __init__(self, name):
        self.name = name
        self.hp = 2
        self.max_mana = 0
        self.mana = 0
        self.deck = [0,0,1,1,2,2,2,3,3,3,3,4,4,4,5,5,6,6,7,8]
        self.shuffle_deck()
        self.hand = self.deck[:3]
        self.deck = self.deck[3:]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def draw(self):
        if self.deck:
            card = self.deck.pop(0)
            print('You draw: ' + str(card))

            if len(self.hand) < 5:
                
                self.hand.append(card)

            else:
                print('But your hand is full )^:')

        else:
            self.hp -= 1
            print('Bleeding out! you have no cards left')

        print()

    def damage(self, amount):
        self.hp -= amount
        if amount == 0:
            print('\n' + self.name + ' took ' + str(amount) + ' damage lmao\n')
        else:
            print('\n' + self.name + ' took ' + str(amount) + ' damage!\n')

        print('Opponent\'s HP: ' + str(self.hp) + '\n')

    def use_card(self, card):
        if card in self.hand:
            self.hand.pop(self.hand.index(card))
            self.mana -= card
            return card

        else:
            return 'error'

    def print_hand(self):
        print('Hand:')
        for card in self.hand:
            print(card, end=' ')
        print()

    def print_hp(self):
        print('HP:\n' + str(self.hp))

    def print_mana(self):
        print('Mana:\n' + str(self.mana))

    def is_dead(self):
        if self.hp <= 0:
            return True

        return False

    def set_active(self):
        print(self.name + '\'s turn:')
        if self.max_mana < 10:
            self.max_mana += 1
            print('Max mana: ' + str(self.max_mana))
    
        self.mana = self.max_mana

        self.draw()

    def has_playable_cards(self):
        for card in self.hand:
            if card <= self.mana:
                return True
            
        return False