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
        pass

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
