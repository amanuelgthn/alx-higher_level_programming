#!/usr/bin/python3
""" Web server
"""
from flask import Flask, Response
app = Flask(__name__)

@app.route("/", methods=['OPTIONS', 'HEAD', 'GET', 'POST'], strict_slashes=False)
def index():
    """ Root
    """
    res = Response("4 methods allowed")
    res.headers["Allow"] = "OPTIONS, HEAD, GET, POST"
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)