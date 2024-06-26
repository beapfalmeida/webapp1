import flask

# Create a website object
app = flask.Flask("Website")

# O @ conecta o metodo à função abaixo
# Os ficheiros html têm de estar numa pasta "templates"


@app.route("/home/")
def home():
    return flask.render_template("tutorial.html")


@app.route("/about/")
def about():
    return flask.render_template("about.html")


@app.route("/store/")
def store():
    return flask.render_template("store.html")


# run the app but allow errors
app.run(debug=True)

# images should be on a folder named static
