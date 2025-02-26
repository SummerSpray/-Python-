import pandas as pd

def process_data(filepath):
    """加载并处理 CSV 文件"""
    df = pd.read_csv(filepath)

    # 校验必要列是否存在
    required_columns = ['姓名', '年龄', '性别', '身高(cm)', '体重(kg)', '血压(高压)', '血压(低压)', '血糖(mmol/L)', '胆固醇(mmol/L)', '心率(次/分)', '步数(每日)', '病史']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"CSV 文件缺少必要列：{col}")

    # 计算 BMI：体重(kg) / (身高(cm)/100)^2
    df['bmi'] = df['体重(kg)'] / (df['身高(cm)'] / 100) ** 2

    # 生成健康建议
    df['健康建议'] = df.apply(generate_health_advice, axis=1)

    return df

def generate_health_advice(row):
    """根据健康数据生成健康建议"""
    advice = []
    
    # BMI 健康建议
    if row['bmi'] < 18.5:
        advice.append('体重过轻，建议增加营养摄入，保持适度运动。')
    elif 18.5 <= row['bmi'] < 24:
        advice.append('体重正常，保持健康饮食和适度运动。')
    elif 24 <= row['bmi'] < 28:
        advice.append('体重偏重，建议控制饮食并增加运动量。')
    else:
        advice.append('体重过重，建议控制饮食和进行规律运动。')

    # 高血压健康建议
    if row['血压(高压)'] > 140 or row['血压(低压)'] > 90:
        advice.append('血压偏高，建议减少盐分摄入，增加运动量，定期监测血压。')
    else:
        advice.append('血压正常，继续保持健康生活方式。')

    # 血糖健康建议
    if row['血糖(mmol/L)'] > 7.0:
        advice.append('血糖偏高，建议控制碳水化合物的摄入，避免高糖食品。')
    else:
        advice.append('血糖正常，继续保持均衡饮食。')

    # 胆固醇健康建议
    if row['胆固醇(mmol/L)'] > 5.2:
        advice.append('胆固醇偏高，建议控制脂肪摄入，增加运动量。')
    else:
        advice.append('胆固醇正常，保持健康饮食和适度运动。')

    # 心率健康建议
    if row['心率(次/分)'] < 60:
        advice.append('心率偏低，建议增加运动量，保持身体活跃。')
    elif row['心率(次/分)'] > 100:
        advice.append('心率偏高，建议减轻压力，保持冷静，并定期监测心率。')
    else:
        advice.append('心率正常，继续保持健康生活方式。')

    # 步数健康建议
    if row['步数(每日)'] < 5000:
        advice.append('步数较少，建议增加日常步行，至少达到每天 5000 步。')
    else:
        advice.append('步数正常，保持适当的运动量。')

    # 病史健康建议
    if '高血压' in row['病史']:
        advice.append('有高血压病史，建议定期监测血压，并遵循医生的建议。')
    if '糖尿病' in row['病史']:
        advice.append('有糖尿病病史，建议保持血糖控制，避免高糖饮食。')
    if '心脏病' in row['病史']:
        advice.append('有心脏病病史，建议定期检查心脏健康，避免过度劳累。')
    if '肥胖' in row['病史']:
        advice.append('有肥胖病史，建议控制体重，改善饮食，增加运动。')

    if '无' in row['病史']:
        advice.append('无明显病史，保持健康饮食和适度运动。')

    return " ".join(advice)
