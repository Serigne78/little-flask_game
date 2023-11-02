from flask import Flask
import random
app = Flask(__name__)
find = random.randint(0,9)
@app.route('/')
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXV2YzhhaWNhdm1rczl5MWJlZmc2eHcyaXR6a2gxZXRmcXNyem1zNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.gif' />"
@app.route('/<guess>')           
def guess_number(guess):
    guess = int(guess)
    if guess > find:
        return f"<h1>Too high, try again!<h1/>" \
            "<img src='https://media.tenor.com/gmHrOv0ibXUAAAAC/pourri.gif'/>"
    elif guess < find:
        return f"<h1>Too low, try again!<h1/>" \
            "<img src='https://media.tenor.com/gmHrOv0ibXUAAAAC/pourri.gif'/>'"
    else:
        return f"<h1>its correct<h1/>" \
            "<img src='https://media.tenor.com/918EwUygx1IAAAAC/mission-impossible-we-got-this.gif'/>"
            


if __name__ == "__main__":
    app.run(port=8080,debug=True)
