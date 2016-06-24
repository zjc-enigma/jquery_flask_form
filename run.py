from flask import Flask
from flask import render_template
from flask import jsonify
from flask import send_from_directory, request, Response

app = Flask(__name__)

@app.route('/')
def interactive():
	return render_template('index.html')


@app.route('/background_process')
def background_process():
	try:
		lang = request.args.get('proglang', 0, type=str)
		if lang.lower() == 'python':
			return jsonify(result='You are wise')
		else:
			return jsonify(result='Try again.')

	except Exception as e:
		return str(e)


if __name__ == "__main__":
    app.run()
