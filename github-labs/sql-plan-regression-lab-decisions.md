# Tasarım kararları

## Alan motorunu CLI'dan ayırmak

`run(config)` orkestrasyonu kaynak kodun doğrudan test edilebilmesini sağlar. JSON arayüz taşınabilirliği artırır; bu sürüm kullanıcı arayüzü barındırmaz.

## Seçilen yöntem

Preaggregation, join fanout, digest, query plan. Para tamsayı; iki ticket join fanout hatasını bilerek gösterir; sürelerden önce doğruluk değerlendirilir.

## Bilinçli sınır

SQLite yerel ölçümüdür; PostgreSQL planlarına veya gerçek üretim yüküne genellenmez.

## Önerilen sonraki doğrulama

Gerçek kullanım hacmiyle testten önce mevcut kabul ve ret örneklerinin alan uzmanı tarafından onaylanması gerekir. Sonraki sürüm performans ölçümleri, dış adaptör sözleşmesi ve üretim gözlemlenebilirliğini ayrı karar kayıtlarında ele almalıdır.
