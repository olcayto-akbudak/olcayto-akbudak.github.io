# SLA ve Çok Pencereli Burn Rate

**Depo adı:** `sla-error-budget-monitor` · Python 3.12+ · bağımsız çalışır · dış paket gerekmez.

Kısa süreli küçük örneklem sıçraması ile kalıcı hizmet bozulmasını ayırmak.

## Teknik kapsam

SLO, düşük hacim koruması, p95, hata bütçesi. Bu depo çalıştırılabilir bir mühendislik laboratuvarıdır. Ağ erişimi, özel hesap veya gerçek müşteri verisi gerektirmez. Örneklerde kasıtlı hatalar da bulunur; BLOCK, REVIEW veya false sonucu bazı senaryolarda beklenen davranıştır.

## Hızlı başlangıç

Depo kökünde:

```bash
python -m unittest -v
python sla_error_budget_monitor.py demo
python sla_error_budget_monitor.py demo --input sla_error_budget_monitor_scenario.json --output custom-report.json
```

`sla_error_budget_monitor_sample-report.json` gerçekten çalıştırılmış örnek çıktıdır. Yeniden çalıştırma sonucu `report.json` olur. Zamanlama ölçümleri hariç sabit seed ve girdiyle tekrarlanabilir. Kurulum için `pip install` gerekmez.

## Mimari ve kararlar

İşlem hattı: Time window selection → error rates → budget burn → minimum volume → combined page.

Temel varsayım: Pencereler now-window < at <= now; alarm tüm pencerelerde eşik aşılınca açılır.

Alan motoru ve komut satırı `sla_error_budget_monitor.py`, kabul senaryosu `sla_error_budget_monitor_scenario.json`, sınır ve hata testleri `test_sla_error_budget_monitor.py` içindedir. Yapılandırma veri sözleşmesi [data-contract.md](sla-error-budget-monitor-data-contract.md), ayrıntılı akış [architecture.md](sla-error-budget-monitor-architecture.md), işletim adımları [runbook.md](sla-error-budget-monitor-runbook.md) içinde açıklanır.

## Doğrulama ve değerlendirme

Testler yalnız örneğin çalışmasını kontrol etmez; projenin davranışına özgü kabul ve ret koşullarını sınar. Örnek senaryoda gözlenen sonuçlar [results.md](sla-error-budget-monitor-results.md) içinde kayıtlıdır. CI Python 3.12/3.13, Ubuntu/Windows için tanımlıdır; yerel doğrulama Python 3.12 üzerinde yapılmıştır. GitHub'da ilk push sonrasında CI ayrıca çalışmalıdır.

## Sınırlar ve üretime geçiş

Uzun dönem hata bütçesi ayrıca tutulmalıdır; remaining değeri son pencerenin bütçesidir.

Bu sürümde otomatik canlı entegrasyon, kullanıcı kimlik doğrulama, izleme altyapısı ve gerçek veriyle performans garantisi yoktur. İş kuralları sentetik kabul senaryolarıyla görünür hale getirilmiştir. Üretime geçmeden örnek sözleşmeyi gerçek alanlarla eşleyin, aşağıdaki deneyleri uygulayın ve sonuçları sürümleyin.

## Zorlaştırma deneyleri

1. 30 günlük SLO için rolling budget ledger ekleyin.
2. Availability ve latency SLI bütçelerini ayrı takip edin.
3. Tenant/region stratum ve minimum hacim korumasını birlikte raporlayın.
4. Eksik telemetriyi başarılı istek saymak yerine UNKNOWN olarak izleyin.

## GitHub'a taşıma

```bash
git init
git add .
git commit -m "Initial working analysis laboratory"
git branch -M main
git remote add origin https://github.com/olcayto-akbudak/sla-error-budget-monitor.git
git push -u origin main
```

Kendi hesabınıza taşırken `olcayto-akbudak` alanını değiştirin. Hesap bilgisi veya erişim anahtarı kaynak koda koymayın. Çalışan kaynak kod, testler ve teknik belgeler bu depoda yayımlanmıştır.

## Depo yerleşimi

GitHub sürümü dosyaları depo kökünde tutar; `sla_error_budget_monitor.py` alan motorunu ve CLI girişini içerir. `test_sla_error_budget_monitor.py` doğrudan bu modülü test eder. Belgeler ve örnek veriler aynı kökte yer alır.

## Ortak kaynak koleksiyonunda çalıştırma

Bu klasörde dosya adları çakışmaması için proje adıyla öneklenmiştir. Bağımsız ZIP asıl sade adlandırmayı korur.

```bash
python sla_error_budget_monitor.py demo
python -m unittest test_sla_error_budget_monitor -v
```
