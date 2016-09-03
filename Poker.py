
#  File: Poker.py

#  Description: This is a file that plays 5 card poker

#  Student's Name: Nelson Morrow

#  Student's UT EID: ntm432

#  Partner's Name: tfwnofriends

#  Partner's UT EID: -

#  Course Name: CS 313E

#  Unique Number:

#  Date Created: 02/08/16

#  Date Last Modified: 02/10/16

import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

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
    if (self.rank == 14):
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

class Poker (object):
  def __init__ (self, num_players):
    self.deck = Deck()
    self.deck.shuffle()
    self.players = []
    numcards_in_hand = 5
    self.PPoints = 0

    for i in range (num_players):
      hand = []
      for j in range (numcards_in_hand):
        hand.append (self.deck.deal())
      self.players.append (hand)

  def play (self):

    self.playernumber = []
    # sort the hands of each player and print
    self.points_hand = []
    self.combinationlist = [] #This list will be used to store each players hand
    self.combination = 'Nothing' #Default hand
    for i in range (len(self.players)):
      sortedHand = sorted (self.players[i], reverse = True)
      self.players[i] = sortedHand
      hand = ''
      for card in sortedHand:
        hand = hand + str (card) + ' '
      print ('Player ' + str (i + 1) + " : " + hand)
      # determine the each type of hand and print
      self.is_one_pair(self.players[i]) #Begin the process of going through the possibilities
      self.is_two_pair(self.players[i])
      self.is_three_kind(self.players[i])
      self.is_straight(self.players[i])
      self.is_flush(self.players[i])
      self.is_full_house(self.players[i])
      self.is_four_kind(self.players[i])
      self.is_straight_flush(self.players[i])
      self.is_royal(self.players[i])
      # create list to store points for each hand
      self.points_hand.append(self.PPoints)
      self.combinationlist.append(self.combination)
      self.combination = 'Nothing'
      self.PPoints = 0
    if max(self.points_hand) == 0: #If everyone gets nothing and has a score of 0
        self.break_tie() #player with the highest card wins
    else: # determine winner
        self.determine_winner()
    for i in range(len(self.players)): # print players and their hands
        print('Player '+str(i+1)+': ' + str(self.combinationlist[i])+ '\n')

    print('Player '+str(self.playernumber[0]+1) + ' wins! '+ '\n') # print winner
    for i in range(len(self.players)):
        if (self.combinationlist[i] is 'Nothing'):
            print('Player ' + str(i+1) + ' ties!' )

  # determine if a hand is a royal flush
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return False

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)
    if rank_order == True and same_suit == True:
        self.PPoints = 10
        self.combination = "Royal Flush"
    return (same_suit and rank_order)


  def is_straight_flush (self, hand):
      i = 0
      rank_order = True
      same_suit = True
      while(i <= len(hand)-5):
          for k in range (i, i+5):
              same_suit = same_suit and (hand[i].suit == hand[k].suit)
          i+=1
      if same_suit == True:
          for k in range (len(hand)):
              rank_order = rank_order and (hand[k].rank == hand[0].rank-k)
          if rank_order == True and same_suit == True:
              self.PPoints = 9
              self.combination = 'Straight Flush'
              return True

      return (same_suit and rank_order)

  def is_four_kind (self, hand):
      i = 0
      same_rank = True
      while(i < len(hand)-4):
        for k in range (i, i+4):
            same_rank = same_rank and (hand[k].rank == hand[i].rank)
        if same_rank == True:
            self.PPoints = 8
            return True
        i+=1
      return (same_rank)

  def is_full_house (self, hand):
      i = 0
      same_rank = True
      while(i <= len(hand)-5):
        for k in range (0,i+3):
            same_rank = same_rank and (hand[k].rank == hand[i].rank)
        if same_rank == True:
            for p in range(k+1,k+3):
                same_rank = same_rank and (hand[p].rank == hand[k+1].rank)
            if same_rank == True:
                self.PPoints = 7
                self.combination = 'Full House'
                return True

        i+=1
      return (same_rank)

  def is_flush (self, hand):
      i = 0
      same_suit = True
      while(i <= len(hand)-5):
        for k in range (i, i+5):
            same_suit = same_suit and (hand[k].suit == hand[i].suit)
        if same_suit == True:
            self.combination = 'Flush'
            self.PPoints = 6
        return True
        i+=1
      return (same_suit)


  def is_straight (self, hand):
      i = 0
      rank_order = True
      while(i <= len(hand)-5):
        for k in range (i, i+5):
            rank_order = rank_order and (hand[k].rank == hand[i].rank-k)
        if rank_order == True:
            self.combination = 'Straight'
            self.PPoints = 5
            return True
        i+=1
      return (rank_order)


  def is_three_kind (self, hand):
      i = 0
      same_rank = True
      while(i < len(hand)-3):
        for k in range (i, i+3):
            same_rank = same_rank and (hand[k].rank == hand[i].rank)
        if same_rank == True:
            self.combination = 'Three kind'
            self.PPoints = 4
            return True
        i+=1
      return (same_rank)

  def is_two_pair (self, hand):
      i = 0
      count=0
      while(i < (len(hand)-1)):
        if (hand[i].rank == hand[i + 1].rank):
            count+=1
            i+=1
        i = i+1
      if count >= 2:
        self.combination = 'Two pair'
        self.PPoints = 3
        return True

      return False

  # determine if a hand is one pair
  def is_one_pair (self, hand):
      i = 0
      while(i < (len(hand)-1)):
        if (hand[i].rank == hand[i + 1].rank):
            self.combination = 'One pair'
            self.PPoints = 2
            return True
        i = i+1
      return False

  def is_high_card (self, hand):

      high_card = hand[0]
      high_card_rank = hand[0].rank
      return(high_card_rank)
  def determine_winner(self): #This function alters numberlist to be a list of the winners in descending order

      for i in range(len(self.points_hand)):
          self.playernumber.append(i)

      for k in range(len(self.points_hand)-1):
        for i in range(len(self.points_hand)-1):
            while self.points_hand[i] < self.points_hand[i+1]:
                temp = self.points_hand[i]
                playernumbertemp = self.playernumber[i]
                self.points_hand[i] = self.points_hand[i+1]
                self.playernumber[i] = self.playernumber[i+1]
                self.points_hand[i+1] = temp
                self.playernumber[i+1] = playernumbertemp

  def break_tie (self): #This function alters numberlist to be a list of the winners in descending order, when every player gets Nothing
  #(Score of 0)

      for i in range(len(self.points_hand)):
          self.playernumber.append(i)

      for k in range(len(self.players)-1):
        for i in range(len(self.players)-1):
          while self.is_high_card(self.players[i]) < self.is_high_card(self.players[i+1]):
            temp = self.players[i]
            playernumbertemp = self.playernumber[i]
            self.players[i] = self.players[i+1]
            self.playernumber[i] = self.playernumber[i+1]
            self.players[i+1] = temp
            self.playernumber[i+1] = playernumbertemp

      return False



def main():
  # prompt user to enter the number of players
  num_players = int (input ('Enter number of players: '))
  while ((num_players < 2) or (num_players > 6)):
    num_players = int (input ('Enter number of players: '))

  # create the Poker object
  game = Poker (num_players)

  # play the game (poker)
  game.play()


main()
