import requests
import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def print_header():
    green = "\033[92m" 
    reset = "\033[0m"
    print(f"{green}╔════════════════════════════════╗")
    print(f"║    𝑫 𝒐 𝒏  𝑪 𝒓 𝒚 𝒑 𝒕 𝒊 𝒄 𝒐      ║")
    print(f"╚════════════════════════════════╝{reset}")
    red = "\033[91m" 
    print(f"{red}@doncryptico{reset}") 
    print(f"{red}𝚅𝚒𝚜𝚒𝚝: http://doncryptico.gt.tc/{reset}") 
    print(f" ")
    print("\033[94m𝗜𝗣-𝗧𝗿𝗮𝗰𝗸𝗲𝗿 𝗩𝟭\033[0m") 
    print(f" ")
def get_ip_info(ip=""):
    try:
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url)
        data = response.json()

        print("\n📡 IP Information:")
        print(f"🔹 IP Address   : {data.get('ip', 'N/A')}")
        print(f"🌍 Hostname     : {data.get('hostname', 'N/A')}")
        print(f"🏙 City         : {data.get('city', 'N/A')}")
        print(f"🗺 Region       : {data.get('region', 'N/A')}")
        print(f"🌎 Country      : {data.get('country', 'N/A')}")
        print(f"📍 Location     : {data.get('loc', 'N/A')}")
        print(f"🏣 Postal Code  : {data.get('postal', 'N/A')}")
        print(f"⏰ Timezone     : {data.get('timezone', 'N/A')}")
        print(f"📡 ISP/Org      : {data.get('org', 'N/A')}")
        print(f"🔗 Map Link     : https://www.google.com/maps?q={data.get('loc', '')}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__": 
    clear_screen()
    print_header()
    ip = input("🔍 Enter IP Address (leave blank for your IP): ").strip()
    get_ip_info(ip)
