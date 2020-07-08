from flask import Flask, redirect, json, request, make_response, jsonify, render_template
from db import getURL, addURL
import random
import string
app = Flask(__name__)

#Routes
@app.route('/')
def home():
    return render_template("index.html")

@app.route("/<urlcode>")
def redirector(urlcode):
	redirect_url = getURL(urlcode)
	if(redirect_url):
		return redirect(redirect_url)
	else:
		return render_template("404.html")

@app.route("/s", methods=['POST'])
def shorten_url():
	original_link = request.get_json()['og_link']
	print(original_link)
	urlcode = ''.join(random.choice(string.ascii_lowercase) for i in range(6))
	shortened_url = addURL(request.host_url, original_link, urlcode)
	res = make_response(jsonify({"status": "OK", "s_url": shortened_url}), 200)
	return res

#Start the server
if __name__ == '__main__' :
	app.run(debug=True) 