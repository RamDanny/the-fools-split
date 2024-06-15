from flask import jsonify, request
from config import app, db
from models import MatrixEntry

@app.route('/entries', methods=['GET'])
def get_entries():
    entries = MatrixEntry.query.all()
    json_entries = [entry.to_json() for entry in entries]
    return jsonify({'entries': json_entries})

@app.route('/make_entries', methods=['POST'])
def make_entries():
    row_num = request.json.get('rowNum')
    col_num = request.json.get('colNum')
    amount = request.json.get('amount')
    if not row_num or not col_num or not amount:
        return (jsonify({'message': 'Must include row, col, amt'}), 400,)
    new_entry = MatrixEntry(row_num=row_num, col_num=col_num, amount=amount)
    try:
        db.session.add(new_entry)
        db.session.commit()
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    return jsonify({'message': 'Entry made!'}), 201

@app.route('/update_entries/<int:user_id>', methods=['PATCH'])
def update_entries(user_id):
    entry = MatrixEntry.query.get(user_id)
    if not entry:
        return jsonify({'message': 'Entry not found'}), 404
    data = request.json
    entry.row_num = data.get('rowNum', entry.row_num)
    entry.col_num = data.get('colNum', entry.col_num)
    entry.amount = data.get('amount', entry.amount)
    db.session.commit()
    return jsonify({'message': 'Entry updated!'}), 200

@app.route('/delete_entries/<int:user_id>', methods=['DELETE'])
def delete_entries(user_id):
    entry = MatrixEntry.query.get(user_id)
    if not entry:
        return jsonify({'message': 'Entry not found'}), 404
    db.session.delete(entry)
    db.session.commit()
    return jsonify({'message': 'Entry deleted!'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)