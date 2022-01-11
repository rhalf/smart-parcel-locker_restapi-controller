from flask import Flask, jsonify, request
from flask_restful import Resource, Api

from service.Cu48b import Cu48b


app = Flask(__name__)
app.url_map.strict_slashes = False

api = Api(app)

@app.route('/cu48b', methods=['GET', 'DELETE'])
def cu48b_A():
    if request.method == 'GET':
        cu48b = Cu48b()
        cu48b.getStatus()
        return jsonify(
            lockers=cu48b.lockers,
            sensors=cu48b.sensors,
            result="ok"
        )
    if request.method == 'DELETE':
        cu48b = Cu48b()
        cu48b.unlockAll()
        return jsonify(result="ok")


@app.route('/cu48b/<locker_id>', methods=['GET', 'POST', 'DELETE'])
def cu48b_B(locker_id = None):
    if request.method == 'POST':
        cu48b = Cu48b()
        cu48b.unlock(0, int(locker_id))
        return jsonify(result="ok")

   


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = '0'
    response.headers["Pragma"] = "no-cache"
    return response

if __name__ == '__main__':
    app.run(debug=True)