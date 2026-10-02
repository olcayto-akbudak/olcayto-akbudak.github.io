# Çalıştırılmış kabul sonuçları

Python 3.12.14, sentetik `order_saga_recovery_scenario.json`; yerel test sayısı **8**, tümü başarılı. Ham test günlüğü `test-log.txt`.

O1: COMPLETED, etkiler {'inventory': 1, 'payment': 1, 'shipping': 1}; O2: COMPENSATED, etkiler {'inventory': 0, 'payment': 0}

Sonuçlar yalnız bu örneğe aittir; üretim doğruluğu veya performans garantisi olarak yorumlanmamalıdır. Ölçülen iş sonucunu kontrol edin; örnek negatif vaka içeriyorsa ret beklenir. Tam çıktı `order_saga_recovery_sample-report.json`.

## Sınanan davranışlar

| Test | Kontrol |
|---|---|
| `test_complete` | complete |
| `test_resume` | resume |
| `test_compensate` | compensate |
| `test_idempotency` | idempotency |
| `test_irreversible` | irreversible |
| `test_empty_id` | empty id |
| `test_compensation_idempotent` | compensation idempotent |
| `test_shipping_crash_recovery` | shipping crash recovery |

## Gelişmiş deney planı

1. Katılımcıları ayrı veritabanı veya HTTP servisine taşıyın.
2. Koordinatör checkpointinden önce/sonra her adımda çökme enjekte edin.
3. Telafi başarısızlığı için kalıcı compensation retry kuyruğu ekleyin.
4. Kargo geri alınamıyorsa manuel kararın kimlik ve gerekçesini audit kaydına bağlayın.
