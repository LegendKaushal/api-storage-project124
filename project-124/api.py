from flask import Flask,jsonify,request

app = Flask(__name__)

contacts = [{
    "id": 1,
    "name": u"Raju",
    "number" : u"9989474953",
    "done" : False
    },
        {
    "id": 2,
    "name": u"Rahul",
    "number" : u"9989474953",
    "done" : False
    }
    ]

@app.route("/send-data" , methods = ["POST"])

def add_contact():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "please provide the data"
        },400)

    create_contact = {
         "id": contacts[-1]["id"]+1,
        "name": request.json["name"],
        "number" : request.json.get("number",""),
        "done" : False
    }
    contacts.append(create_contact)
    return jsonify({
            "status" : "success",
            "message" : "number saved success fully"
    })

@app.route("/get-contacts")

def get_contacts():
    return jsonify({
        "data" : contacts
    })


if(__name__ == "__main__"):
    app.run(debug = True)
