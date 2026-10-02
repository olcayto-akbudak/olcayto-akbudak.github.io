# Dayanıklı Proje Portföyü Optimizasyonu

**Depo adı:** `robust-portfolio-optimizer` · Python 3.12+ · bağımsız çalışır · dış paket gerekmez.

Birden fazla kaynak bütçesinde en kötü senaryo değerini en yükseğe çıkaran proje setini bulmak.

## Teknik kapsam

Exact branch and bound, min-max scenarios, bağımlılık. Bu depo çalıştırılabilir bir mühendislik laboratuvarıdır. Ağ erişimi, özel hesap veya gerçek müşteri verisi gerektirmez. Örneklerde kasıtlı hatalar da bulunur; BLOCK, REVIEW veya false sonucu bazı senaryolarda beklenen davranıştır.

## Hızlı başlangıç

Depo kökünde:

```bash
python -m unittest -v
python robust_portfolio_optimizer.py demo
python robust_portfolio_optimizer.py demo --input robust_portfolio_optimizer_scenario.json --output custom-report.json
```

`robust_portfolio_optimizer_sample-report.json` gerçekten çalıştırılmış örnek çıktıdır. Yeniden çalıştırma sonucu `report.json` olur. Zamanlama ölçümleri hariç sabit seed ve girdiyle tekrarlanabilir. Kurulum için `pip install` gerekmez.

## Mimari ve kararlar

İşlem hattı: Budget validation → include/exclude search → scenario upper bound → dependency gate.

Temel varsayım: Değerler ve maliyetler negatif olamaz; en fazla 26 aday; hedef min(scenario totals).

Alan motoru ve komut satırı `robust_portfolio_optimizer.py`, kabul senaryosu `robust_portfolio_optimizer_scenario.json`, sınır ve hata testleri `test_robust_portfolio_optimizer.py` içindedir. Yapılandırma veri sözleşmesi [data-contract.md](robust-portfolio-optimizer-data-contract.md), ayrıntılı akış [architecture.md](robust-portfolio-optimizer-architecture.md), işletim adımları [runbook.md](robust-portfolio-optimizer-runbook.md) içinde açıklanır.

## Doğrulama ve değerlendirme

Testler yalnız örneğin çalışmasını kontrol etmez; projenin davranışına özgü kabul ve ret koşullarını sınar. Örnek senaryoda gözlenen sonuçlar [results.md](robust-portfolio-optimizer-results.md) içinde kayıtlıdır. CI Python 3.12/3.13, Ubuntu/Windows için tanımlıdır; yerel doğrulama Python 3.12 üzerinde yapılmıştır. GitHub'da ilk push sonrasında CI ayrıca çalışmalıdır.

## Sınırlar ve üretime geçiş

NP-hard arama büyük portföyde pahalıdır; süre sınırlı MILP çözümü ayrıca gerekir.

Bu sürümde otomatik canlı entegrasyon, kullanıcı kimlik doğrulama, izleme altyapısı ve gerçek veriyle performans garantisi yoktur. İş kuralları sentetik kabul senaryolarıyla görünür hale getirilmiştir. Üretime geçmeden örnek sözleşmeyi gerçek alanlarla eşleyin, aşağıdaki deneyleri uygulayın ve sonuçları sürümleyin.

## Zorlaştırma deneyleri

1. Rastgele küçük portföylerde brute-force oracle ile çözümü çapraz doğrulayın.
2. Bağımlılık döngülerini SCC ile önceden teşhis edin.
3. Bütçeyi yüzde 10 artırıp seçilen portföy ve worst-case değer duyarlılığını ölçün.
4. Büyük problemler için MILP adaptörü ve optimality gap raporu ekleyin.

## GitHub'a taşıma

```bash
git init
git add .
git commit -m "Initial working analysis laboratory"
git branch -M main
git remote add origin https://github.com/olcayto-akbudak/robust-portfolio-optimizer.git
git push -u origin main
```

Kendi hesabınıza taşırken `olcayto-akbudak` alanını değiştirin. Hesap bilgisi veya erişim anahtarı kaynak koda koymayın. Çalışan kaynak kod, testler ve teknik belgeler bu depoda yayımlanmıştır.

## Depo yerleşimi

GitHub sürümü dosyaları depo kökünde tutar; `robust_portfolio_optimizer.py` alan motorunu ve CLI girişini içerir. `test_robust_portfolio_optimizer.py` doğrudan bu modülü test eder. Belgeler ve örnek veriler aynı kökte yer alır.

## Ortak kaynak koleksiyonunda çalıştırma

Bu klasörde dosya adları çakışmaması için proje adıyla öneklenmiştir. Bağımsız ZIP asıl sade adlandırmayı korur.

```bash
python robust_portfolio_optimizer.py demo
python -m unittest test_robust_portfolio_optimizer -v
```
