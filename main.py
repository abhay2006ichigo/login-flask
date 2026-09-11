from flask import Flask, request ,redirect, url_for, session, Response


app = Flask(__name__)
app.secret_key = "mysecretkey"
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")   
        if username == "abhay2006" and password == "abhay@123":
            session ["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("incorrect username or password", mimetype="text/plain")
    return'''
   <h1>Login</h1>

        <form method="POST">

            <input
                type="text"
                name="username"
                placeholder="Username">

            <input
                type="password"
                name="password"
                placeholder="Password">

            <button type="submit">
                Login
            </button>
    </form>
'''

@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
       <h1>Dashboard</h1>

        <h2>Welcome {session["user"]} 🎉</h2>

        <a href="/logout">Logout</a>
        '''
    return redirect (url_for("login"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect (url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)