from flask import Flask

app=Flask(__name__)

@app.route("/", defaults={"path": ""})
@app.route('/<path:path>')
def king(path):
    with open("/root/king.txt", "r") as king:
        currentking = king.read()
    return currentking

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=9999)
