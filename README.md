# İbrahim Olcayto Akbudak | İş Geliştirme Analisti

GitHub Pages portföyü. Ana sayfa `index.html`, İngilizce giriş `en.html`, sekiz kapsamlı çalışmanın raporu `analizler.html` dosyasındadır. `notlar/` kaynaklı teknik yazıları içerir. `efatura-dayaniklilik-lab.html` etkileşimli sentetik laboratuvarı ve ayrı Python kaynak paketini sunar.

# Kapsamlı analiz portföyü — 02 Ekim 2026

Sekiz derin SQL/Python çalışması. Bütün veriler sentetiktir; gerçek kurum, müşteri veya GİB kaydı değildir. Python 3.10+ ve standart kitaplık yeterlidir.

## Çalıştırma ve doğrulama

```bash
python run.py
python run.py --study efatura-sla
python run.py --verify
```

`run.py` CSV kaynaklarını SQLite içine yükler, kaydedilmiş SQL sorgularını çalıştırır ve sonuçları `results.json` ile karşılaştırır. `--verify` ayrıca ayrı bir geçici klasörde bütün veri, model ve simülasyon çıktısını yeniden üretir; CSV ve JSON dosyalarını birebir karşılaştırır. Kaynak dosyaları değiştirmez.

```bash
python build_advanced.py
```

Bu komut sabit 20261002 tohumu ile bütün CSV, README, SQL, JSON ve katalog dosyalarını yeniden üretir. 27 veri/durum kontrolü yürütür. SQL tabloları yalnız sentetik veriden beslenir. Model parametreleri ve yöntem ayrıntıları `catalog.json` içinde bulunur.

## Dosya yapısı

- `build_advanced.py`: veri üretimi, simülasyonlar, model eğitimi, bootstrap ve kontrol koşulları.
- `run.py`: kaydedilmiş CSV üzerinde SQL doğrulaması ve tüm çıktıların deterministik yeniden üretme testi.
- `catalog.json`: yöntem, karar, sınır ve tam sonuçlar.
- `analizler/<çalışma>/`: birden fazla CSV, schema.sql, analysis.sql, results.json, README.md.
- `SHA256SUMS`: paketteki kaynak dosyalarının bütünlük listesi.

## Çalışmalar

- **e-Fatura SLA: sansürlü kayıtlar ve vaka karması** — 6.000 belge. Sansür · tabakalama · P95
- **e-Fatura tekrar gönderim: eşlenmiş politika deneyi** — 4.000 eşlenmiş belge. Eşlenmiş deney · iş etkisi
- **API kapasitesi: kesinti, kuyruk ve yeniden deneme** — 5.000 istek × 3 politika. Ayrık olay · kuyruk · jitter
- **Ödeme mutabakatı: çoklu iade, taksit ve kur** — 3.500 ödeme. Çoklu birleşim · kur · tolerans
- **P2P süreç madenciliği: tekrar işleme ve bekleme** — 3.000 süreç vakası. LAG · tekrar işleme · bootstrap
- **Müşteri kaybı: zaman ayrımı ve veri sızıntısı** — 5.400 müşteri. Zaman ayrımı · AUC · kalibrasyon
- **Stok politikası: kesikli talep ve ileri dönem testi** — 60 ürün × 180 gün. İleri dönem test · stok simülasyonu
- **Veri kalitesi: kayıt eşleştirme ve yanlış birleşme** — 4.000 kayıt / 2.000 kimlik. Aday üretim · precision/recall · kümeler

## Yorum sınırı

Bootstrap aralıkları seçilen sentetik örnekleme varsayımları içindir; gerçek şirket belirsizliğini göstermez. Gözlemsel farklar nedensel etki değildir. Simülasyon kazanımları üretim garantisi değildir. Karma para birimli kuruş toplamları yalnız birleşim hatasını göstermek için kullanılır; ekonomik maruziyet TRY kur dönüşümüyle verilir. Her çalışmanın özel sınırları kendi README dosyasında yer alır.


## GitHub Pages

`main` dalı ve kök dizin üzerinden yayımlanır. Canlı adres: https://olcayto-akbudak.github.io/
