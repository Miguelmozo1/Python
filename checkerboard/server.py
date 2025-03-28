from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/4')
def eight_by_four():
    return render_template("4.html")

@app.route('/<int:x>/<int:y>')
def this_by_that(x,y):
    return render_template("x_by_y.html", height = x, length = y)


if __name__ == "__main__":
    app.run(port = 8000, debug = True)
