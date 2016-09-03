'''
  File: Eights.py

  Description: Plays the game of Eights

  Student's Name: Nelson Morrow

  Student's UT EID: ntm432

  Partner's Name: tfwnofriends

  Partner's UT EID: tfwnofriends

  Course Name: CS 313E

  Unique Number:

  Date Created: 03/10/16

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

  def cardRank (self):
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
    return rank

  def __eq__ (self, other):
    return self.rank == other.rank and self.suit == other.suit

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
  def __init__ (self, discard = False):
    self.deck = []
    if (discard == False):
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
  def add(self, card):
        self.cards.append(card)

  def remove(self, cardRem, other):
      self.deck.remove(cardRem)
      other.deck.append(cardRem)
class Player (object):
  # cards is a list of card objects
  def __init__ (self, cards):
    self.cards = cards
    self.won = False
    self.stop = False
  # when a player hits append a card
  def hit (self, card):
    self.cards.append (card)
  def remove(self, cardRem, other):
      self.cards.remove(cardRem)
      other.deck.append(cardRem)
  def PrintCards(self, dealercheck = ''): # Print out the cards for specified player
      hand = sorted (self.cards, reverse = True)
      returnstring = ''
      for card in hand:
          returnstring += str(card) + ' '
      return returnstring

  def get_points (self):
    count = 0
    for card in self.cards:
      if card.rank > 9 or card.rank == 1:
        count += 10
      elif card.rank == 8:
        count += 50
      else:
        count += card.rank

    return count


  # does the player have blackjack or not
  def has_eight (self):
      for card in self.cards:
          if card.rank == 8:
              return True
      return False
  def has_zero (self):
      if len(self.cards) == 0:
          return True
      return False

class Eights (object): #This is the class for the game of eights. It contains all methods related to gameplay of this game specifically.

    def __init__(self, num_players):
        self.deck = Deck()
        self.discardPile = Deck(True) #Creates a discard pile with the same constructor
        self.deck.remove(self.deck.deck[0],self.discardPile) #The first card of the deck goes to the discardpile
        self.gameOver = False
        self.deck.shuffle()
        self.players = []
        self.discard = Card()
        self.Points = 0
        self.round = 0
        numcards_in_hand = 5
        self.num_players = num_players
        for i in range (num_players):
            hand = []
            for j in range (numcards_in_hand):
                hand.append (self.deck.deal())
            self.players.append(Player(hand))

    def Play(self):
        self.PrintHand(0, self.num_players) #Print out the players
        while self.gameOver == False: #While no one has zero and cards in the deck
            self.round = self.round +1
            print('\n')
            print("Round: " + str(self.round))
            self.getInput()
        self.print_winners()

    def print_winners(self): #Prints out the results, using boolean logic to separate losers, winners
        for i in range(len(self.players)):
            if self.players[i].won == True:
                print("Player "+str(i+1)+" wins with "+ str(self.players[i].get_points()) + " points!")
            if self.players[i].won == False:
                print("Player "+str(i+1)+" lost with "+ str(self.players[i].get_points()) + " points!")

    def PrintHand(self, number, numberplayers): #Print every player from some starting number to (startingnumber + number of players to print)
        for i in range(number, (number+numberplayers)):
              print("Player "+str(self.num_players-(self.num_players-i)+1)+": " + self.players[i].PrintCards() + '- '+ str(self.players[i].get_points()) +' points')

    def getInput(self, i = 0): #This function gets user input, filtering for the correct characters.
        self.discard = self.discardPile.deck[len(self.discardPile.deck)-1]
        if i < self.num_players and self.gameOver == False:
            if len(self.deck.deck) == 0: #If the deck has no more cards game is over
                self.gameOver = True
            try:
                print("Discard: " + str(self.discard))

                hasacard = False #check to ensure the player has a card that is playable
                for card in self.players[i].cards:
                   if card.suit == self.discard.suit or card.rank == 8 or card.cardRank() == self.discard.cardRank(): #Playable cards have same suit rank or are an eight
                       hasacard = True

                if (hasacard == True):
                    hit = str (raw_input ("Player " +str(i+1)+" what will you discard: "))
                    suit = assignSuit(hit) # I made this because it is hard to check index for suit when '10' takes up extra character
                    if suit == self.discard.suit or hit[0:1] == '8' or hit[0:1] == self.discard.cardRank():
                        if(hit[0:1] in str(Card.RANKS)) or hit[0:2] == '10' or hit[0:1] == 'J' or hit[0:1] == 'Q' or hit[0:1] == 'K' or hit[0:1] == 'A':
                            Notindeck = True
                            for card in self.players[i].cards:
                                if card.cardRank() == hit[0:1] or card.cardRank() == hit[0:2]: #if the rank of the card is equal to the rank of input
                                    if card.suit == suit: #if the suits are equal
                                        Notindeck = False
                                        self.players[i].remove(card,self.discardPile)
                                        self.PrintHand(i, 1)
                                        if(self.players[i].has_zero() == True): #if player has no more cards game is over
                                            self.gameOver = True
                                            self.players[i].won = True
                                        if (i < self.num_players-1):
                                            self.getInput(i+1)
                                            i = i+(self.num_players-1)
                                        elif i == self.num_players-1:
                                            i = i+(self.num_players)
                                            self.getInput(i+self.num_players)
                            if Notindeck:
                                print('Enter valid card.')
                                self.getInput(i)
                        else:
                            print('Enter valid card.')
                            self.getInput(i)
                    else:
                        print('Enter valid card.')
                        self.getInput(i)
                        i = i+(self.num_players-1)
                else:
                    self.players[i].hit(self.deck.deal())
                    self.PrintHand(i, 1)
                    if (i < self.num_players-1):
                        self.getInput(i+1)
                        i = i+(self.num_players-1)
                    else:
                        i = i+(self.num_players)
                        self.getInput(i)
            except ValueError:
                print('Enter valid card.')
                self.getInput(i)
                i = i+(self.num_players-1)
            except NameError:
                print('Enter valid card.')
                self.getInput(i)
                i = i+(self.num_players-1)
        else:
            return
def assignSuit(hit): #assigns a suit to the user input string
    if hit[1:] == 'H' or hit[2:] == 'H':
        suit = 'H'
    if hit[1:] == 'S' or hit[2:] == 'S':
        suit = 'S'
    if hit[1:] == 'C' or hit[2:] == 'C':
        suit = 'C'
    if hit[1:] == 'D' or hit[2:] == 'D':
        suit = 'D'
    return suit
def main():
  # prompt user to enter the number of players
  num_players = int (input ('Enter number of players: '))
  while ((num_players < 2) or (num_players > 6)):
    num_players = int (input ('Enter number of players: '))

  game = Eights (num_players)
  game.Play()
main()
