from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
app.secret_key = "your_secret_key" # Make this more secure in production

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)