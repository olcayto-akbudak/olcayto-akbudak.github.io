# Girdi ve çıktı sözleşmesi

UTF-8 JSON nesnesi; örnek dosya alanların tam iç içe yapısını gösterir. Zamanlar bu laboratuvarda sayısal sanal zaman/gün değeridir; saat dilimi dönüşümü yapılmaz.

| Üst alan | Tür | Örnek |
|---|---|---|
| `now` | `int` | 100 |
| `contract` | `dict` | {'unique': 'id', 'freshness': {'field': 'at', 'max_age': 20}, 'fields': {'id': {'type': 'string'}, 'amount': {'type': 'integer', 'min': 0}, 'at': {'type': 'inte |
| `rows` | `list` | [{'id': 'A', 'amount': 100, 'at': 90}, {'id': 'A', 'amount': -1, 'at': 20}, {'id': 'B', 'amount': 200, 'at': 95, 'extra': 'drift'}] |
| `baseline_histogram` | `list` | [50, 30, 20] |
| `current_histogram` | `list` | [20, 30, 50] |

## Semantik

Bilinmeyen alan REVIEW; geçersiz satır BLOCK; kabul edilen ve karantinadaki satırlar ayrılır.

Alan motorunun doğrulamaları `data_contract_quality_gate.py` içinde açıkça bulunur. Eksik zorunlu anahtarlar hata verir. Satır bazında karantina/bulgu üreten motorlar rapora yazar; yapısal konfigürasyon hataları işlemi keser. Tam JSON Schema dosyası bu sürümün kapsamında değildir.

## Çıktı

Gerçek çıktı şeması ve örnek değerler `data_contract_quality_gate_sample-report.json` içinde yer alır. Örnek işleme özgü sonuçlar `results.md` içinde açıklanır. Dış tüketici alan adlarını ve birimleri değiştirmeden sözleşmeyi sürümlemelidir.
