# CTF & Konferans Takip Aracı – Araştırma Notları

Bu proje, dünyadaki siber güvenlik yarışmalarını (CTF) ve önemli güvenlik konferanslarını tek bir noktadan takip etmek için tasarlanmış basit bir komut satırı aracıdır.

## 1. CTF (Capture The Flag) Nedir?

- Siber güvenlik alanında pratik yapmaya yönelik teknik yarışmalardır.
- Web, crypto, pwn, reverse engineering, forensics gibi kategoriler içerir.
- Takımlar veya bireysel olarak çözülür.
- Çözülen her görev bir **flag** kazandırır.

## 2. Güvenlik Konferansları

- Örnekler: DEFCON, BlackHat, OWASP etkinlikleri, yerel üniversite konferansları.
- Amaç, yeni güvenlik açıklarını, saldırı/korunma yöntemlerini ve araştırmaları paylaşmaktır.
- Öğrenciler için networking ve kariyer planlaması açısından önemlidir.

## 3. Bu Projenin Çözdüğü Problem

- CTF ve konferans tarihleri birçok farklı sitede dağınık hâlde bulunuyor.
- Kullanıcılar çoğu zaman bazı etkinlikleri kaçırıyor.
- Bu proje:
  - Etkinlikleri **tek listede** gösterir.
  - Kullanıcının ilgi alanına göre **etiket (tag) filtrelemesi** yapar.
  - Sadece **önümüzdeki 60 gün içindeki** etkinlikleri listeleyebilir.

## 4. Araştırma Sonuçları (Özet)

- CTF takvimi genelde topluluk siteleri ve organizasyon sayfaları üzerinden takip ediliyor.
- Basit bir JSON benzeri yapı ile etkinlikleri saklamak, Python ile filtreleme yapmayı kolaylaştırıyor.
- Komut satırı aracı, ekstra arayüz gerektirmeden hızlı kullanım sağlıyor.

## 5. Gelecekte Geliştirme Fikirleri

- Etkinlik verilerini manuel girmek yerine, web istekleri ile otomatik çekmek.
- Etkinlikler için hatırlatma (reminder) sistemi eklemek.
- Veriyi bir JSON dosyasına kaydedip dışarıdan güncellenebilir hâle getirmek.
