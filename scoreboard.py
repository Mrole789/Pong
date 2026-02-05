from turtle import Turtle
FONT = ('Courier',70,'bold')

class Scoreboard(Turtle):
    """Creating scoreboard and keep track of scores"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(-100,150)
        self.write(f'{self.score}', font=FONT)
        self.hideturtle()
        
        self.score2 = 0
        self.goto(50,150)
        self.write(f'{self.score2}', font=FONT)
        
    def increase_score(self,user):
        """Increases score of a player when the opponent misses the ball"""
        if user == 2:
            self.score += 1
        else:
            self.score2 += 1
        self.clear()
        self.goto(-100,150)
        self.write(f'{self.score}', font=FONT)
        self.goto(50,150)
        self.write(f'{self.score2}', font=FONT)
