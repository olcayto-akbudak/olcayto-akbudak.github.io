# SQL Doğruluk ve Plan Regresyonu

**Depo adı:** `sql-plan-regression-lab` · Python 3.12+ · bağımsız çalışır · dış paket gerekmez.

Daha hızlı görünen SQL değişikliğinin tutarları katlamasını sonuç doğruluğuyla yakalamak.

## Teknik kapsam

Preaggregation, join fanout, digest, query plan. Bu depo çalıştırılabilir bir mühendislik laboratuvarıdır. Ağ erişimi, özel hesap veya gerçek müşteri verisi gerektirmez. Örneklerde kasıtlı hatalar da bulunur; BLOCK, REVIEW veya false sonucu bazı senaryolarda beklenen davranıştır.

## Hızlı başlangıç

Depo kökünde:

```bash
python -m unittest -v
python sql_plan_regression_lab.py demo
python sql_plan_regression_lab.py demo --input sql_plan_regression_lab_scenario.json --output custom-report.json
```

`sql_plan_regression_lab_sample-report.json` gerçekten çalıştırılmış örnek çıktıdır. Yeniden çalıştırma sonucu `report.json` olur. Zamanlama ölçümleri hariç sabit seed ve girdiyle tekrarlanabilir. Kurulum için `pip install` gerekmez.

## Mimari ve kararlar

İşlem hattı: Synthetic relational data → independent expected totals → SQL comparison → explain → median timings.

Temel varsayım: Para tamsayı; iki ticket join fanout hatasını bilerek gösterir; sürelerden önce doğruluk değerlendirilir.

Alan motoru ve komut satırı `sql_plan_regression_lab.py`, kabul senaryosu `sql_plan_regression_lab_scenario.json`, sınır ve hata testleri `test_sql_plan_regression_lab.py` içindedir. Yapılandırma veri sözleşmesi [data-contract.md](sql-plan-regression-lab-data-contract.md), ayrıntılı akış [architecture.md](sql-plan-regression-lab-architecture.md), işletim adımları [runbook.md](sql-plan-regression-lab-runbook.md) içinde açıklanır.

## Doğrulama ve değerlendirme

Testler yalnız örneğin çalışmasını kontrol etmez; projenin davranışına özgü kabul ve ret koşullarını sınar. Örnek senaryoda gözlenen sonuçlar [results.md](sql-plan-regression-lab-results.md) içinde kayıtlıdır. CI Python 3.12/3.13, Ubuntu/Windows için tanımlıdır; yerel doğrulama Python 3.12 üzerinde yapılmıştır. GitHub'da ilk push sonrasında CI ayrıca çalışmalıdır.

## Sınırlar ve üretime geçiş

SQLite yerel ölçümüdür; PostgreSQL planlarına veya gerçek üretim yüküne genellenmez.

Bu sürümde otomatik canlı entegrasyon, kullanıcı kimlik doğrulama, izleme altyapısı ve gerçek veriyle performans garantisi yoktur. İş kuralları sentetik kabul senaryolarıyla görünür hale getirilmiştir. Üretime geçmeden örnek sözleşmeyi gerçek alanlarla eşleyin, aşağıdaki deneyleri uygulayın ve sonuçları sürümleyin.

## Zorlaştırma deneyleri

1. İndeksli/indekssiz planları farklı veri seçiciliklerinde ölçün.
2. Yanlış fanout sorgusunu preaggregation ile düzeltip oracle ile karşılaştırın.
3. NULL, sıfır sipariş ve yinelenen satır fixturelarını genişletin.
4. PostgreSQL EXPLAIN ANALYZE adaptöründe warm/cold cache sonuçlarını ayrı tutun.

## GitHub'a taşıma

```bash
git init
git add .
git commit -m "Initial working analysis laboratory"
git branch -M main
git remote add origin https://github.com/olcayto-akbudak/sql-plan-regression-lab.git
git push -u origin main
```

Kendi hesabınıza taşırken `olcayto-akbudak` alanını değiştirin. Hesap bilgisi veya erişim anahtarı kaynak koda koymayın. Çalışan kaynak kod, testler ve teknik belgeler bu depoda yayımlanmıştır.

## Depo yerleşimi

GitHub sürümü dosyaları depo kökünde tutar; `sql_plan_regression_lab.py` alan motorunu ve CLI girişini içerir. `test_sql_plan_regression_lab.py` doğrudan bu modülü test eder. Belgeler ve örnek veriler aynı kökte yer alır.

## Ortak kaynak koleksiyonunda çalıştırma

Bu klasörde dosya adları çakışmaması için proje adıyla öneklenmiştir. Bağımsız ZIP asıl sade adlandırmayı korur.

```bash
python sql_plan_regression_lab.py demo
python -m unittest test_sql_plan_regression_lab -v
```
