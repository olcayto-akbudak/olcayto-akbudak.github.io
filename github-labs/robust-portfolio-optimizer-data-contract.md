# Girdi ve çıktı sözleşmesi

UTF-8 JSON nesnesi; örnek dosya alanların tam iç içe yapısını gösterir. Zamanlar bu laboratuvarda sayısal sanal zaman/gün değeridir; saat dilimi dönüşümü yapılmaz.

| Üst alan | Tür | Örnek |
|---|---|---|
| `budgets` | `dict` | {'money': 12, 'people': 8} |
| `items` | `list` | [{'id': 'A', 'costs': {'money': 4, 'people': 3}, 'values': [8, 6]}, {'id': 'B', 'costs': {'money': 5, 'people': 3}, 'values': [9, 10], 'requires': ['A']}, {'id' |

## Semantik

Değerler ve maliyetler negatif olamaz; en fazla 26 aday; hedef min(scenario totals).

Alan motorunun doğrulamaları `robust_portfolio_optimizer.py` içinde açıkça bulunur. Eksik zorunlu anahtarlar hata verir. Satır bazında karantina/bulgu üreten motorlar rapora yazar; yapısal konfigürasyon hataları işlemi keser. Tam JSON Schema dosyası bu sürümün kapsamında değildir.

## Çıktı

Gerçek çıktı şeması ve örnek değerler `robust_portfolio_optimizer_sample-report.json` içinde yer alır. Örnek işleme özgü sonuçlar `results.md` içinde açıklanır. Dış tüketici alan adlarını ve birimleri değiştirmeden sözleşmeyi sürümlemelidir.
