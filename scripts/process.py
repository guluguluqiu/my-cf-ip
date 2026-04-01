import requests
import re

# 配置源地址
urls = {
    "IPv4": "https://gh-proxy.org/https://raw.githubusercontent.com/joname1/BestCFip/refs/heads/main/ipv4.txt",
    "IPv6": "https://gh-proxy.org/https://raw.githubusercontent.com/joname1/BestCFip/refs/heads/main/ipv6.txt"
}

PORT = "443"

def is_valid_ip(ip):
    # 过滤掉包含 "updated", "list", ".at" 等关键词的干扰行
    if "updated" in ip or "list" in ip or ".at" in ip:
        return False
    # 简单的正则判断：IPv4 包含点，IPv6 包含冒号
    return "." in ip or ":" in ip

def fetch_and_format():
    results = []
    
    for tag, url in urls.items():
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                lines = response.text.strip().split('\n')
                for line in lines:
                    ip = line.strip()
                    # 只有当它是有效 IP 且不为空时才处理
                    if ip and is_valid_ip(ip):
                        results.append(f"{ip}:{PORT}#{tag}_Cloudflare")
        except Exception as e:
            print(f"Error fetching {tag}: {e}")

    with open("ip.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(results))

if __name__ == "__main__":
    fetch_and_format()
