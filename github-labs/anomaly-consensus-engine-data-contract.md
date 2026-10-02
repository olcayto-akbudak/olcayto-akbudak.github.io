# Girdi ve çıktı sözleşmesi

UTF-8 JSON nesnesi; örnek dosya alanların tam iç içe yapısını gösterir. Zamanlar bu laboratuvarda sayısal sanal zaman/gün değeridir; saat dilimi dönüşümü yapılmaz.

| Üst alan | Tür | Örnek |
|---|---|---|
| `values` | `list` | [99, 104, 105, 110, 111, 116, 117, 101, 102, 107, 108, 113, 114, 119, 99, 104, 105, 110, 111, 116, 117, 101, 102, 107, 108, 113, 114, 119, 99, 104, 105, 110, 11 |
| `anomaly_indices` | `list` | [65, 66, 67, 68, 69, 70, 71, 72, 73, 74] |

## Semantik

Baseline warmup boyunca oluşur; izleme sırasında otomatik güncellenmez.

Alan motorunun doğrulamaları `anomaly_consensus_engine.py` içinde açıkça bulunur. Eksik zorunlu anahtarlar hata verir. Satır bazında karantina/bulgu üreten motorlar rapora yazar; yapısal konfigürasyon hataları işlemi keser. Tam JSON Schema dosyası bu sürümün kapsamında değildir.

## Çıktı

Gerçek çıktı şeması ve örnek değerler `anomaly_consensus_engine_sample-report.json` içinde yer alır. Örnek işleme özgü sonuçlar `results.md` içinde açıklanır. Dış tüketici alan adlarını ve birimleri değiştirmeden sözleşmeyi sürümlemelidir.
