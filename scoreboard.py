from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """This function will update user points."""
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=('Arial', 70, 'normal'))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=('Arial', 70, 'normal'))

    def left_point(self):
        """This function will add one point to left player"""
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        """This function will add one point to right player"""
        self.right_score += 1
        self.update_scoreboard()