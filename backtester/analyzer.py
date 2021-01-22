from typing import Tuple, Dict


class Coach:

    def __init__(self):
        """
        Instance that will be useful to check statistics to improve the strategy
        that we are testing, the Coach could be associated with a trading journal.
        """
        pass

    def __iadd__(self, other):
        """
        Update the Coach instance with market information.
        """

        if other.type == 'Market':
            pass
        elif other.type == 'Fill':
            pass
        else:
            raise TypeError('The type of the information is not correct.')

        return self
    
    def __add__(self, other):
        """
        Add the attributes of this instance with the attributes of the second instance
        """
        return self
