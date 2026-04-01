import requests

# Source URLs
urls = {
    "IPv4": "https://gh-proxy.org/https://raw.githubusercontent.com/joname1/BestCFip/refs/heads/main/ipv4.txt",
    "IPv6": "https://gh-proxy.org/https://raw.githubusercontent.com/joname1/BestCFip/refs/heads/main/ipv6.txt"
}

# Target Port
PORT = "443"

def is_valid_ip(ip):
    """Filter out non-IP lines like timestamps or metadata."""
    forbidden_keywords = ["updated", "list", ".at", "Upd"]
    if any(keyword in ip for keyword in forbidden_keywords):
        return False
    # Simple check: IPv4 has dots, IPv6 has colons
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
                    if ip and is_valid_ip(ip):
                        # Format: IP:PORT#TAG_Cloudflare (All English characters)
                        results.append(f"{ip}:{PORT}#{tag}_CF")
        except Exception as e:
            print(f"Error fetching {tag}: {e}")

    # Write to file with English context
    with open("ip.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(results))

if __name__ == "__main__":
    fetch_and_format()
