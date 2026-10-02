# Çalıştırılmış kabul sonuçları

Python 3.12.14, sentetik `sql_plan_regression_lab_scenario.json`; yerel test sayısı **8**, tümü başarılı. Ham test günlüğü `test-log.txt`.

correlated: doğruluk True, medyan 0.225 ms; preaggregate: doğruluk True, medyan 0.281 ms; fanout_bug: doğruluk False, medyan 0.493 ms

Sonuçlar yalnız bu örneğe aittir; üretim doğruluğu veya performans garantisi olarak yorumlanmamalıdır. Ölçülen iş sonucunu kontrol edin; örnek negatif vaka içeriyorsa ret beklenir. Tam çıktı `sql_plan_regression_lab_sample-report.json`.

## Sınanan davranışlar

| Test | Kontrol |
|---|---|
| `test_equivalence` | equivalence |
| `test_fanout_detected` | fanout detected |
| `test_independent_expected` | independent expected |
| `test_index_plan` | index plan |
| `test_noindex_correct` | noindex correct |
| `test_bad_dimension` | bad dimension |
| `test_digest_change` | digest change |
| `test_plan_available` | plan available |

## Gelişmiş deney planı

1. İndeksli/indekssiz planları farklı veri seçiciliklerinde ölçün.
2. Yanlış fanout sorgusunu preaggregation ile düzeltip oracle ile karşılaştırın.
3. NULL, sıfır sipariş ve yinelenen satır fixturelarını genişletin.
4. PostgreSQL EXPLAIN ANALYZE adaptöründe warm/cold cache sonuçlarını ayrı tutun.
