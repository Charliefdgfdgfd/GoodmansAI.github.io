from flask import Flask, render_template, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_command', methods=['POST'])
def process_command():
    command = request.json.get('command')
    
    # Call your audio-commands.py functionality here
    # For example, running a command line process:
    response = subprocess.run(['python', 'audio-commands.py', command], capture_output=True, text=True)

    return jsonify({'response': response.stdout.strip()})

if __name__ == '__main__':
    app.run(debug=True)

