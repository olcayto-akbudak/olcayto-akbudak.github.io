# Tasarım kararları

## Alan motorunu CLI'dan ayırmak

`run(config)` orkestrasyonu kaynak kodun doğrudan test edilebilmesini sağlar. JSON arayüz taşınabilirliği artırır; bu sürüm kullanıcı arayüzü barındırmaz.

## Seçilen yöntem

Unicode normalizasyonu, blocking, cluster constraint. Küme seviyesinde en fazla bir dolu vergi kimliği; boş kimlik eşleşmeyi tek başına engellemez.

## Bilinçli sınır

Tam adres ve dil çözümlemesi yoktur; eşikler etiketli gerçek çiftlerle doğrulanmalıdır.

## Önerilen sonraki doğrulama

Gerçek kullanım hacmiyle testten önce mevcut kabul ve ret örneklerinin alan uzmanı tarafından onaylanması gerekir. Sonraki sürüm performans ölçümleri, dış adaptör sözleşmesi ve üretim gözlemlenebilirliğini ayrı karar kayıtlarında ele almalıdır.
