# Çalıştırılmış kabul sonuçları

Python 3.12.14, sentetik `robust_portfolio_optimizer_scenario.json`; yerel test sayısı **8**, tümü başarılı. Ham test günlüğü `test-log.txt`.

Seçilen ['A', 'B', 'D']; worst-case değer 21; senaryolar [21, 23]; maliyet {'money': 12, 'people': 8}; ziyaret 20.

Sonuçlar yalnız bu örneğe aittir; üretim doğruluğu veya performans garantisi olarak yorumlanmamalıdır. Ölçülen iş sonucunu kontrol edin; örnek negatif vaka içeriyorsa ret beklenir. Tam çıktı `robust_portfolio_optimizer_sample-report.json`.

## Sınanan davranışlar

| Test | Kontrol |
|---|---|
| `test_budget` | budget |
| `test_dependencies` | dependencies |
| `test_conflict` | conflict |
| `test_exact_bruteforce` | exact bruteforce |
| `test_negative` | negative |
| `test_empty` | empty |
| `test_nonfinite_value` | nonfinite value |
| `test_unknown_dependency` | unknown dependency |

## Gelişmiş deney planı

1. Rastgele küçük portföylerde brute-force oracle ile çözümü çapraz doğrulayın.
2. Bağımlılık döngülerini SCC ile önceden teşhis edin.
3. Bütçeyi yüzde 10 artırıp seçilen portföy ve worst-case değer duyarlılığını ölçün.
4. Büyük problemler için MILP adaptörü ve optimality gap raporu ekleyin.
