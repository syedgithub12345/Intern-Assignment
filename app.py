from flask import Flask, request, jsonify
from rule_engine import Node  # Import Node class
import json

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule():
    rule_string = request.json['rule_string']
    # Convert rule_string to an AST representation here
    # For simplicity, you might need to parse the rule string into nodes
    # Return the AST representation as a JSON response
    root_node = Node('operator', 'AND')  # Example root node (update with actual logic)
    return jsonify(root_node.__dict__)

@app.route('/combine_rules', methods=['POST'])
def combine_rules():
    rules = request.json['rules']
    # Logic to combine the rules into a single AST
    combined_node = Node('operator', 'OR')  # Example combined root node
    return jsonify(combined_node.__dict__)

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    json_data = request.json['data']
    ast = request.json['ast']
    # Logic to evaluate the rule against JSON data
    result = True  # Replace with actual evaluation logic
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
