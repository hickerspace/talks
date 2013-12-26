from flask import Flask, request

app = Flask(__name__)

waren = ["Shirt", "Schuhe", "Hose"]

@app.route('/waren', methods=['GET', 'POST'])
def api_waren():
	if request.method == 'GET':
		return "Waren: %s" % waren
	elif request.method == 'POST':
		neueWare = request.form['name']
		waren.append(neueWare)
		index = len(waren) - 1
		return 'Abgelegt unter id %d.' % index

@app.route('/waren/<index>')
def api_waren_nummer(index):
	return waren[int(index)]

if __name__ == '__main__':
	app.run(debug=True)
