from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    user_name = "raphel"
    return render_template("index.html", user_name=user_name)

if __name__ == "__main__":
    app.run(debug=True)