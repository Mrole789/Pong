from turtle import Turtle

class Paddle():
    """creates paddles for user to ply the game"""
    def __init__(self):
        self.paddle_seg = []
        self.paddle_seg2 = []
        
        #paddle 1
        for x in range(3):
            seg = Turtle()
            seg.shape('square')
            seg.color('white')
            seg.penup()
            seg.goto(-380,230-(x*20))
            self.paddle_seg.append(seg)
            
        #paddle 2    
        for x in range(3):
            seg2 = Turtle()
            seg2.shape('square')
            seg2.color('white')
            seg2.penup()
            seg2.goto(380,-230+(x*20))
            self.paddle_seg2.append(seg2)
    
    def move_up(self):
        """Moves left paddle up"""
        self.paddle_seg[0].seth(90)
        seg_pos = self.paddle_seg[0].pos() #segment position
        
        if seg_pos[1] <= 220:
            self.paddle_seg[0].forward(20)
            for x in self.paddle_seg[1:]:
                pos = x.pos()
                x.goto(seg_pos)
                seg_pos = pos
    
    def move_down(self):
        """Moves left paddle down"""
        self.paddle_seg[-1].seth(90)
        seg_pos2 = self.paddle_seg[-1].pos() #segment position
        
        if seg_pos2[1] >= -220:
            self.paddle_seg[-1].backward(20)
            for x in self.paddle_seg[1::-1]:
                pos = x.pos()
                x.goto(seg_pos2)
                seg_pos2 = pos           

    def move_up2(self):
        """Moves right paddle up"""
        self.paddle_seg2[-1].seth(90)
        seg_pos = self.paddle_seg2[-1].pos() #segment position
        
        if seg_pos[1] <= 220:
            self.paddle_seg2[-1].forward(20)
            for x in self.paddle_seg2[1::-1]:
                pos = x.pos()
                x.goto(seg_pos)
                seg_pos = pos
    
    def move_down2(self):
        """Moves right paddle down"""
        self.paddle_seg2[0].seth(90)
        seg_pos2 = self.paddle_seg2[0].pos() #segment position
        
        if seg_pos2[1] >= -220:
            self.paddle_seg2[0].backward(20)
            for x in self.paddle_seg2[1:]:
                pos = x.pos()
                x.goto(seg_pos2)
                seg_pos2 = pos
