# Çalıştırılmış kabul sonuçları

Python 3.12.14, sentetik `data_contract_quality_gate_scenario.json`; yerel test sayısı **8**, tümü başarılı. Ham test günlüğü `test-log.txt`.

Gate REVIEW; kabul 1, karantina 2; PSI 0.5498.

Sonuçlar yalnız bu örneğe aittir; üretim doğruluğu veya performans garantisi olarak yorumlanmamalıdır. Ölçülen iş sonucunu kontrol edin; örnek negatif vaka içeriyorsa ret beklenir. Tam çıktı `data_contract_quality_gate_sample-report.json`.

## Sınanan davranışlar

| Test | Kontrol |
|---|---|
| `test_quarantine` | quarantine |
| `test_unknown_review` | unknown review |
| `test_psi_identity` | psi identity |
| `test_psi_shift` | psi shift |
| `test_future` | future |
| `test_bool_not_int` | bool not int |
| `test_partition_conservation` | partition conservation |
| `test_empty_histogram` | empty histogram |

## Gelişmiş deney planı

1. Birden fazla sütunda birleşik unique ve foreign key sözleşmesi ekleyin.
2. Karantinayı veri sürümü ve kural sürümüyle kalıcı depoya yazın.
3. PSI eşiklerini ayrı historical validation bölümlerinde seçin.
4. Schema drift için alan ekleme ile type değiştirme politikalarını ayrıştırın.
