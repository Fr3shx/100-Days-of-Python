from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()  # Hide the turtle icon
        self.penup()  
        self.color("white")  
        self.score = 0  # Initialize the score
        self.goto(0, 250)  
        self.update_scoreboard()  
    
    def update_scoreboard(self):
        """Updates the scoreboard with the current score."""
        self.clear()  # Clear the previous score
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        """Increases the score by 1 and updates the scoreboard."""
        self.score += 1
        self.update_scoreboard()
