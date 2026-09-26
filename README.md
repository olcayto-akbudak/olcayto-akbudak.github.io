# İbrahim Olcayto Akbudak | İş Geliştirme Analisti

GitHub Pages portföyü ve **20 tamamlanmış, yeniden çalıştırılabilir demo analiz projesi**. Veri kümeleri tamamen sentetiktir; gerçek şirket, müşteri veya GİB kayıtlarını temsil etmez.

## Site

`index.html` ana sayfadır. `en.html` İngilizce giriş sayfası, `og-image.png` paylaşım görselidir. `analizler.html` 20 projenin sonuçlarını ve sorgularını gezilebilir tek sayfada sunar. `analizler-kaynak-kod.zip` bütün veri ve çalıştırılabilir proje klasörlerini içerir; `analizler/<proje>/index.html` adresleri tam kaynak dağıtımında ayrıca çalışır. Filtrelenebilir proje kartları ana sayfada bulunur. Animasyonlar azaltılmış hareket sistem ayarına uyar.

GitHub açık depoları sayfa açıldığında herkese açık API'den çekilir. API geçici olarak çalışmazsa profil bağlantısı görünür kalır. Seçili proje anlatımları ve 20 demo analiz, statik site içeriğidir ve kaynak güncellemesiyle değişir.

## Tekrar üretme

Python 3 ve SQLite (Python standart kitaplığı) yeterlidir. Tek bir projeyi çalıştırmak için:

```bash
python analizler/efatura-sla/run.py
```

Tüm sentetik veri kümeleri, raporlar ve proje dosyaları aynı sabit tohumla tekrar üretilir:

```bash
python build_analyses.py
```

Her proje klasörü `data.csv`, `analysis.sql`, `run.py`, `results.json`, `index.html` ve `README.md` içerir. `run.py` çıktısı `results.json` ile birebir karşılaştırılabilir. Analizler portföy ve öğrenme amaçlıdır; gerçek operasyonel bulgu, mevzuat yorumu veya yatırım kararı olarak kullanılmaz.

## GitHub Pages

Bu depo `olcayto-akbudak.github.io` olarak adlandırıldığında **Settings → Pages → Deploy from a branch → main → /(root)** seçimiyle yayımlanır. `index.html` kök dizinde bulunmalıdır. Site adresi `https://olcayto-akbudak.github.io/` olur.
