import datetime

CTF_EVENTS = [
    {
        "name": "Example CTF 1",
        "type": "CTF",
        "date": "2025-03-10",
        "location": "Online",
        "tags": ["web", "crypto"]
    },
    {
        "name": "Example CTF 2",
        "type": "CTF",
        "date": "2025-04-02",
        "location": "Istanbul",
        "tags": ["pwn", "forensics"]
    },
]

CONF_EVENTS = [
    {
        "name": "Example Conference 1",
        "type": "Conference",
        "date": "2025-02-10",
        "location": "Ankara",
        "tags": ["security"]
    },
]

def list_all_events():
    print("\n=== TÜM ETKİNLİKLER ===")
    for e in CTF_EVENTS + CONF_EVENTS:
        print(f"- {e['name']} ({e['date']} — {e['location']})")

def list_upcoming():
    print("\n=== YAKLAŞAN ETKİNLİKLER (60 GÜN) ===")
    today = datetime.date.today()
    for e in CTF_EVENTS + CONF_EVENTS:
        d = datetime.datetime.strptime(e['date'], "%Y-%m-%d").date()
        if 0 <= (d - today).days <= 60:
            print(f"- {e['name']} ({e['date']})")

def filter_by_tag(tag):
    print(f"\n=== '{tag}' etiketi için filtre ===")
    for e in CTF_EVENTS + CONF_EVENTS:
        if tag.lower() in [t.lower() for t in e["tags"]]:
            print(f"- {e['name']} | {e['date']} | {e['type']}")

def main():
    while True:
        print("\nCTF & Konferans Takip Aracı")
        print("1) Tüm etkinlikleri listele")
        print("2) Yaklaşan etkinlikleri listele")
        print("3) Etikete göre filtrele")
        print("4) Çıkış")
        choice = input("Seçiminiz: ").strip()

        if choice == "1":
            list_all_events()
        elif choice == "2":
            list_upcoming()
        elif choice == "3":
            tag = input("Etiket gir: ")
            filter_by_tag(tag)
        elif choice == "4":
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
