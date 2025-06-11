from flask import Flask

app = Flask(__name__)

@app.route("/")
def greeting():
  return "Hey this is the updated code for the python app!"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8181)