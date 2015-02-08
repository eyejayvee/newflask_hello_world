from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return render_template('index.html')


@app.route("/hello/<name>")
def hello_person(name):
    return render_template('user.html', name=format(name.title()))


# Left this the same so I can see the difference between this option and templating shown above
@app.route("/jedi/<name>/<surname>")
def jedi(name, surname):
    html = """
    <h1>
      May the force be with you {}{}
    </h1>
    <p>
      "It is an honour to meet a Jedi of your race."
    </p>
    """
    return html.format(surname[:3].title(), name[:2])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
