# İbrahim Olcayto Akbudak | İş ve Sistem Analizi

GitHub Pages portföyü. Ana sayfa, Hakkımda, İngilizce profil, analiz seçkisi, laboratuvar kataloğu ve teknik notları içerir.

# Uygulamalı analiz seçkisi

Bu paket ayrı sorulara ve yöntemlere sahip sentetik SQL/Python çalışmalarını içerir. Gerçek kurum, müşteri veya GİB kayıtları kullanılmaz. Sonuçlar üretim performansı veya nedensel kanıt olarak sunulmaz. Kamuya açık gerçek P2P olay günlüğü çalışması bu paketten ayrıdır.

Python 3.10+ standart kitaplık yeterlidir.

```bash
python run.py
python run.py --study efatura-sla
python run.py --verify
```

`run.py` CSV verilerini SQLite’a yükler ve SQL sonuçlarını kayıtlı JSON ile karşılaştırır. `--verify` sabit tohumlu üretimi geçici dizinde çalıştırıp tüm CSV/JSON sonuçlarını karşılaştırır. Sayısal dosyalar hesaplama için makine biçimindedir; web raporları Türkçe sayı biçimiyle sunulur.

## Çalışmalar

- e-Fatura SLA: sansürlü kayıtlar ve vaka karması
- e-Fatura tekrar gönderim: eşlenmiş politika deneyi
- API kapasitesi: kesinti, kuyruk ve yeniden deneme
- Ödeme mutabakatı: çoklu iade, taksit ve kur
- P2P süreç madenciliği: tekrar işleme ve bekleme
- Müşteri kaybı: zaman ayrımı ve veri sızıntısı
- Stok politikası: kesikli talep ve ileri dönem testi
- Veri kalitesi: kayıt eşleştirme ve yanlış birleşme

## Dosyalar

Her çalışma klasöründe CSV, schema.sql, analysis.sql, results.json ve yöntemi/sınırları açıklayan README.md bulunur. build_advanced.py veriyi ve sonuçları yeniden üretir; catalog.json rapor kataloğudur. SHA256SUMS dosya bütünlüğünü kontrol eder.

## Açık kaynak laboratuvarları

[Proje kataloğu](https://olcayto-akbudak.github.io/projeler.html): 10 ayrı GitHub deposu ve portföy içindeki 10 koleksiyon laboratuvarı. Koleksiyon bağlantıları Türkçe belgelere gider; kaynak kod ve testler aynı koleksiyonda, bağımsız ZIP paketlerinde yer alır. Sentetik öğrenme ve doğrulama araçlarıdır; üretimde çalışan hizmetler olarak sunulmaz.

## Site

Projeler statik HTML seçkisidir; ziyaretçi tarafında GitHub API çağrısı yapılmaz. sitemap.xml tüm içerik sayfalarını listeler. Ana sayfa ve Hakkımda sayfasında aynı Person kimliği kullanılır. Sosyal profil yalnız doğrulanmış GitHub adresidir.
