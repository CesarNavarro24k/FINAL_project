from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return """ <h1>Hello, World!</h1>
    <a href="/random_number">¡Ver un numero aleatorio!</a>
    
    """
@app.route("/random_number")
def random_numer():
    num = random.randint(1,10)
    return f'<p> {num}</p>'

app.run(debug=True)