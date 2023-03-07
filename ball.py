from turtle import Turtle


class Ball(Turtle):
    """This is a simple class for a ball"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """To move the ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # to make game a little faster

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1  # when game reset we want to reset the ball speed
        self.bounce_x()
