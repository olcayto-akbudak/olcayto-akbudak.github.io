# Çalıştırılmış kabul sonuçları

Python 3.12.14, sentetik `sla_error_budget_monitor_scenario.json`; yerel test sayısı **8**, tümü başarılı. Ham test günlüğü `test-log.txt`.

Alarm True; pencere ölçümleri [{'window_seconds': 300, 'requests': 29, 'errors': 5, 'burn_rate': 17.241379310344815, 'p95_ms': 128, 'eligible': True}, {'window_seconds': 3600, 'requests': 359, 'errors': 71, 'burn_rate': 19.77715877437324, 'p95_ms': 128, 'eligible': True}]

Sonuçlar yalnız bu örneğe aittir; üretim doğruluğu veya performans garantisi olarak yorumlanmamalıdır. Ölçülen iş sonucunu kontrol edin; örnek negatif vaka içeriyorsa ret beklenir. Tam çıktı `sla_error_budget_monitor_sample-report.json`.

## Sınanan davranışlar

| Test | Kontrol |
|---|---|
| `test_volume_guard` | volume guard |
| `test_sustained` | sustained |
| `test_future_excluded` | future excluded |
| `test_boundary` | boundary |
| `test_good` | good |
| `test_slo` | slo |
| `test_nonfinite_latency` | nonfinite latency |
| `test_p95` | p95 |

## Gelişmiş deney planı

1. 30 günlük SLO için rolling budget ledger ekleyin.
2. Availability ve latency SLI bütçelerini ayrı takip edin.
3. Tenant/region stratum ve minimum hacim korumasını birlikte raporlayın.
4. Eksik telemetriyi başarılı istek saymak yerine UNKNOWN olarak izleyin.
