import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/nosotros')
def about():
    return render_template('nosotros.html')

@app.route('/recursos')
def resources():
    return render_template('recursos.html')

@app.route('/eventos')
def events():
    return render_template('eventos.html')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host='0.0.0.0', port=port)
