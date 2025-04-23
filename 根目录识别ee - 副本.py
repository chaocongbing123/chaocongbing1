import requests

# AList服务器配置
alist_url = "https://xtweebvuqanq.ap-northeast-1.clawcloudrun.com"  # 您的AList地址
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicHdkX3RzIjowLCJleHAiOjE3NDQ3NDYxOTgsIm5iZiI6MTc0NDU3MzM5OCwiaWF0IjoxNzQ0NTczMzk4fQ._R_B0PU677FB4AOtdwhBN2JcXyh918t9d8OVTB-cee8"  # 您的Token

# 步骤1: 使用Token验证登录（调用 /api/me）
def verify_token():
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(f"{alist_url}/api/me", headers=headers, timeout=10)
        response.raise_for_status()  # 抛出HTTP错误
        response_json = response.json()
        print("登录响应:", response_json)
        
        if response_json.get("code") == 200:
            print("Token验证成功！登录AList成功。")
            user_info = response_json.get("data", {})
            print(f"用户信息: {user_info}")
            
            # 步骤2: 如果登录成功，列出根目录文件
            list_root_directory()
        else:
            print("Token验证失败，错误信息:", response_json.get("message", "未知错误"))
    except requests.exceptions.RequestException as e:
        print("请求错误:", str(e))
    except ValueError:
        print("响应解析失败：非JSON格式")

# 步骤2: 列出根目录文件
def list_root_directory():
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    data = {
        "path": "/",  # 根目录
        "page": 1,
        "per_page": 10,
        "refresh": False
    }
    try:
        response = requests.post(f"{alist_url}/api/fs/list", headers=headers, json=data, timeout=10)
        response.raise_for_status()
        response_json = response.json()
        print("根目录响应:", response_json)
        
        if response_json.get("code") == 200:
            files = response_json["data"].get("content", [])
            if files:
                print("根目录文件列表:")
                for file in files:
                    print(f"- 名称: {file.get('name', '未知')}, 类型: {'文件夹' if file.get('type') == 1 else '文件'}")
            else:
                print("根目录为空，没有文件或文件夹。")
        else:
            print("列出根目录失败，错误信息:", response_json.get("message", "未知错误"))
    except requests.exceptions.RequestException as e:
        print("请求错误:", str(e))
    except ValueError:
        print("响应解析失败：非JSON格式")

# 主程序
if __name__ == "__main__":
    verify_token()