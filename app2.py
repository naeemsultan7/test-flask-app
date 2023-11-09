from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

data = []


@app.route("/", methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         roll = request.form['roll']
#         course = request.form['course']
#         record1 = {'name': name, 'email': email,
#                    'roll': roll, 'course': course}
#         data.append(record1)
def home():
    if request.method == 'POST':
        name = request.json['name']
        email = request.json['email']
        roll = request.json['roll']
        course = request.json['course']
        record1 = {'name': name, 'email': email,
                   'roll': roll, 'course': course}
        data.append(record1)
    return jsonify(data)
    # return render_template("home2.html")
    # return render_template("home2.html", message='Success')
    # else:
    #     return render_template("home2.html", data=data)


@app.route("/about", methods=['GET', 'POST'])
def about():
    # return render_template('about.html', data=data)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
