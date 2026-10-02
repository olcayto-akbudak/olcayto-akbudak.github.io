# Gereksinim ve Test İzlenebilirliği

**Depo adı:** `requirements-traceability-graph` · Python 3.12+ · bağımsız çalışır · dış paket gerekmez.

Yüksek riskli gereksinimlerin güncel test kanıtı olmadan sürüme çıkmasını engellemek.

## Teknik kapsam

DAG, risk ağırlığı, revision freshness, impact BFS. Bu depo çalıştırılabilir bir mühendislik laboratuvarıdır. Ağ erişimi, özel hesap veya gerçek müşteri verisi gerektirmez. Örneklerde kasıtlı hatalar da bulunur; BLOCK, REVIEW veya false sonucu bazı senaryolarda beklenen davranıştır.

## Hızlı başlangıç

Depo kökünde:

```bash
python -m unittest -v
python requirements_traceability_graph.py demo
python requirements_traceability_graph.py demo --input requirements_traceability_graph_scenario.json --output custom-report.json
```

`requirements_traceability_graph_sample-report.json` gerçekten çalıştırılmış örnek çıktıdır. Yeniden çalıştırma sonucu `report.json` olur. Zamanlama ölçümleri hariç sabit seed ve girdiyle tekrarlanabilir. Kurulum için `pip install` gerekmez.

## Mimari ve kararlar

İşlem hattı: Graph validation → descendants → fresh passing tests → weighted coverage → release gate.

Temel varsayım: Her gereksinimden erişilebilen güncel başarılı test kapsama sayılır.

Alan motoru ve komut satırı `requirements_traceability_graph.py`, kabul senaryosu `requirements_traceability_graph_scenario.json`, sınır ve hata testleri `test_requirements_traceability_graph.py` içindedir. Yapılandırma veri sözleşmesi [data-contract.md](requirements-traceability-graph-data-contract.md), ayrıntılı akış [architecture.md](requirements-traceability-graph-architecture.md), işletim adımları [runbook.md](requirements-traceability-graph-runbook.md) içinde açıklanır.

## Doğrulama ve değerlendirme

Testler yalnız örneğin çalışmasını kontrol etmez; projenin davranışına özgü kabul ve ret koşullarını sınar. Örnek senaryoda gözlenen sonuçlar [results.md](requirements-traceability-graph-results.md) içinde kayıtlıdır. CI Python 3.12/3.13, Ubuntu/Windows için tanımlıdır; yerel doğrulama Python 3.12 üzerinde yapılmıştır. GitHub'da ilk push sonrasında CI ayrıca çalışmalıdır.

## Sınırlar ve üretime geçiş

Bağlantının iş anlamını insan doğrular; grafik tek başına test kalitesini ispatlamaz.

Bu sürümde otomatik canlı entegrasyon, kullanıcı kimlik doğrulama, izleme altyapısı ve gerçek veriyle performans garantisi yoktur. İş kuralları sentetik kabul senaryolarıyla görünür hale getirilmiştir. Üretime geçmeden örnek sözleşmeyi gerçek alanlarla eşleyin, aşağıdaki deneyleri uygulayın ve sonuçları sürümleyin.

## Zorlaştırma deneyleri

1. Tek testin birden fazla gereksinimi kapsaması için evidence provenance ekleyin.
2. Kritik gereksinim için tüm zorunlu testlerin geçmesi politikasını ekleyin.
3. Revision yerine kaynak içerik hash freshness kullanın.
4. Değişiklik etkisini upstream/downstream ayrı raporlayın.

## GitHub'a taşıma

```bash
git init
git add .
git commit -m "Initial working analysis laboratory"
git branch -M main
git remote add origin https://github.com/olcayto-akbudak/requirements-traceability-graph.git
git push -u origin main
```

Kendi hesabınıza taşırken `olcayto-akbudak` alanını değiştirin. Hesap bilgisi veya erişim anahtarı kaynak koda koymayın. Çalışan kaynak kod, testler ve teknik belgeler bu depoda yayımlanmıştır.

## Depo yerleşimi

GitHub sürümü dosyaları depo kökünde tutar; `requirements_traceability_graph.py` alan motorunu ve CLI girişini içerir. `test_requirements_traceability_graph.py` doğrudan bu modülü test eder. Belgeler ve örnek veriler aynı kökte yer alır.

## Ortak kaynak koleksiyonunda çalıştırma

Bu klasörde dosya adları çakışmaması için proje adıyla öneklenmiştir. Bağımsız ZIP asıl sade adlandırmayı korur.

```bash
python requirements_traceability_graph.py demo
python -m unittest test_requirements_traceability_graph -v
```
