# Girdi ve çıktı sözleşmesi

UTF-8 JSON nesnesi; örnek dosya alanların tam iç içe yapısını gösterir. Zamanlar bu laboratuvarda sayısal sanal zaman/gün değeridir; saat dilimi dönüşümü yapılmaz.

| Üst alan | Tür | Örnek |
|---|---|---|
| `workers` | `int` | 2 |
| `tasks` | `list` | [{'id': 'auth', 'duration': 2, 'expected': 200, 'actual': 200}, {'id': 'create', 'duration': 3, 'depends': ['auth'], 'expected': 201, 'actual': 201, 'fail_first |

## Semantik

Retry yalnız idempotent veya idempotency_key içeren görevlerde açılır.

Alan motorunun doğrulamaları `integration_test_orchestrator.py` içinde açıkça bulunur. Eksik zorunlu anahtarlar hata verir. Satır bazında karantina/bulgu üreten motorlar rapora yazar; yapısal konfigürasyon hataları işlemi keser. Tam JSON Schema dosyası bu sürümün kapsamında değildir.

## Çıktı

Gerçek çıktı şeması ve örnek değerler `integration_test_orchestrator_sample-report.json` içinde yer alır. Örnek işleme özgü sonuçlar `results.md` içinde açıklanır. Dış tüketici alan adlarını ve birimleri değiştirmeden sözleşmeyi sürümlemelidir.
