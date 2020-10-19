from flask import Flask,render_template
app=Flask(__name__)
form={
8	"head":["","1sec","1min","1h","1day","1mon","1year","1cent"],
	"lgn":["1","1","1","1","1","1","0","0"],
	"sqrt(n)":["0","0","0","0","0","0","0","0"],
	"n":["","","","","","","",""],
	"nlgn":["","","","","","","",""],
	"n^2":["","","","","","","",""],
	"n^3":["","","","","","","",""],
	"2^n":["","","","","","","",""],
	"n":["","","","","","","",""]
}
@app.route("/visual",methods=["get","post"])
def p0():
	return render_template("algrtable.html",form=form)


if __name__=='__main__':
		app.run(debug=True)
/