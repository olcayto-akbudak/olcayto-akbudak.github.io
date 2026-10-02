# Girdi ve çıktı sözleşmesi

UTF-8 JSON nesnesi; örnek dosya alanların tam iç içe yapısını gösterir. Zamanlar bu laboratuvarda sayısal sanal zaman/gün değeridir; saat dilimi dönüşümü yapılmaz.

| Üst alan | Tür | Örnek |
|---|---|---|
| `now` | `int` | 4000 |
| `windows` | `list` | [300, 3600] |
| `minimum` | `int` | 20 |
| `events` | `list` | [{'at': 100, 'ok': False, 'latency_ms': 100}, {'at': 110, 'ok': True, 'latency_ms': 101}, {'at': 120, 'ok': True, 'latency_ms': 102}, {'at': 130, 'ok': True, 'l |

## Semantik

Pencereler now-window < at <= now; alarm tüm pencerelerde eşik aşılınca açılır.

Alan motorunun doğrulamaları `sla_error_budget_monitor.py` içinde açıkça bulunur. Eksik zorunlu anahtarlar hata verir. Satır bazında karantina/bulgu üreten motorlar rapora yazar; yapısal konfigürasyon hataları işlemi keser. Tam JSON Schema dosyası bu sürümün kapsamında değildir.

## Çıktı

Gerçek çıktı şeması ve örnek değerler `sla_error_budget_monitor_sample-report.json` içinde yer alır. Örnek işleme özgü sonuçlar `results.md` içinde açıklanır. Dış tüketici alan adlarını ve birimleri değiştirmeden sözleşmeyi sürümlemelidir.
