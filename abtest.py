#coding=utf-8
import aiohttp
import asyncio
import random

import requests
import random
import time
import logging
import sys
import io

# 设置标准输出编码为 UTF-8（适用于 Windows + Python 3.8）
sys.stdout = io.TextIOWrapper(io.BytesIO(), encoding='utf-8')

# 配置信息
EXPERIMENT_KEY = "exp_20251119_103626"
API_URL = "http://43.154.89.59:8001/api/v1/split"
USER_COUNT = 10000  # 测试的 user_id 数量，可调整
MAX_SLEEP = 2  # 请求间隔最大时间（防止服务器压力过大）
AUTH_TOKEN = "sUinttmFoYhXDy0IaKo1p7h2ZQtcsQHgRlpAMpoBFxzij2fRxkovPm6Jl_zRnUC53yxkIcp7NRmPkmwzP_o09A"  # 你的 Token

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# 生成随机 user_id 函数
def generate_user_id():
    return f"user_{random.randint(1000000000, 9999999999)}"


# 初始化会话对象（用于保持 cookie 和 headers）
session = requests.Session()
session.headers.update({
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "User-Agent": "Python-Script-Tester/1.0"
})


# 发送请求的函数
def send_request(user_id):
    url = f"{API_URL}?experiment_key={EXPERIMENT_KEY}&user_id={user_id}"

    print(f"发送请求到: {url}")
    logging.info(f"发送请求到: {url}")

    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()  # 检查是否发生网络异常或认证失败

        # 输出响应结果
        print(f"✅ 响应状态码: {response.status_code}")
        logging.info(f"✅ 响应状态码: {response.status_code}")
        print(f"响应内容: {response.text[:200]}...")
        logging.info(f"响应内容: {response.text[:200]}...")

    except requests.exceptions.RequestException as e:
        print(f"❌ 请求失败: {e}")
        logging.error(f"❌ 请求失败: {e}")

    # 控制请求频率
    time.sleep(random.uniform(0, MAX_SLEEP))


# 主程序
if __name__ == "__main__":
    user_ids = [generate_user_id() for _ in range(USER_COUNT)]
    for user_id in user_ids:
        send_request(user_id)
