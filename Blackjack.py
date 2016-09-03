
'''
  File: Blackjack.py

  Description: Plays the game of Blackjack

  Student's Name: Nelson Morrow

  Student's UT EID: ntm432

  Partner's Name: tfwnofriends

  Partner's UT EID: tfwnofriends

  Course Name: CS 313E

  Unique Number:

  Date Created: 03/11/16

  Date Last Modified:

'''
import random

class Card (object):
  RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

  SUITS = ('C', 'D', 'H', 'S')

  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  def __str__ (self):
    if (self.rank == 1):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)

class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  def shuffle (self):
    random.shuffle (self.deck)

  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Player (object):
  # cards is a list of card objects
  def __init__ (self, cards):
    self.cards = cards
    self.lost = False
    self.won = False
    self.stop = False
  # when a player hits append a card
  def hit (self, card):
    self.cards.append (card)

  def PrintCards(self, dealercheck = ''): # Print out the cards for specified player
      if dealercheck == '':
        returnstring = ''
        for card in self.cards:
            returnstring += str(card) + ' '
        return returnstring
      else:
          for card in self.cards:
              return str(card)

  def get_points (self):
    count = 0
    for card in self.cards:
      if card.rank > 9:
        count += 10
      elif card.rank == 1:
        count += 11
      else:
        count += card.rank

    # deduct 10 if Ace is there and and needed as 1
    for card in self.cards:
      if count <= 21:
        break
      elif card.rank == 1:
        count = count - 10

    return count

  # does the player have blackjack or not
  def has_blackjack (self):
    return (len(self.cards) == 2) and (self.get_points() == 21)
  def player_lost (self): #check if the player lost
      if self.get_points() > 21:
          self.lost = True
class Blackjack (object):

    def __init__(self, num_players):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []
        self.Points = 0
        numcards_in_hand = 2
        self.num_players = num_players
        for i in range (num_players):
            hand = []
            for j in range (numcards_in_hand):
                hand.append (self.deck.deal())
            self.players.append(Player(hand))
        hand = []
        for i in range(numcards_in_hand):
            hand.append (self.deck.deal())
        self.dealer = Player(hand)

    def Play(self):
        self.PrintHand(0, self.num_players)
        self.print_dealer()
        self.getInput()
        self.check_blackjack()
        while self.dealer.get_points() < 17:
            self.dealer.hit(self.deck.deal())
        self.print_dealer(True)
        self.check_against_dealer()
        self.score_check()
        self.print_winners()

    def getInput(self, i = 0): #This function gets user input, filtering for the correct characters.
        while i < self.num_players:
            if self.players[i].has_blackjack(): #If player has blackjack then go to next player
                i = i+1
            try:
                hit = str (raw_input ("Player " +str(i+1)+" do you want to hit? [y / n]: "))
                if hit == 'y' or hit == 'Y' or hit == 'n' or hit == 'N':
                    if(hit == 'y' or hit == 'Y'):
                        self.players[i].hit(self.deck.deal())
                        self.PrintHand(i, 1)
                        self.players[i].player_lost() #If player has lost then go to next player
                        if(self.players[i].lost == True):
                            i=i+1
                    else:
                        i=i+1
                        if (i < self.num_players):
                            self.getInput(i)
                            i = i+(self.num_players-1)
                        else:
                            i = self.num_players
                else:
                    print('Enter y or n.')
                    self.getInput(i)
                    i = i+(self.num_players-1)
            except ValueError:
                print('Enter y or n.')
                self.getInput(i)
                i = i+(self.num_players-1)
            except NameError:
                print('Enter y or n.')
                self.getInput(i)
                i = i+(self.num_players-1)

    def PrintHand(self, number, numberplayers): #Print every player from some starting number to (startingnumber + number of players to print)
        hand = ''
        for i in range(number, (number+numberplayers)):
              print("Player "+str(self.num_players-(self.num_players-i)+1)+": " + self.players[i].PrintCards() + '- '+ str(self.players[i].get_points()) +' points')
    def print_dealer(self, all = False): # print out the dealers hand. Just one card in the beginning, and all cards at end
        if all == False:
            print("Dealer: " + self.dealer.PrintCards('one')+ '\n')
        else:
            print("Dealer: " + self.dealer.PrintCards() + '- '+ str(self.dealer.get_points()) +' points'+ '\n')
    def print_winners(self): #Prints out the results, using boolean logic to separate losers, winners, push
        for i in range(len(self.players)):
            if self.players[i].won == True:
                print("Player "+str(i+1)+" wins!")
            if self.players[i].lost == True:
                print("Player "+str(i+1)+" lost!")
            elif self.players[i].won == False and self.players[i].lost == False:
                print("Player "+str(i+1)+" pushed!")
    def score_check(self):
        for i in range(self.num_players):
            if(self.players[i].get_points() < self.dealer.get_points()):
                if self.players[i].won == False:
                    self.players[i].lost = True
            if(self.players[i].get_points() > self.dealer.get_points()):
                if self.players[i].lost == False:
                    self.players[i].won = True
    def check_against_dealer(self):
        if(self.dealer.get_points() > 21):
            for i in range(0,self.num_players):
                if self.players[i].lost == False:
                    self.players[i].won = True
        if(self.dealer.get_points() == 21):
            for i in range(self.num_players):
                if(self.players[i].get_points() != 21):
                    if(self.players[i].won == False):
                        self.players[i].lost = True
    def check_blackjack(self):
        for i in range(self.num_players):
            if self.players[i].has_blackjack() == True:
                self.players[i].won = True

def main():
  # prompt user to enter the number of players
  num_players = int (input ('Enter number of players: '))
  while ((num_players < 2) or (num_players > 6)):
    num_players = int (input ('Enter number of players: '))

  game = Blackjack (num_players)
  game.Play()
main()
