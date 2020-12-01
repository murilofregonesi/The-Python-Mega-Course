"""
Personal Website

Created on November 2020
@author: Murilo Fregonesi Falleiros
"""

from flask import Flask, render_template

app = Flask(__name__) # Create an application

# Define App Homepage
@app.route('/')
def home():
    return render_template('home.html')

# Define App About
@app.route('/about/')
def about():
    return render_template('about.html')

# Run App at script run
if __name__ == '__main__':
    app.run(debug=True)