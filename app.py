from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_property_info', methods=['GET'])
def get_property_info():
    address = request.args.get('address', 'Unknown Address')
    return jsonify({"message": f"Property info for {address}"})

if __name__ == '__main__':
    app.run(debug=True)
