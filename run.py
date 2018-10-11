# Import Statement
from flask import Flask, jsonify

# Application Instance
app = Flask(__name__)

# Creating our main route
@app.route('/')
def index():
	return jsonify({'message': 'hello world'})
# Starting up our Flask Server (helps us run the application)
if __name__ == '__main__':
	app.run(debug=True)