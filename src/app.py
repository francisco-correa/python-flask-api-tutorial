from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todos = [
    { "label": "Practice coding", "done": False },
    { "label": "Practice coding again", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
   # you can convert that variable into a json string like this
    json_text = jsonify(todos)

    # and then you can return it on the response body like this
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    return jsonify(todos)

@app.route("/todos/<int:position>", methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)
  
# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)