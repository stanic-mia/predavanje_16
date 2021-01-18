
from flask import Flask, render_template

# kreiranje objekta
app = Flask(__name__)

# kontroleri
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about-me")
def about():
    return render_template("about-me.html")

if __name__ == "__main__":
    app.run()