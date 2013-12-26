from flask import Flask

app = Flask(__name__)


@app.route('/<name>')
def api_hello(name):
	return 'Hallo %s!' % name


if __name__ == '__main__':
	app.run(debug=True)
