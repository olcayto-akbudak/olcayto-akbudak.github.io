# İşletim ve hata inceleme

1. `python --version` ile 3.12 veya daha yeni sürümü doğrulayın.
2. Depo kökünde testleri çalıştırın; başarısız test varken senaryoyu referans kabul etmeyin.
3. `sql_plan_regression_lab_scenario.json` dosyasının bir kopyasını değiştirin; referans örneği koruyun.
4. `python sql_plan_regression_lab.py demo --input <dosya> --output deney.json` çalıştırın.
5. Beklenen ret/inceleme ile beklenmeyen exception durumunu ayırın.
6. Çıktıyı `sql_plan_regression_lab_sample-report.json` ile karşılaştırın; sentetik negatif örnekleri otomatik başarıya çevirmeyin.

## Projeye özgü kontrol

Synthetic relational data → independent expected totals → SQL comparison → explain → median timings

Para tamsayı; iki ticket join fanout hatasını bilerek gösterir; sürelerden önce doğruluk değerlendirilir.

## Arıza çözümü

JSON parse hatasında girdi biçimini; eksik alan hatasında sözleşmeyi; kural ihlalinde alan bulgusunu; SQLite kilidinde eşzamanlı yazıcı sayısını inceleyin. Gerçek veriyi paylaşmadan önce anonimleştirin. Başarı iddiasını raporun gate/valid/fit/correct/state alanının ilgili semantiğiyle ilişkilendirin; sadece exit code yeterli değildir.

## Üretim açığı

SQLite yerel ölçümüdür; PostgreSQL planlarına veya gerçek üretim yüküne genellenmez.
