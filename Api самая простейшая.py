from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/users", methods={"GET"})
def returnUserInfo():
    id = int(request.args.get("id"))

    users = {
        1: {"name": "Alex", "age": 25, "city": "London"},
        2: {"name": "Max", "age": 28, "city": "Miami"},
        3: {"name": "Egor", "age": 15, "city": "LA"},
        4: {"name": "Anton", "age": 19, "city": "Las Vegas"},
        5: {"name": "Misha", "age": 22, "city": "Moscow"},
        6: {"name": "Petr", "age": 17, "city": "St.Petersburg"},
        7: {"name": "Pavel", "age": 33, "city": "Novosibirsk"},
    }

    return jsonify(users[id])


if __name__ == "__main__":
    app.run(debug=True)
