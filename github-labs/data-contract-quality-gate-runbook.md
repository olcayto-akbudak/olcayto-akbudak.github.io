# İşletim ve hata inceleme

1. `python --version` ile 3.12 veya daha yeni sürümü doğrulayın.
2. Depo kökünde testleri çalıştırın; başarısız test varken senaryoyu referans kabul etmeyin.
3. `data_contract_quality_gate_scenario.json` dosyasının bir kopyasını değiştirin; referans örneği koruyun.
4. `python data_contract_quality_gate.py demo --input <dosya> --output deney.json` çalıştırın.
5. Beklenen ret/inceleme ile beklenmeyen exception durumunu ayırın.
6. Çıktıyı `data_contract_quality_gate_sample-report.json` ile karşılaştırın; sentetik negatif örnekleri otomatik başarıya çevirmeyin.

## Projeye özgü kontrol

Row contract checks → duplicate/freshness → quarantine → release gate → PSI

Bilinmeyen alan REVIEW; geçersiz satır BLOCK; kabul edilen ve karantinadaki satırlar ayrılır.

## Arıza çözümü

JSON parse hatasında girdi biçimini; eksik alan hatasında sözleşmeyi; kural ihlalinde alan bulgusunu; SQLite kilidinde eşzamanlı yazıcı sayısını inceleyin. Gerçek veriyi paylaşmadan önce anonimleştirin. Başarı iddiasını raporun gate/valid/fit/correct/state alanının ilgili semantiğiyle ilişkilendirin; sadece exit code yeterli değildir.

## Üretim açığı

PSI kategorik histogram karşılaştırmasıdır; kendi başına istatistiksel anlamlılık testi değildir.
