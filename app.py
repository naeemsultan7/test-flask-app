from flask import Flask


@app.route("/")
def home():
    return "Hello Python with Flask"


app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
