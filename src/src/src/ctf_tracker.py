# src/ctf_tracker.py

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
        "name": "BlackHat Europe",
        "type": "Conference",
        "date": "2025-12-10",
        "location": "London",
        "tags": ["security", "research"]
    },
    {
        "name": "DEFCON",
        "type": "Conference",
        "date": "2025-08-08",
        "location": "Las Vegas",
        "tags": ["security", "ctf"]
    },
]


def parse_date(d):
    return datetime.datetime.strptime(d, "%Y-%m-%d").date()


def list_all_events():
    print("\n--- TÜM ETKİNLİKLER ---")
    for e in CTF_EVENTS + CONF_EVENTS:
        print(f"- {e['date']} | {e['type']} | {e['name']} ({e['location']})")


def list_upcoming(days=60):
    today = datetime.date.today()
    limit = today + datetime.timedelta(days=days)
    print(f"\n--- Önümüzdeki {days} gün ---")
    for e in CTF_EVENTS + CONF_EVENTS:
        d = parse_date(e["date"])
        if today <= d <= limit:
            print(f"- {d} | {e['type']} | {e['name']}")


def filter_by_tag(tag):
    tag = tag.lower()
    print(f"\n--- '{tag}' etiketi için filtre ---")
    for e in CTF_EVENTS + CONF_EVENTS:
        if any(tag in t.lower() for t in e["tags"]):
            print(f"- {e['date']} | {e['type']} | {e['name']}")


def main():
    while True:
        print("\nCTF & Konferans Takip Aracı")
        print("1) Tüm etkinlikleri listele")
        print("2) Önümüzdeki 60 günü listele")
        print("3) Etikete göre filtrele")
        print("4) Çıkış")
        choice = input("Seçiminiz: ").strip()

        if choice == "1":
            list_all_events()
        elif choice == "2":
            list_upcoming()
        elif choice == "3":
            tag = input("Etiket (web, crypto, pwn, security vb.): ")
            filter_by_tag(tag)
        elif choice == "4":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    main()
