# Kısıtlı Müşteri Eşleştirme

**Depo adı:** `entity-resolution-workbench` · Python 3.12+ · bağımsız çalışır · dış paket gerekmez.

Benzer müşteri adlarını birleştirirken çelişkili vergi kimliklerinin dolaylı birleşmesini önlemek.

## Teknik kapsam

Unicode normalizasyonu, blocking, cluster constraint. Bu depo çalıştırılabilir bir mühendislik laboratuvarıdır. Ağ erişimi, özel hesap veya gerçek müşteri verisi gerektirmez. Örneklerde kasıtlı hatalar da bulunur; BLOCK, REVIEW veya false sonucu bazı senaryolarda beklenen davranıştır.

## Hızlı başlangıç

Depo kökünde:

```bash
python -m unittest -v
python entity_resolution_workbench.py demo
python entity_resolution_workbench.py demo --input entity_resolution_workbench_scenario.json --output custom-report.json
```

`entity_resolution_workbench_sample-report.json` gerçekten çalıştırılmış örnek çıktıdır. Yeniden çalıştırma sonucu `report.json` olur. Zamanlama ölçümleri hariç sabit seed ve girdiyle tekrarlanabilir. Kurulum için `pip install` gerekmez.

## Mimari ve kararlar

İşlem hattı: Country/name blocking → pair similarity → sorted edges → cluster tax-id gate.

Temel varsayım: Küme seviyesinde en fazla bir dolu vergi kimliği; boş kimlik eşleşmeyi tek başına engellemez.

Alan motoru ve komut satırı `entity_resolution_workbench.py`, kabul senaryosu `entity_resolution_workbench_scenario.json`, sınır ve hata testleri `test_entity_resolution_workbench.py` içindedir. Yapılandırma veri sözleşmesi [data-contract.md](entity-resolution-workbench-data-contract.md), ayrıntılı akış [architecture.md](entity-resolution-workbench-architecture.md), işletim adımları [runbook.md](entity-resolution-workbench-runbook.md) içinde açıklanır.

## Doğrulama ve değerlendirme

Testler yalnız örneğin çalışmasını kontrol etmez; projenin davranışına özgü kabul ve ret koşullarını sınar. Örnek senaryoda gözlenen sonuçlar [results.md](entity-resolution-workbench-results.md) içinde kayıtlıdır. CI Python 3.12/3.13, Ubuntu/Windows için tanımlıdır; yerel doğrulama Python 3.12 üzerinde yapılmıştır. GitHub'da ilk push sonrasında CI ayrıca çalışmalıdır.

## Sınırlar ve üretime geçiş

Tam adres ve dil çözümlemesi yoktur; eşikler etiketli gerçek çiftlerle doğrulanmalıdır.

Bu sürümde otomatik canlı entegrasyon, kullanıcı kimlik doğrulama, izleme altyapısı ve gerçek veriyle performans garantisi yoktur. İş kuralları sentetik kabul senaryolarıyla görünür hale getirilmiştir. Üretime geçmeden örnek sözleşmeyi gerçek alanlarla eşleyin, aşağıdaki deneyleri uygulayın ve sonuçları sürümleyin.

## Zorlaştırma deneyleri

1. 100.000 kayıt için blocking recall ve candidate reduction oranlarını ölçün.
2. Transitif bağlarda vergi kimliği çatışmasını canlı inceleme kuyruğuna aktarın.
3. Adres ve telefon özelliklerine kalibre edilmiş skor ekleyin.
4. Label çiftleriyle precision/recall ölçün; örnek similarity değerini doğruluk sanmayın.

## GitHub'a taşıma

```bash
git init
git add .
git commit -m "Initial working analysis laboratory"
git branch -M main
git remote add origin https://github.com/olcayto-akbudak/entity-resolution-workbench.git
git push -u origin main
```

Kendi hesabınıza taşırken `olcayto-akbudak` alanını değiştirin. Hesap bilgisi veya erişim anahtarı kaynak koda koymayın. Çalışan kaynak kod, testler ve teknik belgeler bu depoda yayımlanmıştır.

## Depo yerleşimi

GitHub sürümü dosyaları depo kökünde tutar; `entity_resolution_workbench.py` alan motorunu ve CLI girişini içerir. `test_entity_resolution_workbench.py` doğrudan bu modülü test eder. Belgeler ve örnek veriler aynı kökte yer alır.

## Ortak kaynak koleksiyonunda çalıştırma

Bu klasörde dosya adları çakışmaması için proje adıyla öneklenmiştir. Bağımsız ZIP asıl sade adlandırmayı korur.

```bash
python entity_resolution_workbench.py demo
python -m unittest test_entity_resolution_workbench -v
```
