# Sipariş Saga ve Telafi Laboratuvarı

**Depo adı:** `order-saga-recovery` · Python 3.12+ · bağımsız çalışır · dış paket gerekmez.

Stok/ödeme/kargo zincirinde çöken koordinatörü yeniden başlatmak ve güvenli telafi etmek.

## Teknik kapsam

Kalıcı adımlar, çökme enjeksiyonu, compensation. Bu depo çalıştırılabilir bir mühendislik laboratuvarıdır. Ağ erişimi, özel hesap veya gerçek müşteri verisi gerektirmez. Örneklerde kasıtlı hatalar da bulunur; BLOCK, REVIEW veya false sonucu bazı senaryolarda beklenen davranıştır.

## Hızlı başlangıç

Depo kökünde:

```bash
python -m unittest -v
python order_saga_recovery.py demo
python order_saga_recovery.py demo --input order_saga_recovery_scenario.json --output custom-report.json
```

`order_saga_recovery_sample-report.json` gerçekten çalıştırılmış örnek çıktıdır. Yeniden çalıştırma sonucu `report.json` olur. Zamanlama ölçümleri hariç sabit seed ve girdiyle tekrarlanabilir. Kurulum için `pip install` gerekmez.

## Mimari ve kararlar

İşlem hattı: Inventory → payment → shipping → completion; failure → compensation/manual.

Temel varsayım: Katılımcılar order+step anahtarlı kalıcı yerel mock; kargo gerçekleşmişse manuel inceleme gerekir.

Alan motoru ve komut satırı `order_saga_recovery.py`, kabul senaryosu `order_saga_recovery_scenario.json`, sınır ve hata testleri `test_order_saga_recovery.py` içindedir. Yapılandırma veri sözleşmesi [data-contract.md](order-saga-recovery-data-contract.md), ayrıntılı akış [architecture.md](order-saga-recovery-architecture.md), işletim adımları [runbook.md](order-saga-recovery-runbook.md) içinde açıklanır.

## Doğrulama ve değerlendirme

Testler yalnız örneğin çalışmasını kontrol etmez; projenin davranışına özgü kabul ve ret koşullarını sınar. Örnek senaryoda gözlenen sonuçlar [results.md](order-saga-recovery-results.md) içinde kayıtlıdır. CI Python 3.12/3.13, Ubuntu/Windows için tanımlıdır; yerel doğrulama Python 3.12 üzerinde yapılmıştır. GitHub'da ilk push sonrasında CI ayrıca çalışmalıdır.

## Sınırlar ve üretime geçiş

Gerçek dağıtık transaction yoktur; remote katılımcı idempotency ve outbox gereklidir.

Bu sürümde otomatik canlı entegrasyon, kullanıcı kimlik doğrulama, izleme altyapısı ve gerçek veriyle performans garantisi yoktur. İş kuralları sentetik kabul senaryolarıyla görünür hale getirilmiştir. Üretime geçmeden örnek sözleşmeyi gerçek alanlarla eşleyin, aşağıdaki deneyleri uygulayın ve sonuçları sürümleyin.

## Zorlaştırma deneyleri

1. Katılımcıları ayrı veritabanı veya HTTP servisine taşıyın.
2. Koordinatör checkpointinden önce/sonra her adımda çökme enjekte edin.
3. Telafi başarısızlığı için kalıcı compensation retry kuyruğu ekleyin.
4. Kargo geri alınamıyorsa manuel kararın kimlik ve gerekçesini audit kaydına bağlayın.

## GitHub'a taşıma

```bash
git init
git add .
git commit -m "Initial working analysis laboratory"
git branch -M main
git remote add origin https://github.com/olcayto-akbudak/order-saga-recovery.git
git push -u origin main
```

Kendi hesabınıza taşırken `olcayto-akbudak` alanını değiştirin. Hesap bilgisi veya erişim anahtarı kaynak koda koymayın. Çalışan kaynak kod, testler ve teknik belgeler bu depoda yayımlanmıştır.

## Depo yerleşimi

GitHub sürümü dosyaları depo kökünde tutar; `order_saga_recovery.py` alan motorunu ve CLI girişini içerir. `test_order_saga_recovery.py` doğrudan bu modülü test eder. Belgeler ve örnek veriler aynı kökte yer alır.

## Bağlantı yaşam döngüsü

SQLite transaction context bağlantıyı kendi başına kapatmaz. `sqlite_session` başarıda commit, hatada rollback yapar ve her durumda dosya tanıtıcısını kapatır. Test başlangıcında kapanan bağlantıya erişimin `ProgrammingError` verdiği kontrol edilir; geçici dosyalar Windows üzerinde kilitli kalmaz.

## Ortak kaynak koleksiyonunda çalıştırma

Bu klasörde dosya adları çakışmaması için proje adıyla öneklenmiştir. Bağımsız ZIP asıl sade adlandırmayı korur.

```bash
python order_saga_recovery.py demo
python -m unittest test_order_saga_recovery -v
```
