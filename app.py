from flask import Flask
app = Flask(__name__)  # Correctly pass __name__ to Flask

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Correctly check if this script is being run directly
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

