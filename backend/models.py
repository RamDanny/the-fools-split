from config import db
from sqlalchemy import UniqueConstraint

class MatrixEntry(db.Model):
    __tablename__ = 'fools'
    id = db.Column(db.Integer, primary_key=True)
    row_num = db.Column(db.Integer, unique=False, nullable=False)
    col_num = db.Column(db.Integer, unique=False, nullable=False)
    amount = db.Column(db.Integer, unique=False, nullable=False)

    __table_args__ = (UniqueConstraint('row_num', 'col_num', name='uniqpair'),)

    def to_json(self):
        return {
            'id': self.id,
            'rowNum': self.row_num,
            'colNum': self.col_num,
            'amount': self.amount,
        }
