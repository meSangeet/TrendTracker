from flask import Flask, jsonify, render_template
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Ensure index.html is in the templates folder

@app.route('/run-script', methods=['GET'])
def run_script():
    try:
        # Run the Selenium script and capture its output
        result = subprocess.run(['python3', 'scrape_trending.py'], capture_output=True, text=True)
        
        # Parse the output (assuming it's JSON)
        output = result.stdout.strip()

        # Convert the output to a dictionary (if it's valid JSON)
        data = json.loads(output)

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
