# blackjack.py is a python file hold all the classes necessary for the
# blackjack program.

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

        Note:
            Enter a note.

        Args:
            variable name (type): definition

        Returns:
            variable name (type): definition

        Example:
            Enter example if necessary.
        """
        self.deck = {}
        self.deck_shuffle()

    def deck_shuffle(self):
        """
        Enter description
        """
        self.deck = [
        { 0 : (11,"Ace","Spades")},
        { 1 : (2,"Two","Spades")},
        { 2 : (3,"Three","Spades")},
        { 3 : (4,"Four","Spades")},
        { 4 : (5,"Five","Spades")},
        { 5 : (6,"Six","Spades")},
        { 6 : (7,"Seven","Spades")},
        { 7 : (8,"Eight","Spades")},
        { 8 : (9,"Nine","Spades")},
        { 9 : (10,"Ten","Spades")},
        { 10 : (10,"Jack","Spades")},
        { 11 : (10,"Queen","Spades")},
        { 12 : (10,"King","Spades")},
        { 13 : (11,"Ace","Hearts")},
        { 14 : (2,"Two","Hearts")},
        { 15 : (3,"Three","Hearts")},
        { 16 : (4,"Four","Hearts")},
        { 17 : (5,"Five","Hearts")},
        { 18 : (6,"Six","Hearts")},
        { 19 : (7,"Seven","Hearts")},
        { 20 : (8,"Eight","Hearts")},
        { 21 : (9,"Nine","Hearts")},
        { 22 : (10,"Ten","Hearts")},
        { 23 : (10,"Jack","Hearts")},
        { 24 : (10,"Queen","Hearts")},
        { 25 : (10,"King","Hearts")},
        { 26 : (11,"Ace","Diamonds")},
        { 27 : (2,"Two","Diamonds")},
        { 28 : (3,"Three","Diamonds")},
        { 29 : (4,"Four","Diamonds")},
        { 30 : (5,"Five","Diamonds")},
        { 31 : (6,"Six","Diamonds")},
        { 32 : (7,"Seven","Diamonds")},
        { 33 : (8,"Eight","Diamonds")},
        { 34 : (9,"Nine","Diamonds")},
        { 35 : (10,"Ten","Diamonds")},
        { 36 : (10,"Jack","Diamonds")},
        { 37 : (10,"Queen","Diamonds")},
        { 38 : (10,"King","Diamonds")},
        { 39 : (11,"Ace","Clovers")},
        { 40 : (2,"Two","Clovers")},
        { 41 : (3,"Three","Clovers")},
        { 42 : (4,"Four","Clovers")},
        { 43 : (5,"Five","Clovers")},
        { 44 : (6,"Six","Clovers")},
        { 45 : (7,"Seven","Clovers")},
        { 46 : (8,"Eight","Clovers")},
        { 47 : (9,"Nine","Clovers")},
        { 48 : (10,"Ten","Clovers")},
        { 49 : (10,"Jack","Clovers")},
        { 50 : (10,"Queen","Clovers")},
        { 51 : (10,"King","Clovers")}
        ]

    def draw_card(self):
        """
        Enter description
        """
        pass

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
        """
        Enter description
        """
        pass

    def add_cards(self,cards):
        """
        Enter description
        """
        pass

    def place_bet(self):
        """
        Enter description
        """
        pass

    def card_count(self):
        """
        Enter description
        """
        pass
