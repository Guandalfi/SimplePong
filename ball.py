from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.07
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bouce_wall(self):
        self.y_move *= -1
        

    def bouce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    
    def ball_reset(self):
        self.goto(0, 0)
        self.move_speed = 0.07
        self.x_move *= -1
        

