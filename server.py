from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe, hush hush!'


@app.route('/')
def index():
    if "user" not in session:
        session["user"] = []
    return render_template("index.html")

@app.route('/submit', methods=["POST"])
def submit():    
    temp_user = {
        "name":request.form["name"],
        "gender":request.form["gender"],
        "location":request.form["location"],
        "favorite_language":request.form["favorite_language"],
        "comment":request.form["comment"],
        "subscribe":request.form["subscribe"],
    }
    session["user"].append(temp_user)
    session.modified = True
    return redirect("/results")

@app.route('/results')
def results():
    return render_template("submission.html",user=session["user"])

@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)