from turtle import Turtle


STYLE=("Courier", 20 ,"bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as f:
            self.highscore=int(f.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} HIgh Score: {self.highscore}", align="center", font=STYLE)

    def reset(self):
       
        if self.score > self.highscore:
            self.highscore=self.score
            with open("data.txt","w") as f:
                f.write(str(self.highscore))
        self.score=0
        self.update_score()

    def new_score(self):
        self.score+=1
        self.update_score()
        

