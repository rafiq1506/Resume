from flask import Flask, render_template
from keep_alive import keep_alive
keep_alive()

# app = Flask(__name__)
app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


