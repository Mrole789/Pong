from turtle import Turtle

class Ball(Turtle):
    """Creating the ball and detecting collions"""
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.seth(315)
        self.tiltangle(-135)
        self.penup()
        
        self.ball_speed = 0.1
        
    def move(self,parts):
        """Moves the ball and detects collisions with walls"""
        self.forward(20)
        ball_pos = self.pos()
        ball_heading = self.heading()
        
        #Detecting ball collisions with the paddles
        for x in parts[0]:
            if self.distance(x) < 25:
                self.seth(180-ball_heading)
                self.ball_speed *= 0.9
                
        for x in parts[1]:
            if self.distance(x) < 25:
                self.seth(180-ball_heading)
                self.ball_speed *= 0.9
        
        #Detecting collisions with the walls
        if ball_pos[1] >= 220:
            self.seth(360-ball_heading)
        elif ball_pos[1] <= -220:
            self.seth(360-ball_heading)
                
    def refresh(self):
        """Sends the ball to its initial position for a new game phase"""
        self.goto(0,0)
        self.seth(180-self.heading())
        self.ball_speed = 0.1
