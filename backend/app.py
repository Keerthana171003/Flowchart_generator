from flask import Flask, request, jsonify
from flask_cors import CORS
from pyflowchart import Flowchart

app = Flask(__name__)
CORS(app)

@app.route('/generate-flowchart', methods=['POST'])
def generate_flowchart():
    if 'code' not in request.json:
        return jsonify({"error": "No code provided"}), 400

    code = request.json['code']
    try:
        fc = Flowchart.from_code(code)
        flowchart_representation = fc.flowchart()
        # Assuming the flowchart representation is directly SVG data
        return flowchart_representation, 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


