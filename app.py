from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

# 初始化应用
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化数据库
db = SQLAlchemy(app)

# 导入模型
from models import UserHealthData


@app.route('/')
def index():
    """主页，显示所有用户数据"""
    users = UserHealthData.query.all()
    return render_template('index.html', users=users)


@app.route('/upload', methods=['POST'])
def upload():
    """处理文件上传"""
    if 'file' not in request.files:
        flash('未选择文件', 'error')
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        flash('未选择文件', 'error')
        return redirect(url_for('index'))

    try:
        # 解析 CSV 文件
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)
        data = parse_csv(filepath)

        # 插入数据库
        for entry in data:
            user = UserHealthData(**entry)
            db.session.add(user)
        db.session.commit()

        flash('数据上传成功', 'success')
        return redirect(url_for('index'))
    except Exception as e:
        flash(f'数据处理失败: {e}', 'error')
        return redirect(url_for('index'))


def parse_csv(filepath):
    """解析上传的 CSV 文件"""
    import csv
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            # 处理每行数据
            data.append({
                'name': row['姓名'],
                'age': int(row['年龄']),
                'gender': row['性别'],
                'height': float(row['身高(cm)']),
                'weight': float(row['体重(kg)']),
                'blood_pressure': row['血压'],
                'blood_sugar': float(row['血糖(mmol/L)']),
                'cholesterol': float(row['胆固醇(mmol/L)']),
                'heart_rate': int(row['心率(次/分)']),
                'steps': int(row['步数(每日)']),
                'medical_history': row['病史']
            })
    return data


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
