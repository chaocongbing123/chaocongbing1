import requests
import random
import string
import time
import hashlib
import uuid
import json
import os
from datetime import datetime
import pytz
from concurrent.futures import ThreadPoolExecutor

class C:
    r = '\033[91m'
    g = '\033[92m'
    y = '\033[93m'
    b = '\033[94m'
    m = '\033[95m'
    c = '\033[96m'
    re = '\033[0m'

Name = ["VIVO-", "OPPO-", "HUAWEI-", "Honor-", "XIAOMI", "HONGMI-", "APPLE-"]
Type = ["S ", " pro ", "A "]
salts = [
    {"alg": "md5", "salt": "7xOq4Z8s"}, {"alg": "md5", "salt": "QE9/9+IQco"},
    {"alg": "md5", "salt": "WdX5J9CPLZp"}, {"alg": "md5", "salt": "NmQ5qFAXqH3w984cYhMeC5TJR8j"},
    {"alg": "md5", "salt": "cc44M+l7GDhav"}, {"alg": "md5", "salt": "KxGjo/wHB+Yx8Lf7kMP+/m9I+"},
    {"alg": "md5", "salt": "wla81BUVSmDkctHDpUT"}, {"alg": "md5", "salt": "c6wMr1sm1WxiR3i8LDAm3W"},
    {"alg": "md5", "salt": "hRLrEQCFNYi0PFPV"}, {"alg": "md5", "salt": "o1J41zIraDtJPNuhBu7Ifb/q3"},
    {"alg": "md5", "salt": "U"}, {"alg": "md5", "salt": "RrbZvV0CTu3gaZJ56PVKki4IeP"},
    {"alg": "md5", "salt": "NNuRbLckJqUp1Do0YlrKCUP"}, {"alg": "md5", "salt": "UUwnBbipMTvInA0U0E9"},
    {"alg": "md5", "salt": "VzGc"}
]
s_w = "-" * 80

def A():
    client_id = "YNxT9w7GMdWvEOKa"
    client_version = "1.49.3"
    client_secret = "dbw2OtmVEeuUvIptb1Coyg"
    package_name = "com.pikcloud.pikpak"
    password = "q12345"
    appkey = "com.pikcloud.pikpak1appkey"
    return client_id, client_version, client_secret, package_name, password, appkey

def B():
    timestamp = str(int(time.time()) * 1000)
    device_id = str(uuid.uuid4()).replace("-", "")
    PM = ""
    for i in range(3):
        r = chr(random.randint(65, 90))
        PM += r
    PM = PM + "-"
    for i in range(5):
        if random.randint(0, 4) != 2:
            r = chr(random.randint(65, 90))
        else:
            r = chr(random.randint(48, 57))
        PM += r
    PB = Name[random.randint(0, 6)] + str(random.randint(3, 9)) + Type[random.randint(0, 2)] + str(random.randint(5, 6)) + "G"
    return timestamp, device_id, PM, PB

def get_ua_key(id, k):
    rank_1 = hashlib.sha1((id + k).encode("utf-8")).hexdigest()
    rank_2 = get_hash(rank_1)
    return id + rank_2

def get_UA(id, U, t, PM, PB):
    UA = ("ANDROID-com.pikcloud.pikpak/1.49.3 accessmode/ devicename/" + PB + 
          " appname/ android-com.pikcloud.pikpak appid/ action_type/ clientid/ YNxT9w7GMdWvEOKa deviceid/" + id +
          " refresh_token/ grant_type/ devicemodel/ " + PM + " networktype/WIFI accesstype/ sessionid/ osversion/" +
          "13." + str(random.randint(0, 9)) + "." + str(random.randint(0, 9)) + " datetime/" + t + 
          " protocolversion/200 sdkversion/2.0.1.200200 clientversion/1.49.3 providername/NONE clientip/" +
          " session_origin/ devicesign/div101." + U + " platformversion/10 usrno/")
    return UA

def get_sign(orgin_str):
    for salt in salts:
        orgin_str = get_hash(orgin_str + salt["salt"])
    return orgin_str

def get_hash(str_val):
    obj = hashlib.md5()
    obj.update(str_val.encode("utf-8"))
    result = obj.hexdigest()
    return result

basicRequestHeaders_1 = {
    "Accept-Language": "zh",
    "Content-Type": "application/json; charset=utf-8",
    "Host": "user.mypikpak.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "content-type": "application/json"
}

def a1(client_id, client_secret, name, password, ca):
    url = "https://user.mypikpak.net/v1/auth/signin"
    querystring = {"client_id": client_id}
    payload = {"captcha_token": ca, "client_id": client_id, "client_secret": client_secret, "username": name, "password": password}
    response = requests.request("POST", url, json=payload, params=querystring)
    print("正在登录: ", C.c, response.text, C.re)
    print()
    print()
    return json.loads(response.text)

def p4(client_id, captcha_token, device_id, captcha_sign, email, timestamp, User_Agent, proxies):
    url = "https://user.mypikpak.net/v1/shield/captcha/init?client_id=YNxT9w7GMdWvEOKa"
    querystring = {"client_id": client_id}
    payload = {
        "action": "POST:/v1/auth/signup",
        "captcha_token": captcha_token,
        "client_id": client_id,
        "device_id": device_id,
        "meta": {
            "captcha_sign": "1." + captcha_sign,
            "user_id": "",
            "package_name": "com.pikcloud.pikpak",
            "client_version": "1.49.3",
            "email": email,
            "timestamp": timestamp
        },
        "redirect_uri": "xlaccsdk01://xbase.cloud/callback?state=harbor"
    }
    headers = {
        "Host": "user.mypikpak.com",
        "x-device-id": device_id,
        "user-agent": User_Agent,
        "accept-language": "zh",
        "content-type": "application/json",
        "accept-encoding": "gzip"
    }
    response = requests.request("POST", url, json=payload, headers=headers, params=querystring, proxies=proxies)
    print("安全信息提交:", C.c, response.text, C.re)
    print()
    print()
    return json.loads(response.text)

def 安全token(device_id, ca, t):
    a = {
        "client_id": "YNxT9w7GMdWvEOKa",
        "action": "POST:/config/v1/activity_operation",
        "device_id": device_id,
        "meta": {
            "captcha_sign": "1." + ca,
            "client_version": "1.49.3",
            "package_name": "com.pikcloud.pikpak",
            "user_id": "",
            "timestamp": t
        }
    }
    r = requests.post("https://user.mypikpak.net/v1/shield/captcha/init", json=a)
    print("设备验证", C.c, r.text, C.re)
    print()
    return json.loads(r.text)

def start():
    c, v, s, a, p, k = A()
    t, id_val, PM, PB = B()
    q = get_sign(c + v + a + id_val + t)
    print(C.y, f"\n{'-'*80}\n", C.re)
    print(datetime.now().strftime('时间:' + C.g + '%Y年%m月%d日%H时%M分%S秒' + C.re))
    print()
    print("手机:", C.g, PB, C.re)
    print()
    print("型号:", C.g, PM, C.re)
    print()
    print("设备:", C.g, PB, PM, C.re)
    print()
    print("时间戳:", C.g, t, C.re)
    print()
    print("设备ID:", C.g, id_val, C.re)
    print()
    U = get_ua_key(id_val, k)
    print("设备key:", C.g, U, C.re)
    print()
    u = get_UA(id_val, U, t, PM, PB)
    print("设备信息:", C.g, u, C.re)
    print()
    print(C.y, f"\n{'-'*80}\n", C.re)
    return c, s, id_val, q, p, t, u, PM, PB

def login_pikpak(email):
    c, s, id_val, q, p, t, u, PM, PB = start()
    print()
    print()
    print("开始准备登录")
    ca = 安全token(id_val, q, t)['captcha_token']
    h11 = p4(c, ca, id_val, q, email, t, u, '')
    ca = h11['captcha_token']
    h1 = a1(c, s, email, p, ca)
    if 'access_token' in h1:
        access_token = h1['access_token']
        print(f"{C.g}登录成功！获取到访问令牌 for {email}{C.re}")
        return access_token
    else:
        print(f"{C.r}登录失败 for {email}：{h1.get('error', '未知错误')}{C.re}")
        return None

def create_folder_with_beijing_time(access_token, email):
    beijing_tz = pytz.timezone('Asia/Shanghai')
    beijing_time = datetime.now(beijing_tz)
    folder_name = beijing_time.strftime("%Y%m%d%H.%M%S")
    url = "https://api-drive.mypikpak.net/drive/v1/files"
    payload = {
        "kind": "drive#folder",
        "name": folder_name,
        "parent_id": ""
    }
    headers = {
        "Host": "api-drive.mypikpak.com",
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200 or response.status_code == 201:
        print(f"{C.g}文件夹 '{folder_name}' 创建成功 for {email}！{C.re}")
    else:
        print(f"{C.r}文件夹创建失败 for {email}：{response.text}{C.re}")

def process_account(email):
    print(f"{C.y}开始处理账号: {email}{C.re}")
    access_token = login_pikpak(email)
    if access_token:
        create_folder_with_beijing_time(access_token, email)
    print(f"{C.y}账号 {email} 处理完成{C.re}")
    print(f"{C.y}{'-' * 80}{C.re}")

def load_emails_from_file(filename="活跃.txt"):
    emails = []
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    email = line.strip()
                    if email:
                        emails.append(email)
            print(f"{C.g}成功从 {filename} 读取 {len(emails)} 个邮箱账号{C.re}")
        except Exception as e:
            print(f"{C.r}读取 {filename} 文件失败: {e}{C.re}")
    return emails

def save_emails_to_file(emails, filename="活跃.txt"):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for email in emails:
                file.write(email + "\n")
        print(f"{C.g}成功保存 {len(emails)} 个邮箱账号到 {filename}{C.re}")
    except Exception as e:
        print(f"{C.r}保存 {filename} 文件失败: {e}{C.re}")

def prompt_for_emails():
    print(f"{C.y}未找到 活跃.txt 文件或文件为空，请输入邮箱账号（每行一个，按空行结束输入）：{C.re}")
    emails = []
    while True:
        email = input().strip()
        if not email:  # 空行结束输入
            break
        if email:
            emails.append(email)
    if emails:
        save_emails_to_file(emails)
        print(f"{C.g}已保存 {len(emails)} 个邮箱账号到 活跃.txt{C.re}")
    else:
        print(f"{C.r}未输入任何邮箱账号，程序将退出{C.re}")
        exit(1)
    return emails

if __name__ == "__main__":
    sw = " " * 30
    print(C.y, f'{sw}PikPak 文件夹创建工具', C.re)
    print()
    start_time = time.time()

    # 读取邮箱账号
    emails = load_emails_from_file()
    if not emails:
        emails = prompt_for_emails()

    if not emails:
        print(f"{C.r}没有可处理的邮箱账号，程序退出{C.re}")
        exit(1)

    print(f"{C.y}即将处理 {len(emails)} 个邮箱账号，每次处理 2 个并发{C.re}")

    # 按每组两个账号并发处理
    for i in range(0, len(emails), 2):
        group = emails[i:i+2]
        print(f"{C.y}处理第 {i+1} 到 {i+len(group)} 个账号{C.re}")
        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(process_account, email) for email in group]
            for future in futures:
                future.result()  # 等待当前组完成
        time.sleep(2)  # 每组之间稍作延时，避免 API 限流

    print(f"{C.g}所有账号处理完成！{C.re}")
    print(f"总执行时间: {time.time() - start_time:.2f}秒")
