# Çalıştırılmış kabul sonuçları

Python 3.12.14, sentetik `entity_resolution_workbench_scenario.json`; yerel test sayısı **8**, tümü başarılı. Ham test günlüğü `test-log.txt`.

Kümeler [['A', 'B'], ['C']]; 2 vergi kimliği çatışması reddedildi.

Sonuçlar yalnız bu örneğe aittir; üretim doğruluğu veya performans garantisi olarak yorumlanmamalıdır. Ölçülen iş sonucunu kontrol edin; örnek negatif vaka içeriyorsa ret beklenir. Tam çıktı `entity_resolution_workbench_sample-report.json`.

## Sınanan davranışlar

| Test | Kontrol |
|---|---|
| `test_tax_conflict` | tax conflict |
| `test_cluster_invariant` | cluster invariant |
| `test_normalize` | normalize |
| `test_country_block` | country block |
| `test_duplicate` | duplicate |
| `test_threshold` | threshold |
| `test_email_punctuation_preserved` | email punctuation preserved |
| `test_compatible_merge` | compatible merge |

## Gelişmiş deney planı

1. 100.000 kayıt için blocking recall ve candidate reduction oranlarını ölçün.
2. Transitif bağlarda vergi kimliği çatışmasını canlı inceleme kuyruğuna aktarın.
3. Adres ve telefon özelliklerine kalibre edilmiş skor ekleyin.
4. Label çiftleriyle precision/recall ölçün; örnek similarity değerini doğruluk sanmayın.
