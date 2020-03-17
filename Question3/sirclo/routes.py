from flask import request, Response, jsonify
from sirclo.models import BeratBadan
from sirclo import app, db

@app.route('/api/v1/berat-badan/',methods=["GET"])
def daftar_berat_badan():
    sortby = request.args.get('sortby')
    id = request.args.get('id')
    query = BeratBadan.query
    if id is not None:
        berat_badan = query.get(id)
        if berat_badan is None:
            return jsonify({"message":"Data not found"}), 404
        else:
            return jsonify(berat_badan.serialize), 200
    else:
        if sortby is not None:
            try:
                query = query.order_by(getattr(BeratBadan, sortby))
            except:
                pass
        results = query.all()
        return jsonify([result.serialize for result in results]), 200

@app.route('/api/v1/berat-badan/',methods=["POST"])
def tambah_berat_badan():
    data = request.get_json()
    berat_badan = BeratBadan(
        tanggal=data['tanggal'],
        max=data['max'],
        min=data['min'],
    )
    db.session.add(berat_badan)
    db.session.commit()
    return jsonify(berat_badan.serialize), 200

@app.route('/api/v1/berat-badan/<int:id>',methods=["PUT"])
def ubah_berat_badan(id):
    data = request.get_json()
    berat_badan = BeratBadan.query.get(id)
    if berat_badan is None:
        return jsonify({"message":"Data not found"}), 404
    else:
        berat_badan.tanggal = data['tanggal'] if 'tanggal' in data else berat_badan.tanggal
        berat_badan.max = data['max'] if 'max' in data else berat_badan.max
        berat_badan.min = data['min'] if 'min' in data else berat_badan.min
        db.session.commit()
        return jsonify(berat_badan.serialize), 200
    

