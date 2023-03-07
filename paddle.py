from turtle import Turtle


class Paddle(Turtle):
    """This is simple class for paddles"""

    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(x_position, y_position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


def reset_paddles(left_paddle, right_paddle):
    """This function will update paddles coordinates, when someone will earn a point"""
    left_paddle.goto(-350, 0)
    right_paddle.goto(350, 0)
