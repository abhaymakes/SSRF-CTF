from flask import Flask, render_template
from flask_talisman import Talisman

app = Flask(__name__)

@app.route('/')
def flag():
    return render_template('target.html')

if __name__ == "__main__":
    app.run(debug=True)
