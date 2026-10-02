# Mimari

Kısa süreli küçük örneklem sıçraması ile kalıcı hizmet bozulmasını ayırmak.

```mermaid
flowchart TD
  A["Sentetik senaryo"] --> B["Girdi ve kural doğrulama"]
  B --> C["SLO"]
  C --> D["Bulgular ve durumlar"]
  D --> E["JSON rapor"]
```

Asıl alan akışı: **Time window selection → error rates → budget burn → minimum volume → combined page**. CLI JSON yükler, çekirdek `run(config)` alan motorunu çağırır ve JSON seri hale getirir. Veritabanı kullanan örnekler geçici dizinde izole edilir; kalıcı sınıflar doğrudan çağrılırken dosya yolu dışarıdan verilir.

## İnvariant ve başarısızlık sınırı

Pencereler now-window < at <= now; alarm tüm pencerelerde eşik aşılınca açılır.

Uzun dönem hata bütçesi ayrıca tutulmalıdır; remaining değeri son pencerenin bütçesidir.

Her hata kararı makine tarafından okunabilir çıktı veya açık exception üretir. Geçersiz yapılandırma sessizce düzeltilmez. Olası tekrarların güvenliği ilgili çekirdeğin kabul kurallarına bağlıdır; bütün projelere ortak bir retry uygulanmaz.
