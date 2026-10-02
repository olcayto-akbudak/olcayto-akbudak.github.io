# İşletim ve hata inceleme

1. `python --version` ile 3.12 veya daha yeni sürümü doğrulayın.
2. Depo kökünde testleri çalıştırın; başarısız test varken senaryoyu referans kabul etmeyin.
3. `order_saga_recovery_scenario.json` dosyasının bir kopyasını değiştirin; referans örneği koruyun.
4. `python order_saga_recovery.py demo --input <dosya> --output deney.json` çalıştırın.
5. Beklenen ret/inceleme ile beklenmeyen exception durumunu ayırın.
6. Çıktıyı `order_saga_recovery_sample-report.json` ile karşılaştırın; sentetik negatif örnekleri otomatik başarıya çevirmeyin.

## Projeye özgü kontrol

Inventory → payment → shipping → completion; failure → compensation/manual

Katılımcılar order+step anahtarlı kalıcı yerel mock; kargo gerçekleşmişse manuel inceleme gerekir.

## Arıza çözümü

JSON parse hatasında girdi biçimini; eksik alan hatasında sözleşmeyi; kural ihlalinde alan bulgusunu; SQLite kilidinde eşzamanlı yazıcı sayısını inceleyin. Gerçek veriyi paylaşmadan önce anonimleştirin. Başarı iddiasını raporun gate/valid/fit/correct/state alanının ilgili semantiğiyle ilişkilendirin; sadece exit code yeterli değildir.

## Üretim açığı

Gerçek dağıtık transaction yoktur; remote katılımcı idempotency ve outbox gereklidir.
