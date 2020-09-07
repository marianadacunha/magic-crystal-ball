from flask import Flask, render_template
import random

# Initializing a variable of Flask
app = Flask(__name__)

@app.route("/")
def index():
    number = random.randint(0, 12)
    return render_template("index.html", number=number)

if __name__ == "__main__":
    app.run()