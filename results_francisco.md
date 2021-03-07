Results from API- flask

# Coding
```python
from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todos = [
    { "label": "Practicar Flask", "done": False },
    { "label": "Crar APIs con Flask", "done": False }
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

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)
  
# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
```
![app-py](https://user-images.githubusercontent.com/75753132/110245363-79eb5600-7f41-11eb-8b82-59fcbec274ae.png)


# Post-todo
```
Method: POST
Rute: {{url}}/todos
```
### Body: 
    {"done": false,
    "label": "Descansar despúes de aprender flask"}

![post-to-do](https://user-images.githubusercontent.com/75753132/110245427-da7a9300-7f41-11eb-8070-460d577384e9.png)

# Delete-todo
## Task "Crear APIs con Flask" ha sido borrada"
```
Method: DELETE
Rute: {{url}}/todos/1
```

![delete-todo](https://user-images.githubusercontent.com/75753132/110245464-fed66f80-7f41-11eb-9bc5-ca5db8b25053.png)
