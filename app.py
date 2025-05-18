from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def run_code():
    data = request.get_json()
    code = data.get('code', '')
    try:
        result = subprocess.run(['python', '-c', code], capture_output=True, text=True)
        output = result.stdout if result.stdout else result.stderr
    except Exception as e:
        output = str(e)
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)