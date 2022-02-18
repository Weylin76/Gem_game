from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):
    '''
    Grabs message from message.txt

    Attributes: 
    _message (string): from the message text file
    '''

    def __init__(self):
        super().__init__() #super links to the parnet class
        self._points = 0
        # self.pos_points = 0 #starts as empty string
        # self.neg_points = 0

    # def get_message(self):  #change to pos points
    #     """
    #     Get random message from message text file.
    #     """
    #     return self._message

    # def set_message(self,message): #set ponits
    #     """"
    #     updates the message
    #     """
    #     self._message = message

    def get_points(self):
        """
        This gets the total points the change in point value either pos or neg
        """
        return self._points

    def set_points(self, points):
        """
        Update the total points collected by the player.
        """
        self._points = points

    def change_score(self):
         #if robot postion == gem (42) position += 1
         #if robot postion == rock (79) position -= 1
         #else ==0


    
    #def artifact_falls(self):
        #create loop to make each artifact fall to the bottom of the banner
        #grab whole artifact class and make fall by looping minus 1 until it reaches bottom