from flask import Flask,request,jsonify
from flask_cors import CORS

from bert import QA

app = Flask(__name__)
CORS(app)

model = QA("model")

@app.route("/home",methods=['GET'])
def predict():
    return "Hello to my AI platform"


@app.route("/",methods=['POST'])
def predict():
    doc = request.form.get("document")
    q = request.form.get("question")
    try:
        out = model.predict(doc,q)
        return jsonify({"result":out['answer']})
    except Exception as e:
        print(e)
        return jsonify({"result":"Model Failed"})

if __name__ == "__main__":
    app.run(port=8000)