from flask import Flask, jsonify, redirect, send_from_directory


app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({'status':'Ok'})

@app.route('/')
def index():
    return redirect('/index.html')

@app.route('/<path:subpath>')
def static_files(subpath):
    return send_from_directory('static/',  subpath)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
