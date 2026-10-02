# İbrahim Olcayto Akbudak | İş Geliştirme Analisti

GitHub Pages portföyü. `analizler.html` arama, kategori filtresi, açılır raporlar ve yeniden üretilebilir kaynak paketini sunar. Sayfa ve ana sayfa toplam analiz sayısını göstermez.

# Uygulamalı analiz portföyü

Tamamen sentetik, yeniden üretilebilir SQL/Python karar çalışmaları. Gerçek kurum, müşteri veya GİB kaydı kullanılmaz. Python 3.10+ standart kitaplık yeterlidir.

```bash
python run.py
python run.py --study webhook-ack
python run.py --verify
python -m unittest test_methods.py
```

`run.py` CSV dosyalarını SQLite'a yükler ve bütün SQL sonuçlarını kaydedilmiş JSON ile karşılaştırır. `--verify` ilk çalışmaları ve yeni senaryoları ayrı geçici klasörde üretir; katalog, CSV ve sonuç dosyalarını birebir karşılaştırır. Belirsizlik, nedensellik ve ekonomik değer iddiaları her çalışmanın README dosyasında sınırlandırılır.

Yeniden oluşturma:

```bash
python build_advanced.py
python build_expansion.py
```

`build_expansion.py` aynı analiz ailelerinde ortak yöntem kodunu kullanır; her çalışmanın ayrı sorusu, tohumu, parametre varyantı, veri sözleşmesi, hesaplanan sonuçları ve karar sınırları vardır. Bunlar bağımsız akademik araştırma veya gerçek kurum vaka raporu olarak sunulmaz.

Dosyalar: `analizler/<slug>/` altında CSV, `schema.sql`, `analysis.sql`, `results.json`, `README.md`; yeni senaryolarda `contract.json`. `specs.py` konu ve iş sorularını, `catalog.json` tüm yöntem ve sonuçları, `SHA256SUMS` dosya bütünlüğünü tutar.

## Çalışmalar

- **e-Fatura SLA: sansürlü kayıtlar ve vaka karması** — Sansür · tabakalama · P95
- **e-Fatura tekrar gönderim: eşlenmiş politika deneyi** — Eşlenmiş deney · iş etkisi
- **API kapasitesi: kesinti, kuyruk ve yeniden deneme** — Ayrık olay · kuyruk · jitter
- **Ödeme mutabakatı: çoklu iade, taksit ve kur** — Çoklu birleşim · kur · tolerans
- **P2P süreç madenciliği: tekrar işleme ve bekleme** — LAG · tekrar işleme · bootstrap
- **Müşteri kaybı: zaman ayrımı ve veri sızıntısı** — Zaman ayrımı · AUC · kalibrasyon
- **Stok politikası: kesikli talep ve ileri dönem testi** — İleri dönem test · stok simülasyonu
- **Veri kalitesi: kayıt eşleştirme ve yanlış birleşme** — Aday üretim · precision/recall · kümeler
- **Webhook ACK politikası ve kayıp olay** — Eşlenmiş politika · bootstrap · maliyet duyarlılığı
- **Alias önbelleği yenileme deneyi** — Eşlenmiş politika · bootstrap · maliyet duyarlılığı
- **UBL ön kontrolünün retlere etkisi** — Eşlenmiş politika · bootstrap · maliyet duyarlılığı
- **ETag zorunluluğu ve çakışan güncelleme** — Eşlenmiş politika · bootstrap · maliyet duyarlılığı
- **Kiosk ödeme teyit ekranı deneyi** — Eşlenmiş politika · bootstrap · maliyet duyarlılığı
- **Sipariş formu doğrulama deneyi** — Eşlenmiş politika · bootstrap · maliyet duyarlılığı
- **İade inceleme kapısı deneyi** — Eşlenmiş politika · bootstrap · maliyet duyarlılığı
- **Cari kart mükerrer uyarısı deneyi** — Eşlenmiş politika · bootstrap · maliyet duyarlılığı
- **Teslimat adresi teyit deneyi** — Eşlenmiş politika · bootstrap · maliyet duyarlılığı
- **Destek talebi şablonu deneyi** — Eşlenmiş politika · bootstrap · maliyet duyarlılığı
- **Excel aktarımı önizleme deneyi** — Eşlenmiş politika · bootstrap · maliyet duyarlılığı
- **Token yenileme penceresi deneyi** — Eşlenmiş politika · bootstrap · maliyet duyarlılığı
- **Şube sürüm geçişi: farkların farkı** — Panel veri · farkların farkı · placebo · küme bootstrap
- **Fatura batch boyutu müdahalesi** — Panel veri · farkların farkı · placebo · küme bootstrap
- **Depo yerleşim değişikliği** — Panel veri · farkların farkı · placebo · küme bootstrap
- **Destek ön sınıflandırma müdahalesi** — Panel veri · farkların farkı · placebo · küme bootstrap
- **QR menü önbellek geçişi** — Panel veri · farkların farkı · placebo · küme bootstrap
- **Tedarikçi sipariş yönlendirmesi** — Panel veri · farkların farkı · placebo · küme bootstrap
- **Satın alma onay limiti değişimi** — Panel veri · farkların farkı · placebo · küme bootstrap
- **Alacak hatırlatma programı** — Panel veri · farkların farkı · placebo · küme bootstrap
- **Partner onboarding rehberi** — Panel veri · farkların farkı · placebo · küme bootstrap
- **Fiyat gösterimi sadeleştirmesi** — Panel veri · farkların farkı · placebo · küme bootstrap
- **Sayım akışı saat kesiti müdahalesi** — Panel veri · farkların farkı · placebo · küme bootstrap
- **Sürüm kabul kapısı müdahalesi** — Panel veri · farkların farkı · placebo · küme bootstrap
- **e-Fatura yanıt süresi ve sansür** — Kaplan–Meier · sağ sansür · RMST · risk kümesi
- **e-Arşiv teslimat süresi dağılımı** — Kaplan–Meier · sağ sansür · RMST · risk kümesi
- **e-İrsaliye teyit süresi dağılımı** — Kaplan–Meier · sağ sansür · RMST · risk kümesi
- **Kesinti toparlanma süresi** — Kaplan–Meier · sağ sansür · RMST · risk kümesi
- **Ödeme valör süresi ve bekleyenler** — Kaplan–Meier · sağ sansür · RMST · risk kümesi
- **İade sonuçlanma süresi** — Kaplan–Meier · sağ sansür · RMST · risk kümesi
- **Müşteri ilk aktivasyon süresi** — Kaplan–Meier · sağ sansür · RMST · risk kümesi
- **Tedarikçi uygunsuzluğu kapanış süresi** — Kaplan–Meier · sağ sansür · RMST · risk kümesi
- **Partner sözleşme tamamlama süresi** — Kaplan–Meier · sağ sansür · RMST · risk kümesi
- **Şema geçişi tamamlama süresi** — Kaplan–Meier · sağ sansür · RMST · risk kümesi
- **Stok eritme süresi ve gözlem sonu** — Kaplan–Meier · sağ sansür · RMST · risk kümesi
- **Destek yeniden açılma zaman analizi** — Kaplan–Meier · sağ sansür · RMST · risk kümesi
- **Risk ağırlıklı test portföyü seçimi** — Tam arama · min-max · bağımlılık · bütçe duyarlılığı
- **Entegrasyon yol haritası optimizasyonu** — Tam arama · min-max · bağımlılık · bütçe duyarlılığı
- **Depo iyileştirme portföyü** — Tam arama · min-max · bağımlılık · bütçe duyarlılığı
- **Tedarikçi denetim kapsamı seçimi** — Tam arama · min-max · bağımlılık · bütçe duyarlılığı
- **Veri düzeltme işlerinin önceliği** — Tam arama · min-max · bağımlılık · bütçe duyarlılığı
- **Entegrasyon kontrol portföyü** — Tam arama · min-max · bağımlılık · bütçe duyarlılığı
- **Şube yatırım portföyü** — Tam arama · min-max · bağımlılık · bütçe duyarlılığı
- **Kampanya portföyü dayanıklılığı** — Tam arama · min-max · bağımlılık · bütçe duyarlılığı
- **Analist eğitim kapasitesi dağılımı** — Tam arama · min-max · bağımlılık · bütçe duyarlılığı
- **Gözlemlenebilirlik yatırımı seçimi** — Tam arama · min-max · bağımlılık · bütçe duyarlılığı
- **Tahsilat aksiyonu kapasite seçimi** — Tam arama · min-max · bağımlılık · bütçe duyarlılığı
- **Ürün keşif araştırmaları seçimi** — Tam arama · min-max · bağımlılık · bütçe duyarlılığı
- **API çağrı hacmi ileri dönem testi** — İleri dönem · kayan başlangıç · baz çizgi · WAPE
- **Fatura hacmi takvim tahmini** — İleri dönem · kayan başlangıç · baz çizgi · WAPE
- **Sipariş geliş hacmi tahmini** — İleri dönem · kayan başlangıç · baz çizgi · WAPE
- **Destek talebi hacim tahmini** — İleri dönem · kayan başlangıç · baz çizgi · WAPE
- **İade hacmi dönem dışı testi** — İleri dönem · kayan başlangıç · baz çizgi · WAPE
- **Depo toplama yükü tahmini** — İleri dönem · kayan başlangıç · baz çizgi · WAPE
- **QR menü istek hacmi tahmini** — İleri dönem · kayan başlangıç · baz çizgi · WAPE
- **Partner aktivasyon hacmi tahmini** — İleri dönem · kayan başlangıç · baz çizgi · WAPE
- **Sevkiyat adedi ileri dönem testi** — İleri dönem · kayan başlangıç · baz çizgi · WAPE
- **Excel aktarım işi yükü tahmini** — İleri dönem · kayan başlangıç · baz çizgi · WAPE
- **Ödeme işlem hacmi ileri dönem testi** — İleri dönem · kayan başlangıç · baz çizgi · WAPE
- **Kampanya siparişi tahmin sağlamlığı** — İleri dönem · kayan başlangıç · baz çizgi · WAPE
- **Dövizli mutabakat stres senaryosu** — Ortak şok · eşlenmiş senaryo · VaR / CVaR · prim duyarlılığı
- **Sağlayıcı kesintisi kayıp kuyruğu** — Ortak şok · eşlenmiş senaryo · VaR / CVaR · prim duyarlılığı
- **Tedarik gecikmesi marj riski** — Ortak şok · eşlenmiş senaryo · VaR / CVaR · prim duyarlılığı
- **İade dalgası marj dayanıklılığı** — Ortak şok · eşlenmiş senaryo · VaR / CVaR · prim duyarlılığı
- **Şüpheli ödeme inceleme kapasitesi** — Ortak şok · eşlenmiş senaryo · VaR / CVaR · prim duyarlılığı
- **Bulut maliyeti uç senaryo analizi** — Ortak şok · eşlenmiş senaryo · VaR / CVaR · prim duyarlılığı
- **Stok yokluğu kayıp stres testi** — Ortak şok · eşlenmiş senaryo · VaR / CVaR · prim duyarlılığı
- **Kampanya marjı uç kayıp analizi** — Ortak şok · eşlenmiş senaryo · VaR / CVaR · prim duyarlılığı
- **Alacak gecikmesi nakit stres testi** — Ortak şok · eşlenmiş senaryo · VaR / CVaR · prim duyarlılığı
- **Sürüm olay maliyeti stres testi** — Ortak şok · eşlenmiş senaryo · VaR / CVaR · prim duyarlılığı
- **Depo kesintisi operasyon riski** — Ortak şok · eşlenmiş senaryo · VaR / CVaR · prim duyarlılığı
- **Partner kaybı gelir stres testi** — Ortak şok · eşlenmiş senaryo · VaR / CVaR · prim duyarlılığı

## 20 ileri seviye GitHub projesi

[Proje kataloğu](https://olcayto-akbudak.github.io/projeler.html) arama, konu filtresi, yöntem, örnek sonuç ve kaynak bağlantıları sunar. İlk 10 proje ayrı açık GitHub deposunda, diğer 10 proje [github-labs koleksiyonunda](github-labs/README.md) okunabilir kaynak dosyaları ve bağımsız ZIP paketleriyle yer alır. GitHub'ın yeni depo oluşturma hız sınırı nedeniyle bu yerleşim kullanılmıştır.

Toplam 160 alan testi ve 20 sentetik demo yerel ortamda doğrulandı. Ayrı depoların her birinde ve koleksiyonda Linux/Windows, Python 3.12/3.13 CI tanımı vardır. SQLite transaction sonrasında bağlantılar deterministik kapanır; Windows dosya kilidi regresyonu test başlangıçlarında kontrol edilir.

[Tüm kaynakları indir](github-projeleri-20.zip). Örnekler sentetiktir; üretim hizmeti veya gerçek kurum sonucu olarak sunulmaz.

