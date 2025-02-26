# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///health_data.db'  # 数据库配置
    SECRET_KEY = os.urandom(24)  # 秘钥
    UPLOAD_FOLDER = 'uploads'  # 上传文件目录
    SQLALCHEMY_TRACK_MODIFICATIONS = False
