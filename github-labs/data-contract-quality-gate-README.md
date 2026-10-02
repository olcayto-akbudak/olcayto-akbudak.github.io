# Veri Sözleşmesi ve Karantina

**Depo adı:** `data-contract-quality-gate` · Python 3.12+ · bağımsız çalışır · dış paket gerekmez.

Şema ve veri hatalarının downstream raporlara sessizce girmesini engellemek.

## Teknik kapsam

Type/range/reference/unique/freshness, PSI. Bu depo çalıştırılabilir bir mühendislik laboratuvarıdır. Ağ erişimi, özel hesap veya gerçek müşteri verisi gerektirmez. Örneklerde kasıtlı hatalar da bulunur; BLOCK, REVIEW veya false sonucu bazı senaryolarda beklenen davranıştır.

## Hızlı başlangıç

Depo kökünde:

```bash
python -m unittest -v
python data_contract_quality_gate.py demo
python data_contract_quality_gate.py demo --input data_contract_quality_gate_scenario.json --output custom-report.json
```

`data_contract_quality_gate_sample-report.json` gerçekten çalıştırılmış örnek çıktıdır. Yeniden çalıştırma sonucu `report.json` olur. Zamanlama ölçümleri hariç sabit seed ve girdiyle tekrarlanabilir. Kurulum için `pip install` gerekmez.

## Mimari ve kararlar

İşlem hattı: Row contract checks → duplicate/freshness → quarantine → release gate → PSI.

Temel varsayım: Bilinmeyen alan REVIEW; geçersiz satır BLOCK; kabul edilen ve karantinadaki satırlar ayrılır.

Alan motoru ve komut satırı `data_contract_quality_gate.py`, kabul senaryosu `data_contract_quality_gate_scenario.json`, sınır ve hata testleri `test_data_contract_quality_gate.py` içindedir. Yapılandırma veri sözleşmesi [data-contract.md](data-contract-quality-gate-data-contract.md), ayrıntılı akış [architecture.md](data-contract-quality-gate-architecture.md), işletim adımları [runbook.md](data-contract-quality-gate-runbook.md) içinde açıklanır.

## Doğrulama ve değerlendirme

Testler yalnız örneğin çalışmasını kontrol etmez; projenin davranışına özgü kabul ve ret koşullarını sınar. Örnek senaryoda gözlenen sonuçlar [results.md](data-contract-quality-gate-results.md) içinde kayıtlıdır. CI Python 3.12/3.13, Ubuntu/Windows için tanımlıdır; yerel doğrulama Python 3.12 üzerinde yapılmıştır. GitHub'da ilk push sonrasında CI ayrıca çalışmalıdır.

## Sınırlar ve üretime geçiş

PSI kategorik histogram karşılaştırmasıdır; kendi başına istatistiksel anlamlılık testi değildir.

Bu sürümde otomatik canlı entegrasyon, kullanıcı kimlik doğrulama, izleme altyapısı ve gerçek veriyle performans garantisi yoktur. İş kuralları sentetik kabul senaryolarıyla görünür hale getirilmiştir. Üretime geçmeden örnek sözleşmeyi gerçek alanlarla eşleyin, aşağıdaki deneyleri uygulayın ve sonuçları sürümleyin.

## Zorlaştırma deneyleri

1. Birden fazla sütunda birleşik unique ve foreign key sözleşmesi ekleyin.
2. Karantinayı veri sürümü ve kural sürümüyle kalıcı depoya yazın.
3. PSI eşiklerini ayrı historical validation bölümlerinde seçin.
4. Schema drift için alan ekleme ile type değiştirme politikalarını ayrıştırın.

## GitHub'a taşıma

```bash
git init
git add .
git commit -m "Initial working analysis laboratory"
git branch -M main
git remote add origin https://github.com/olcayto-akbudak/data-contract-quality-gate.git
git push -u origin main
```

Kendi hesabınıza taşırken `olcayto-akbudak` alanını değiştirin. Hesap bilgisi veya erişim anahtarı kaynak koda koymayın. Çalışan kaynak kod, testler ve teknik belgeler bu depoda yayımlanmıştır.

## Depo yerleşimi

GitHub sürümü dosyaları depo kökünde tutar; `data_contract_quality_gate.py` alan motorunu ve CLI girişini içerir. `test_data_contract_quality_gate.py` doğrudan bu modülü test eder. Belgeler ve örnek veriler aynı kökte yer alır.

## Ortak kaynak koleksiyonunda çalıştırma

Bu klasörde dosya adları çakışmaması için proje adıyla öneklenmiştir. Bağımsız ZIP asıl sade adlandırmayı korur.

```bash
python data_contract_quality_gate.py demo
python -m unittest test_data_contract_quality_gate -v
```
