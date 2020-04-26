from flask import Flask

app=Flask(__name__)

@app.route("/")
def king():
    with open("/root/king.txt", "r") as king:
        currentking = king.read()
    return currentking

