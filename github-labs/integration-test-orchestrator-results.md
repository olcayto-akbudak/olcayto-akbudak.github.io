# Çalıştırılmış kabul sonuçları

Python 3.12.14, sentetik `integration_test_orchestrator_scenario.json`; yerel test sayısı **8**, tümü başarılı. Ham test günlüğü `test-log.txt`.

Gate BLOCK; makespan 9; sonuçlar {'auth': {'status': 'passed', 'attempts': 1, 'finished': 2}, 'slow': {'status': 'timeout', 'attempts': 1, 'finished': 4}, 'after-slow': {'status': 'skipped', 'attempts': 0}, 'create': {'status': 'passed', 'attempts': 2, 'finished': 8}, 'read': {'status': 'passed', 'attempts': 1, 'finished': 9}}

Sonuçlar yalnız bu örneğe aittir; üretim doğruluğu veya performans garantisi olarak yorumlanmamalıdır. Ölçülen iş sonucunu kontrol edin; örnek negatif vaka içeriyorsa ret beklenir. Tam çıktı `integration_test_orchestrator_sample-report.json`.

## Sınanan davranışlar

| Test | Kontrol |
|---|---|
| `test_retry` | retry |
| `test_skip` | skip |
| `test_timeout` | timeout |
| `test_unsafe` | unsafe |
| `test_cycle` | cycle |
| `test_workers` | workers |
| `test_nonfinite_duration` | nonfinite duration |
| `test_serial_makespan` | serial makespan |

## Gelişmiş deney planı

1. HTTP adaptöründe retry safety sözleşmesini idempotency key ile doğrulayın.
2. Sanal scheduler çıktısından JUnit XML üretin.
3. Worker occupancy ve kritik yol süresini DAG üzerinde raporlayın.
4. Kısmi başarılı testlerin artifact bağımlılıklarını ayrıca modelleyin.
