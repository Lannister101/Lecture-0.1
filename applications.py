from flask import Flask ,render_template, request



app= Flask(__name__)



@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/signin")
def signinpage():
    return render_template("signin.html")

@app.route("/addproducts")
def addproductspage():
    return render_template("addproduct.html")


@app.route("/products")
def productspage():
    names = ["1kg of tomatoes ", "A pen ", "A geometrical set"]
    prices = ["sh 100", "sh 15", " sh 200"]
    return render_template("buy.html", names=names, prices=prices )


notes = []


@app.route("/userregistartion")
def userregistrationpage():
    return render_template("userregistration.html")


@app.route("/welcomeuser" , methods=["GET" , "POST"])
def welcomeuserpage():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)

    return render_template("welcomeuserpage.html", notes=notes)

@app.route("/usersignin")
def usersigninpage():
    return render_template("usersignin.html")


@app.route("/sell")
def registrationpage():
    return render_template("registration.html")

@app.route("/hello", methods =["POST"])
def hello():
    name= request.form.get("name")
    return render_template("hello.html" ,name=name)


if __name__ == "__main__":
    app.run()
