from app import db


class UserHealthData(db.Model):
    """用户健康数据模型"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    blood_pressure = db.Column(db.String(20), nullable=False)
    blood_sugar = db.Column(db.Float, nullable=False)
    cholesterol = db.Column(db.Float, nullable=False)
    heart_rate = db.Column(db.Integer, nullable=False)
    steps = db.Column(db.Integer, nullable=False)
    medical_history = db.Column(db.Text, nullable=True)
