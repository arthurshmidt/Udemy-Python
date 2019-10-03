# blackjack.py is a python file hold all the classes necessary for the
# blackjack program.

import random

class bj_deck():
    """Enter description.

    Attributes:
        Attribute name (type): basic description

    Methods:
        Method Name - basic description

    Note:
        Enter a note.
    """

    def __init__(self):
        """Enter description and what it does.

        Accepts (blank) and returns (blank)
        ex. Accepts an action and returns a tuple (observation, reward, done, info).

        Args:
            variable name (type): definition

        Returns:
            variable name (type): definition

        Note:
            Enter a note.

        Example:
            Enter example if necessary.
        """
        self.deck = {}
        self.deck_shuffle()

    def deck_shuffle(self):
        """Method redefines the the deck dictionary, thus adding back any Cards
        that were rearranged or removed.  In essance re-shuffling the deck.

        Arg: nothing
        Returns: nothing

        Note: This method redefines the self.deck attribute. A card is defined
        by a Tuple of (Name,Suite,Value) and a "deck" is the dictionary colletion
        of all the "cards" organized by number.

        Example: deck.deck_shuffle()
            * deck being and instance of class bj_deck()
        """
        self.deck = {
        0 : ("Ace","Spades",11),
        1 : ("Two","Spades",2),
        2 : ("Three","Spades",3),
        3 : ("Four","Spades",4),
        4 : ("Five","Spades",5),
        5 : ("Six","Spades",6),
        6 : ("Seven","Spades",7),
        7 : ("Eight","Spades",8),
        8 : ("Nine","Spades",9),
        9 : ("Ten","Spades",10),
        10 : ("Jack","Spades",10),
        11 : ("Queen","Spades",10),
        12 : ("King","Spades",10),
        13 : ("Ace","Hearts",11),
        14 : ("Two","Hearts",2),
        15 : ("Three","Hearts",3),
        16 : ("Four","Hearts",4),
        17 : ("Five","Hearts",5),
        18 : ("Six","Hearts",6),
        19 : ("Seven","Hearts",7),
        20 : ("Eight","Hearts",8),
        21 : ("Nine","Hearts",9),
        22 : ("Ten","Hearts",10),
        23 : ("Jack","Hearts",10),
        24 : ("Queen","Hearts",10),
        25 : ("King","Hearts",10),
        26 : ("Ace","Diamonds",11),
        27 : ("Two","Diamonds",2),
        28 : ("Three","Diamonds",3),
        29 : ("Four","Diamonds",4),
        30 : ("Five","Diamonds",5),
        31 : ("Six","Diamonds",6),
        32 : ("Seven","Diamonds",7),
        33 : ("Eight","Diamonds",8),
        34 : ("Nine","Diamonds",9),
        35 : ("Ten","Diamonds",10),
        36 : ("Jack","Diamonds",10),
        37 : ("Queen","Diamonds",10),
        38 : ("King","Diamonds",10),
        39 : ("Ace","Clovers",11),
        40 : ("Two","Clovers",2),
        41 : ("Three","Clovers",3),
        42 : ("Four","Clovers",4),
        43 : ("Five","Clovers",5),
        44 : ("Six","Clovers",6),
        45 : ("Seven","Clovers",7),
        46 : ("Eight","Clovers",8),
        47 : ("Nine","Clovers",9),
        48 : ("Ten","Clovers",10),
        49 : ("Jack","Clovers",10),
        50 : ("Queen","Clovers",10),
        51 : ("King","Clovers",10)
        }

    def draw_card(self):
        """Method randomly selects a card from self.deck and returns the card.

        Args: None.

        Returns:
            temp_card a tuple of (string,string,int): ("Name","Suite",Value)

        Example:
            name,suite,value = deck.draw_card() or
            card = deck.draw_card()
        """

        while True:
            random_number = randint(0,51)
            if random_number in self.deck:
                temp_card = self.deck[random_number]
                self.deck[random_number]
                return temp_card
                break

class bj_player():
    """
    Enter description, attributes and functions of the class.
    """

    def __init__(self,player_name="Computer",is_computer=True,chips=0):
        """
        Enter description
        """

        self.player_name = player_name
        self.is_computer = is_computer
        self.chips = chips
        self.cards = []                 # list of dictionaries
        self.bet = 0

    def add_chips(self,chips):
        """Adds and removes chips from self.chips.

        Accepts (blank) and returns (blank)
        ex. Accepts an action and returns a tuple (observation, reward, done, info).

        Args:
            chips (int): The amount you would like to add or remove from the
            user chip total.

        Returns: None

        Note:
            Does NOT error check for insuficient funds.

        Example: player.add_chips(-100) - removes 100 chips from balance.
        """

        self.chips += chips

    def add_cards(self,cards):
        """Enter description and what it does.

        Accepts (blank) and returns (blank)
        ex. Accepts an action and returns a tuple (observation, reward, done, info).

        Args: cards - tuple of type ("string","string",int)

        Returns: None
        """
        self.cards.append(cards)

    def place_bet(self):
        """Enter description and what it does.

        Accepts (blank) and returns (blank)
        ex. Accepts an action and returns a tuple (observation, reward, done, info).

        Args:
            variable name (type): definition

        Returns:
            variable name (type): definition

        Note:
            Enter a note.

        Example:
            Enter example if necessary.
        """
        pass

    def card_count(self):
        """Enter description and what it does.

        Accepts (blank) and returns (blank)
        ex. Accepts an action and returns a tuple (observation, reward, done, info).

        Args:
            variable name (type): definition

        Returns:
            variable name (type): definition

        Note:
            Enter a note.

        Example:
            Enter example if necessary.
        """
        pass
