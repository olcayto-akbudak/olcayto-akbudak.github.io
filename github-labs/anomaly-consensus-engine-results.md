# Çalıştırılmış kabul sonuçları

Python 3.12.14, sentetik `anomaly_consensus_engine_scenario.json`; yerel test sayısı **8**, tümü başarılı. Ham test günlüğü `test-log.txt`.

10 alarm; değerlendirme {'true_positive': 10, 'false_positive': 0, 'missed': 0}. Geçici EWMA etkisi nedeniyle shift sonrası false positive oluşabilir.

Sonuçlar yalnız bu örneğe aittir; üretim doğruluğu veya performans garantisi olarak yorumlanmamalıdır. Ölçülen iş sonucunu kontrol edin; örnek negatif vaka içeriyorsa ret beklenir. Tam çıktı `anomaly_consensus_engine_sample-report.json`.

## Sınanan davranışlar

| Test | Kontrol |
|---|---|
| `test_flat` | flat |
| `test_shift` | shift |
| `test_short` | short |
| `test_nonfinite` | nonfinite |
| `test_alpha` | alpha |
| `test_baseline_frozen` | baseline frozen |
| `test_seasonality_no_alarm` | seasonality no alarm |
| `test_period` | period |

## Gelişmiş deney planı

1. Bir günlük ani spike ile 20 günlük level shift için ayrı alarm metrikleri çıkarın.
2. Baseline kirlenmesini azaltan robust update tasarlayın.
3. Alarm eşiklerini validation bölümündeki yanlış alarm bütçesiyle seçin.
4. Birden fazla metrikte alarm korelasyonunu incident gruplarına dönüştürün.
