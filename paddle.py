from turtle import Turtle

#INITIAL_X = 350
#INITIAL_y = 0
#INITIAL_HEADING = 90
PADDLE_LEN = 1
PADDLE_WID = 5


class Paddle(Turtle):
    def __init__(self, initial_x, initial_y):
        super().__init__()
        self.penup()
        #self.setheading(INITIAL_HEADING)
        self.shapesize(stretch_len=PADDLE_LEN, stretch_wid=PADDLE_WID)
        self.goto(initial_x, initial_y)
        self.shape('square')
        self.color('white')
        

    def go_south(self):
        self.goto(self.xcor(), self.ycor() + 20)
    
    def go_north(self):
        self.goto(self.xcor(), self.ycor() - 20)