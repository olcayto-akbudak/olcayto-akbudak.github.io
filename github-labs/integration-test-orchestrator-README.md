# Entegrasyon Test DAG Orkestratörü

**Depo adı:** `integration-test-orchestrator` · Python 3.12+ · bağımsız çalışır · dış paket gerekmez.

Başarısız ön koşuldan sonraki testleri atlamak ve tekrarın yan etkisini kontrol etmek.

## Teknik kapsam

Sanal scheduler, timeout, safe retry, bağımlılık. Bu depo çalıştırılabilir bir mühendislik laboratuvarıdır. Ağ erişimi, özel hesap veya gerçek müşteri verisi gerektirmez. Örneklerde kasıtlı hatalar da bulunur; BLOCK, REVIEW veya false sonucu bazı senaryolarda beklenen davranıştır.

## Hızlı başlangıç

Depo kökünde:

```bash
python -m unittest -v
python integration_test_orchestrator.py demo
python integration_test_orchestrator.py demo --input integration_test_orchestrator_scenario.json --output custom-report.json
```

`integration_test_orchestrator_sample-report.json` gerçekten çalıştırılmış örnek çıktıdır. Yeniden çalıştırma sonucu `report.json` olur. Zamanlama ölçümleri hariç sabit seed ve girdiyle tekrarlanabilir. Kurulum için `pip install` gerekmez.

## Mimari ve kararlar

İşlem hattı: DAG cycle check → bounded workers → attempt completion → retry/skip → gate.

Temel varsayım: Retry yalnız idempotent veya idempotency_key içeren görevlerde açılır.

Alan motoru ve komut satırı `integration_test_orchestrator.py`, kabul senaryosu `integration_test_orchestrator_scenario.json`, sınır ve hata testleri `test_integration_test_orchestrator.py` içindedir. Yapılandırma veri sözleşmesi [data-contract.md](integration-test-orchestrator-data-contract.md), ayrıntılı akış [architecture.md](integration-test-orchestrator-architecture.md), işletim adımları [runbook.md](integration-test-orchestrator-runbook.md) içinde açıklanır.

## Doğrulama ve değerlendirme

Testler yalnız örneğin çalışmasını kontrol etmez; projenin davranışına özgü kabul ve ret koşullarını sınar. Örnek senaryoda gözlenen sonuçlar [results.md](integration-test-orchestrator-results.md) içinde kayıtlıdır. CI Python 3.12/3.13, Ubuntu/Windows için tanımlıdır; yerel doğrulama Python 3.12 üzerinde yapılmıştır. GitHub'da ilk push sonrasında CI ayrıca çalışmalıdır.

## Sınırlar ve üretime geçiş

Yerel sanal görevlerdir; gerçek HTTP transport ve JUnit adaptörü bu sürümde yoktur.

Bu sürümde otomatik canlı entegrasyon, kullanıcı kimlik doğrulama, izleme altyapısı ve gerçek veriyle performans garantisi yoktur. İş kuralları sentetik kabul senaryolarıyla görünür hale getirilmiştir. Üretime geçmeden örnek sözleşmeyi gerçek alanlarla eşleyin, aşağıdaki deneyleri uygulayın ve sonuçları sürümleyin.

## Zorlaştırma deneyleri

1. HTTP adaptöründe retry safety sözleşmesini idempotency key ile doğrulayın.
2. Sanal scheduler çıktısından JUnit XML üretin.
3. Worker occupancy ve kritik yol süresini DAG üzerinde raporlayın.
4. Kısmi başarılı testlerin artifact bağımlılıklarını ayrıca modelleyin.

## GitHub'a taşıma

```bash
git init
git add .
git commit -m "Initial working analysis laboratory"
git branch -M main
git remote add origin https://github.com/olcayto-akbudak/integration-test-orchestrator.git
git push -u origin main
```

Kendi hesabınıza taşırken `olcayto-akbudak` alanını değiştirin. Hesap bilgisi veya erişim anahtarı kaynak koda koymayın. Çalışan kaynak kod, testler ve teknik belgeler bu depoda yayımlanmıştır.

## Depo yerleşimi

GitHub sürümü dosyaları depo kökünde tutar; `integration_test_orchestrator.py` alan motorunu ve CLI girişini içerir. `test_integration_test_orchestrator.py` doğrudan bu modülü test eder. Belgeler ve örnek veriler aynı kökte yer alır.

## Ortak kaynak koleksiyonunda çalıştırma

Bu klasörde dosya adları çakışmaması için proje adıyla öneklenmiştir. Bağımsız ZIP asıl sade adlandırmayı korur.

```bash
python integration_test_orchestrator.py demo
python -m unittest test_integration_test_orchestrator -v
```
