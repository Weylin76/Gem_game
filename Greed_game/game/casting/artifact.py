from game.casting.actor import Actor

class Artifact(Actor):
    '''
    Grabs message from message.txt

    Attributes: 
    _message (string): from the message text file
    '''

    def __init__(self):
        super().__init__() #super links to the parnet class
        self._score = 0


    def set_score(self, text):
        """
        Tell director to add or minus 1 based on artifact type
        return 
        """
        if text == 42:
            score += 1
        elif text == 79:
            score -=1
        else:
            score += 0
        self._score = score

    def get_score(self):
        """
        This gets the total points the change in point value either pos or neg
        """
        return self._score
  

