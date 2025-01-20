from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hi there777777777777'

if __name__ == "__main__":
	app.run()