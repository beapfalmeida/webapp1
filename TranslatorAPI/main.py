import flask
import pandas as pd

translator = flask.Flask("Webpage")
df = pd.read_csv("dictionary.csv")


@translator.route("/")
def home():
    return flask.render_template("home.html")


@translator.route("/api/v1/<word>/")
def function(word):
    definition = df.loc[df['word'] == word]["definition"].squeeze()
    result = {"definition": definition, "word": word}
    return result


translator.run(debug=True)
