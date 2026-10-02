# Çalıştırılmış kabul sonuçları

Python 3.12.14, sentetik `requirements_traceability_graph_scenario.json`; yerel test sayısı **8**, tümü başarılı. Ham test günlüğü `test-log.txt`.

Risk ağırlıklı kapsama %71.43; gate BLOCK; etki ['B1', 'T1'].

Sonuçlar yalnız bu örneğe aittir; üretim doğruluğu veya performans garantisi olarak yorumlanmamalıdır. Ölçülen iş sonucunu kontrol edin; örnek negatif vaka içeriyorsa ret beklenir. Tam çıktı `requirements_traceability_graph_sample-report.json`.

## Sınanan davranışlar

| Test | Kontrol |
|---|---|
| `test_stale_gate` | stale gate |
| `test_weight` | weight |
| `test_impact` | impact |
| `test_cycle` | cycle |
| `test_dangling` | dangling |
| `test_duplicate` | duplicate |
| `test_current_evidence_pass` | current evidence pass |
| `test_unknown_change` | unknown change |

## Gelişmiş deney planı

1. Tek testin birden fazla gereksinimi kapsaması için evidence provenance ekleyin.
2. Kritik gereksinim için tüm zorunlu testlerin geçmesi politikasını ekleyin.
3. Revision yerine kaynak içerik hash freshness kullanın.
4. Değişiklik etkisini upstream/downstream ayrı raporlayın.
