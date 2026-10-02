# Girdi ve çıktı sözleşmesi

UTF-8 JSON nesnesi; örnek dosya alanların tam iç içe yapısını gösterir. Zamanlar bu laboratuvarda sayısal sanal zaman/gün değeridir; saat dilimi dönüşümü yapılmaz.

| Üst alan | Tür | Örnek |
|---|---|---|
| `nodes` | `list` | [{'id': 'R1', 'kind': 'requirement', 'risk': 5, 'revision': 2}, {'id': 'R2', 'kind': 'requirement', 'risk': 2, 'revision': 1}, {'id': 'B1', 'kind': 'rule'}, {'i |
| `edges` | `list` | [['R1', 'B1'], ['B1', 'T1'], ['R2', 'T2']] |
| `changed` | `list` | ['B1'] |

## Semantik

Her gereksinimden erişilebilen güncel başarılı test kapsama sayılır.

Alan motorunun doğrulamaları `requirements_traceability_graph.py` içinde açıkça bulunur. Eksik zorunlu anahtarlar hata verir. Satır bazında karantina/bulgu üreten motorlar rapora yazar; yapısal konfigürasyon hataları işlemi keser. Tam JSON Schema dosyası bu sürümün kapsamında değildir.

## Çıktı

Gerçek çıktı şeması ve örnek değerler `requirements_traceability_graph_sample-report.json` içinde yer alır. Örnek işleme özgü sonuçlar `results.md` içinde açıklanır. Dış tüketici alan adlarını ve birimleri değiştirmeden sözleşmeyi sürümlemelidir.
