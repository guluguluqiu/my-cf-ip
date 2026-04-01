import requests

# 配置源地址
urls = {
    "IPv4": "https://raw.gitmirror.com/joname1/BestCFip/refs/heads/main/ipv4.txt",
    "IPv6": "https://raw.gitmirror.com/joname1/BestCFip/refs/heads/main/ipv6.txt"
}

# 预设端口（根据你的需求修改，这里假设为443）
PORT = "443"

def fetch_and_format():
    results = []
    
    for tag, url in urls.items():
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                lines = response.text.strip().split('\n')
                for ip in lines:
                    if ip.strip():
                        # 格式：IP:端口#说明
                        results.append(f"{ip.strip()}:{PORT}#{tag}_Cloudflare")
        except Exception as e:
            print(f"Error fetching {tag}: {e}")

    # 写入文件
    with open("ip.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(results))

if __name__ == "__main__":
    fetch_and_format()
