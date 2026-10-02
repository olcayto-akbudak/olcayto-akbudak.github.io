# Tasarım kararları

## Alan motorunu CLI'dan ayırmak

`run(config)` orkestrasyonu kaynak kodun doğrudan test edilebilmesini sağlar. JSON arayüz taşınabilirliği artırır; bu sürüm kullanıcı arayüzü barındırmaz.

## Seçilen yöntem

SLO, düşük hacim koruması, p95, hata bütçesi. Pencereler now-window < at <= now; alarm tüm pencerelerde eşik aşılınca açılır.

## Bilinçli sınır

Uzun dönem hata bütçesi ayrıca tutulmalıdır; remaining değeri son pencerenin bütçesidir.

## Önerilen sonraki doğrulama

Gerçek kullanım hacmiyle testten önce mevcut kabul ve ret örneklerinin alan uzmanı tarafından onaylanması gerekir. Sonraki sürüm performans ölçümleri, dış adaptör sözleşmesi ve üretim gözlemlenebilirliğini ayrı karar kayıtlarında ele almalıdır.
