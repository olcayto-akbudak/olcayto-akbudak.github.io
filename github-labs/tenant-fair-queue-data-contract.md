# Girdi ve çıktı sözleşmesi

UTF-8 JSON nesnesi; örnek dosya alanların tam iç içe yapısını gösterir. Zamanlar bu laboratuvarda sayısal sanal zaman/gün değeridir; saat dilimi dönüşümü yapılmaz.

| Üst alan | Tür | Örnek |
|---|---|---|
| `tenants` | `dict` | {'gold': 3, 'standard': 1} |
| `jobs` | `list` | [{'id': 'G0', 'tenant': 'gold', 'cost': 3}, {'id': 'G1', 'tenant': 'gold', 'cost': 4}, {'id': 'G2', 'tenant': 'gold', 'cost': 5}, {'id': 'G3', 'tenant': 'gold', |

## Semantik

Tüm işler başlangıçta hazırdır; adalet tamamlanan maliyet üzerinden ölçülür.

Alan motorunun doğrulamaları `tenant_fair_queue.py` içinde açıkça bulunur. Eksik zorunlu anahtarlar hata verir. Satır bazında karantina/bulgu üreten motorlar rapora yazar; yapısal konfigürasyon hataları işlemi keser. Tam JSON Schema dosyası bu sürümün kapsamında değildir.

## Çıktı

Gerçek çıktı şeması ve örnek değerler `tenant_fair_queue_sample-report.json` içinde yer alır. Örnek işleme özgü sonuçlar `results.md` içinde açıklanır. Dış tüketici alan adlarını ve birimleri değiştirmeden sözleşmeyi sürümlemelidir.
