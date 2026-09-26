# İbrahim Olcayto Akbudak — portföy

Tek dosyalık, statik portföy sitesi. GitHub Pages üzerinde çalışır; kurulum veya derleme gerektirmez.

## Yayımlama

1. GitHub'da herkese açık bir `olcayto-akbudak.github.io` deposu oluşturun (kişisel alan adında yayın için). Başka bir ad kullanırsanız adres `https://olcayto-akbudak.github.io/DEPO-ADI/` olur.
2. Bu paketteki `index.html` dosyasını deponun kök dizinine ekleyip `main` dalına gönderin.
3. Depoda **Settings → Pages → Build and deployment → Deploy from a branch** seçin; dal olarak `main`, klasör olarak `/ (root)` ayarlayıp kaydedin.
4. Pages yayımlama tamamlanınca siteyi belirtilen adreste açın.

## GitHub projelerinin güncellenmesi

`index.html`, ziyaret sırasında `https://api.github.com/users/olcayto-akbudak/repos` adresinden açık depoları sayfalayarak okur. Yeni bir **public** depo oluşturduğunuzda veya mevcut depoyu güncellediğinizde sayfa yenilendiği anda proje listesine yansır. Manuel HTML düzenlemesi ve Actions iş akışı gerekmez. GitHub API erişilemezse profil bağlantısı kullanılabilir; anonim API isteklerinin hız sınırı vardır. Gizli depolar listelenmez. Üstteki seçili proje anlatımları editoryaldir ve yalnızca `index.html` düzenlenince değişir.

## İçerik düzenleme

Metinler, seçili proje kartları, iletişim ve stiller `index.html` içindedir. Yeni biyografi veya deneyim bilgileri için bu dosyayı düzenleyip tekrar gönderin. GitHub kullanıcı adı değişirse `loadGitHubProjects` içindeki `user` değişkenini ve profil bağlantısını da güncelleyin.
