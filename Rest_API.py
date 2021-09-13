# ************************ Rest API using Pyhon flask module **************************8

# This is the problem solving on how to make the rest APIs on pyhton
from flask import Flask, jsonify

# initializing
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/armstrong/<string:number>')
def Armstrong_1(number):
    output = 0
    for num in str(number):
        Num = int(num) ** len(str(number))
        output = Num + output
        print(output)

    if int(number) == output:
        print(f"{number} is the Armstrong number...!")
        results = {
            "number": number,
            "IP": "112.232.254.25",
            "Armstrong": True,
            "Results": number + " is a Armstrong number"
        }
    else:
        print(f"{number} is not the Armstrong number...!")
        results = {
            "number": number,
            "IP": "112.232.254.25",
            "Armstrong": False,
            "Results": number + " is not a Armstrong number"
        }
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)

