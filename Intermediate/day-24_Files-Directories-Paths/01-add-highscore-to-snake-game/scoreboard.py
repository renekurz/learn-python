from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())

        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            # With only the self.high_score everytime you start the game, it will be 0
            # With the file you will have the high_score since you programmed the game
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        
        self.score = 0
        self.update_scoreboard()