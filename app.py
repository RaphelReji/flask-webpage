from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    user_name = "raphel"
    return render_template("index.html", user_name=user_name)


@app.route("/testing")
def testing():
    user_name = "raphele"
    return render_template("testing.html", user_name=user_name)


@app.route("/greet", methods=["GET", "POST"])
def greet():
    user_name = ""

    if request.method == "POST":
        user_name = request.form.get("user_name", "").strip()

    return render_template("greet.html", user_name=user_name)

if __name__ == "__main__":
    app.run(debug=True)


