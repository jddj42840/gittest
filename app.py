import pymongo
from flask import *
client = pymongo.MongoClient(
    "mongodb+srv://root:0000@cluster0.goald.mongodb.net/?retryWrites=true&w=majority")
print("success")
app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)
app.secret_key = "key22"

db = client.test


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/user", methods=["POST"])
def user():
    name = request.form.get("username")
    session["username"] = name
    passwd = request.form.get("password")
    collection = db.website

    collection.insert_one({
        "username": name,
        "password": passwd
    })

    return render_template("user.html", username=name)


print("Hello my name is chchchc")
print("first version in secondbranch branch")
app.run(port=5000, debug=True)
