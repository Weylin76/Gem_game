from game.casting.actor import Actor
from game.shared.point import Point

class Artifact(Actor):
    '''
    Grabs message from message.txt    

    Attributes: 
    _message (string): from the message text file
    '''

    def __init__(self):
        super().__init__() #super links to the parnet class
        self._score = 0


    def set_score(self):
        """
        Tell director to add or minus 1 based on artifact type
        return 
        """
    
        if self._text == '*':
            self._score += 1
        elif self._text == 'O':
            self._score -=1
        #else:
            #self._score += 0
        return self._score

    # def get_score(self):
    #     """
    #     This gets the total points the change in point value either pos or neg
    #     """
    #     return self._score
  
    # def move_next(self, max_x, max_y):
    #     """Moves the actor to its next position according to its velocity. Will wrap the position 
    #     from one side of the screen to the other when it reaches the given maximum x and y values.
        
    #     Args:
    #         max_x (int): The maximum x value.
    #         max_y (int): The maximum y value.
    #     """
    #     x = (self._position.get_x() + self._velocity.get_x()) % max_x
    #     y = (self._position.get_y() + self._velocity.get_y()+0) % max_y
    #     self._position = Point(x, y)
