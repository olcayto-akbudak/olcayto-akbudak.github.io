# Mevsimsel Anomali Konsensüsü

**Depo adı:** `anomaly-consensus-engine` · Python 3.12+ · bağımsız çalışır · dış paket gerekmez.

Haftalık dalgalanmayı gerçek işlem hatası gibi işaretlemeden kalıcı sapmaları saptamak.

## Teknik kapsam

Median/MAD, EWMA, ardışık alarm oyları. Bu depo çalıştırılabilir bir mühendislik laboratuvarıdır. Ağ erişimi, özel hesap veya gerçek müşteri verisi gerektirmez. Örneklerde kasıtlı hatalar da bulunur; BLOCK, REVIEW veya false sonucu bazı senaryolarda beklenen davranıştır.

## Hızlı başlangıç

Depo kökünde:

```bash
python -m unittest -v
python anomaly_consensus_engine.py demo
python anomaly_consensus_engine.py demo --input anomaly_consensus_engine_scenario.json --output custom-report.json
```

`anomaly_consensus_engine_sample-report.json` gerçekten çalıştırılmış örnek çıktıdır. Yeniden çalıştırma sonucu `report.json` olur. Zamanlama ölçümleri hariç sabit seed ve girdiyle tekrarlanabilir. Kurulum için `pip install` gerekmez.

## Mimari ve kararlar

İşlem hattı: Frozen seasonal baseline → robust residual → EWMA → 2-of-3 vote.

Temel varsayım: Baseline warmup boyunca oluşur; izleme sırasında otomatik güncellenmez.

Alan motoru ve komut satırı `anomaly_consensus_engine.py`, kabul senaryosu `anomaly_consensus_engine_scenario.json`, sınır ve hata testleri `test_anomaly_consensus_engine.py` içindedir. Yapılandırma veri sözleşmesi [data-contract.md](anomaly-consensus-engine-data-contract.md), ayrıntılı akış [architecture.md](anomaly-consensus-engine-architecture.md), işletim adımları [runbook.md](anomaly-consensus-engine-runbook.md) içinde açıklanır.

## Doğrulama ve değerlendirme

Testler yalnız örneğin çalışmasını kontrol etmez; projenin davranışına özgü kabul ve ret koşullarını sınar. Örnek senaryoda gözlenen sonuçlar [results.md](anomaly-consensus-engine-results.md) içinde kayıtlıdır. CI Python 3.12/3.13, Ubuntu/Windows için tanımlıdır; yerel doğrulama Python 3.12 üzerinde yapılmıştır. GitHub'da ilk push sonrasında CI ayrıca çalışmalıdır.

## Sınırlar ve üretime geçiş

Eşikler demo içindir; saha verisinde yanlış alarm bütçesiyle doğrulanmalıdır.

Bu sürümde otomatik canlı entegrasyon, kullanıcı kimlik doğrulama, izleme altyapısı ve gerçek veriyle performans garantisi yoktur. İş kuralları sentetik kabul senaryolarıyla görünür hale getirilmiştir. Üretime geçmeden örnek sözleşmeyi gerçek alanlarla eşleyin, aşağıdaki deneyleri uygulayın ve sonuçları sürümleyin.

## Zorlaştırma deneyleri

1. Bir günlük ani spike ile 20 günlük level shift için ayrı alarm metrikleri çıkarın.
2. Baseline kirlenmesini azaltan robust update tasarlayın.
3. Alarm eşiklerini validation bölümündeki yanlış alarm bütçesiyle seçin.
4. Birden fazla metrikte alarm korelasyonunu incident gruplarına dönüştürün.

## GitHub'a taşıma

```bash
git init
git add .
git commit -m "Initial working analysis laboratory"
git branch -M main
git remote add origin https://github.com/olcayto-akbudak/anomaly-consensus-engine.git
git push -u origin main
```

Kendi hesabınıza taşırken `olcayto-akbudak` alanını değiştirin. Hesap bilgisi veya erişim anahtarı kaynak koda koymayın. Çalışan kaynak kod, testler ve teknik belgeler bu depoda yayımlanmıştır.

## Depo yerleşimi

GitHub sürümü dosyaları depo kökünde tutar; `anomaly_consensus_engine.py` alan motorunu ve CLI girişini içerir. `test_anomaly_consensus_engine.py` doğrudan bu modülü test eder. Belgeler ve örnek veriler aynı kökte yer alır.

## Ortak kaynak koleksiyonunda çalıştırma

Bu klasörde dosya adları çakışmaması için proje adıyla öneklenmiştir. Bağımsız ZIP asıl sade adlandırmayı korur.

```bash
python anomaly_consensus_engine.py demo
python -m unittest test_anomaly_consensus_engine -v
```
