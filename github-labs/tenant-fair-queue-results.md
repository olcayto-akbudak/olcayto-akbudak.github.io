# Çalıştırılmış kabul sonuçları

Python 3.12.14, sentetik `tenant_fair_queue_scenario.json`; yerel test sayısı **8**, tümü başarılı. Ham test günlüğü `test-log.txt`.

Toplam hizmet {'gold': 54, 'standard': 36}; makespan 90; normalize Jain 0.9000. Sonlu kuyruklar sonsuz backlog adalet ispatı değildir.

Sonuçlar yalnız bu örneğe aittir; üretim doğruluğu veya performans garantisi olarak yorumlanmamalıdır. Ölçülen iş sonucunu kontrol edin; örnek negatif vaka içeriyorsa ret beklenir. Tam çıktı `tenant_fair_queue_sample-report.json`.

## Sınanan davranışlar

| Test | Kontrol |
|---|---|
| `test_exact_once` | exact once |
| `test_cost_conservation` | cost conservation |
| `test_big_job` | big job |
| `test_weight_order` | weight order |
| `test_unknown` | unknown |
| `test_bad_weight` | bad weight |
| `test_duplicate_jobs` | duplicate jobs |
| `test_nonfinite_weight` | nonfinite weight |

## Gelişmiş deney planı

1. Canlı geliş zamanları ve tenant maksimum eşzamanlı iş sınırı ekleyin.
2. DRR ile FIFO politikasını aynı değişken iş maliyetlerinde kıyaslayın.
3. Uzun işlerin head-of-line beklemesini per-tenant p95 ile ölçün.
4. Öncelik yaşlandırması eklerken ağırlıklı hizmet garantisini yeniden sınayın.
