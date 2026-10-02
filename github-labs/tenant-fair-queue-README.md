# Tenant Adil Kuyruk Motoru

**Depo adı:** `tenant-fair-queue` · Python 3.12+ · bağımsız çalışır · dış paket gerekmez.

Bir tenantın pahalı işlerinin diğerlerinin kuyruğunu tek başına tüketmesini önlemek.

## Teknik kapsam

Weighted deficit round robin, değişken maliyet. Bu depo çalıştırılabilir bir mühendislik laboratuvarıdır. Ağ erişimi, özel hesap veya gerçek müşteri verisi gerektirmez. Örneklerde kasıtlı hatalar da bulunur; BLOCK, REVIEW veya false sonucu bazı senaryolarda beklenen davranıştır.

## Hızlı başlangıç

Depo kökünde:

```bash
python -m unittest -v
python tenant_fair_queue.py demo
python tenant_fair_queue.py demo --input tenant_fair_queue_scenario.json --output custom-report.json
```

`tenant_fair_queue_sample-report.json` gerçekten çalıştırılmış örnek çıktıdır. Yeniden çalıştırma sonucu `report.json` olur. Zamanlama ölçümleri hariç sabit seed ve girdiyle tekrarlanabilir. Kurulum için `pip install` gerekmez.

## Mimari ve kararlar

İşlem hattı: Tenant queues → quantum credit → non-preemptive dispatch → weighted service report.

Temel varsayım: Tüm işler başlangıçta hazırdır; adalet tamamlanan maliyet üzerinden ölçülür.

Alan motoru ve komut satırı `tenant_fair_queue.py`, kabul senaryosu `tenant_fair_queue_scenario.json`, sınır ve hata testleri `test_tenant_fair_queue.py` içindedir. Yapılandırma veri sözleşmesi [data-contract.md](tenant-fair-queue-data-contract.md), ayrıntılı akış [architecture.md](tenant-fair-queue-architecture.md), işletim adımları [runbook.md](tenant-fair-queue-runbook.md) içinde açıklanır.

## Doğrulama ve değerlendirme

Testler yalnız örneğin çalışmasını kontrol etmez; projenin davranışına özgü kabul ve ret koşullarını sınar. Örnek senaryoda gözlenen sonuçlar [results.md](tenant-fair-queue-results.md) içinde kayıtlıdır. CI Python 3.12/3.13, Ubuntu/Windows için tanımlıdır; yerel doğrulama Python 3.12 üzerinde yapılmıştır. GitHub'da ilk push sonrasında CI ayrıca çalışmalıdır.

## Sınırlar ve üretime geçiş

Canlı varış, öncelik yaşlandırma ve tenant rate cap bu sürümde bulunmaz.

Bu sürümde otomatik canlı entegrasyon, kullanıcı kimlik doğrulama, izleme altyapısı ve gerçek veriyle performans garantisi yoktur. İş kuralları sentetik kabul senaryolarıyla görünür hale getirilmiştir. Üretime geçmeden örnek sözleşmeyi gerçek alanlarla eşleyin, aşağıdaki deneyleri uygulayın ve sonuçları sürümleyin.

## Zorlaştırma deneyleri

1. Canlı geliş zamanları ve tenant maksimum eşzamanlı iş sınırı ekleyin.
2. DRR ile FIFO politikasını aynı değişken iş maliyetlerinde kıyaslayın.
3. Uzun işlerin head-of-line beklemesini per-tenant p95 ile ölçün.
4. Öncelik yaşlandırması eklerken ağırlıklı hizmet garantisini yeniden sınayın.

## GitHub'a taşıma

```bash
git init
git add .
git commit -m "Initial working analysis laboratory"
git branch -M main
git remote add origin https://github.com/olcayto-akbudak/tenant-fair-queue.git
git push -u origin main
```

Kendi hesabınıza taşırken `olcayto-akbudak` alanını değiştirin. Hesap bilgisi veya erişim anahtarı kaynak koda koymayın. Çalışan kaynak kod, testler ve teknik belgeler bu depoda yayımlanmıştır.

## Depo yerleşimi

GitHub sürümü dosyaları depo kökünde tutar; `tenant_fair_queue.py` alan motorunu ve CLI girişini içerir. `test_tenant_fair_queue.py` doğrudan bu modülü test eder. Belgeler ve örnek veriler aynı kökte yer alır.

## Ortak kaynak koleksiyonunda çalıştırma

Bu klasörde dosya adları çakışmaması için proje adıyla öneklenmiştir. Bağımsız ZIP asıl sade adlandırmayı korur.

```bash
python tenant_fair_queue.py demo
python -m unittest test_tenant_fair_queue -v
```
