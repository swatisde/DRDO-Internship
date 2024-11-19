from flask import Flask, render_template
import os

app = Flask(__name__)

# Set the Cesium token
if os.environ.get('CESIUM_TOKEN') is None:
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI4MDI1OGUxNC04ZDMxLTQ0YWYtYTBhNS1jODFjNzhhMDBmZWIiLCJpZCI6MjE0MTk1LCJpYXQiOjE3MTUzMTg1MTB9.TwLsujwSHXLD914QpzuFP6aoLr6bQvIXwl78qtXmFxA'  # Replace with your actual default token
else:
    token = os.environ.get('CESIUM_TOKEN')

@app.route('/')
def index():
    return render_template('index.html', token=token)

if __name__ == '__main__':
    app.run(debug=True)