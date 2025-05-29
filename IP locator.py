import requests

BLEU_CLAIR = "\033[38;5;117m"
RESET = "\033[0m"

ascii_art = r"""
  _____________       ____                    _____                  
 ___  _/__  __ \     __  / __________________ __  /______________    
___  / __  /_/ /    __  /  _  __ \  ___/  __ `/  __/  __ \_  ___/    
__/ /  _  ____/     _  /___/ /_/ / /__ / /_/ // /_ / /_/ /  /        
/___/  /_/          /_____/\____/\___/ \____/ \__/ \____//_/         
"""

def localiser_ip(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        if data['status'] == 'success':
            print(f"\n📍 Résultats pour {data['query']}:")
            print(f"Pays              : {data['country']}")
            print(f"Région            : {data['regionName']}")
            print(f"Ville             : {data['city']}")
            print(f"Fournisseur (ISP) : {data['isp']}")
            print(f"Latitude          : {data['lat']}")
            print(f"Longitude         : {data['lon']}")
            print(f"Fuseau horaire    : {data['timezone']}")
            print(f"📌 Google Maps    : https://www.google.com/maps?q={data['lat']},{data['lon']}")

            if "proxy" in data:
                print(f"VPN/Proxy détecté : {'Oui' if data['proxy'] else 'Non'}")

            isp = data['isp'].lower()
            if "sfr" in isp:
                print(f"🔗 Détails SFR     : https://www.google.com/search?q=SFR+adresse+IP+{ip}")
            elif "orange" in isp:
                print(f"🔗 Détails Orange  : https://www.google.com/search?q=Orange+adresse+IP+{ip}")
            elif "free" in isp:
                print(f"🔗 Détails Free    : https://www.google.com/search?q=Free+adresse+IP+{ip}")
            elif "bouygues" in isp:
                print(f"🔗 Détails Bouygues: https://www.google.com/search?q=Bouygues+adresse+IP+{ip}")
            elif "ovh" in isp:
                print(f"🔗 Détails OVH     : https://www.google.com/search?q=OVH+adresse+IP+{ip}")
        else:
            print("❌ Erreur : Impossible de localiser l'IP.")
    except Exception as e:
        print("⚠️ Erreur lors de la requête :", e)

if __name__ == "__main__":
    print(f"{BLEU_CLAIR}{ascii_art}{RESET}")
    ip = input("💻 IP adress : ")
    localiser_ip(ip)
    input("\n🟦 Appuyez sur Entrée pour quitter...")
