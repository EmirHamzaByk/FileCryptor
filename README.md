# File Cryptor: Güvenli Dosya Şifreleme Uygulaması


File Cryptor, dosyalarınızı güvenli bir şekilde şifrelemek ve şifrelenmiş dosyaları çözmek için kullanabileceğiniz basit ve etkili bir Python uygulamasıdır. Bu uygulama, simetrik şifreleme algoritması olan Fernet ile cryptography kütüphanesini kullanır ve güvenilir PyQt5 kütüphanesini GUI (Grafiksel Kullanıcı Arayüzü) oluşturmak için kullanır.

## Özellikler
Kolay Dosya Seçimi: Şifrelemek istediğiniz dosyaları kolayca seçmek için dosya seçme düğmesini kullanabilirsiniz.

**Güçlü Şifreleme Anahtarı Oluşturma:** Uygulama, otomatik olarak benzersiz ve güçlü şifreleme anahtarları oluşturabilir. Bu anahtarları şifreleme ve çözme işlemlerinde kullanabilirsiniz. [***Anahtarınızı Kaybederseniz Şifrelenen Dosyanızı Çözemezsiniz***]

**Dinamik Anahtar Girişi: **İster kendi şifreleme anahtarınızı girin, ister uygulama tarafından oluşturulan anahtarları kullanın. Esnek anahtar yönetimi ile dosyalarınızın güvenliğini sağlayın.

**Hata Kontrolü ve Geri Bildirim:** Dosya şifreleme ve çözme işlemleri sırasında ortaya çıkan hatalar için kullanıcı dostu hata iletişim kutuları sağlar. Dosyalarınızın güvenli bir şekilde işlenmesini sağlamak için gerekli önlemler alınmıştır.

## Nasıl Kullanılır?
**Dosya Seçimi:** Şifrelemek istediğiniz dosyaları "Dosya Seç" düğmesine tıklayarak kolayca seçebilirsiniz.

**Şifreleme Anahtarı Oluşturma:** Uygulama, "Anahtar Oluştur" düğmesine tıkladığınızda otomatik olarak güçlü bir şifreleme anahtarı oluşturur. Ayrıca, kendi özel anahtarınızı girmek için "Anahtarınızı buraya girin veya anahtar oluşturun" alanını kullanabilirsiniz.

**Dosya Şifreleme:** Şifrelemek istediğiniz dosyaları seçtikten sonra, "Şifrele" düğmesine tıklayarak dosyalarınızı güvenli bir şekilde şifreleyebilirsiniz. Güçlü şifreleme algoritması sayesinde dosyalarınızın korunduğundan emin olabilirsiniz.

**Dosya Çözme:** Daha önce şifrelenmiş dosyalarınızı çözmek için aynı anahtarı kullanabilirsiniz. Şifrelenmiş dosyaları seçtikten sonra "Çöz" düğmesine tıklamanız yeterlidir.

## Güvenlik Uyarısı
Dosya şifreleme ve çözme işlemleri, simetrik şifreleme algoritması olan Fernet kullanılarak gerçekleştirilir. Bu nedenle, dosyalarınızın güvenliği anahtara bağlıdır. **Anahtarın kaybedilmesi durumunda şifrelenmiş dosyaların geri dönüşü olmayabilir.** Dosya şifreleme ve çözme işlemleri sırasında anahtarı güvende tutmaya özen gösterin.
