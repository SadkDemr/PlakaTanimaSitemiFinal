
PLAKA TANIMA SİSTEMİ
Automatic Number Plate Recognition
 Proje Adı: Plaka Tanıma Sistemi
Proje Türü:Yazılım Mühendisliği Lisans Programı IV. Yarıyıl Mühendislik Projesi II Dersi Projesi.

Proje Takımı:
•	Muhammed Sadık DEMİR   (Yazılım Mühendisliği Bölümü 2. Sınıf Öğrencisi)
Projenin Amacı:
Açık kaynaklı OpenCv ve Easy OCR kütüphanesi kullanılarak Python programlama dili ile plaka tanıma sistemi geliştirmek.
Projenin Çıktısı:
Python programlama dili ile geliştirilmiş 5 aşamadan geçerek yüklenen araç resmi üzerinde ki plakayı metin olarak aracın üzerine çıkarmaktadır
Projenin özellikleri ve aşamaları:
•	Proje 5 temel bölümden oluşmaktadır.
•	1-) Görüntüyü Gri Tonlama ve Bulanık Bir Şekilde Okuma; Burada yüklenen resim gri tonlanır bu işlem filtreleme işlemine yardımcıdır.
•	2-)Filtreleme İşlemi; Burada yüklene araç görseli çeşitli filtreleme işlemlerinden geçer bunu sebebi ise plaka kısmını ortaya çıkarmaktır.
 
•	3-)Kontürleme ve Maskeleme İşlemi; Bu bölümde ise filtreleme işleminden geçen araç görseli sadece araç plakası kalıncaya dek kontürlenir bunun sebebi ise Easy OCR kütüphanesinin plaka üzerinde ki plaka kodunu rahat bir şekilde okuması ve yazdırmasıdır.
 
•	4-) Easy OCR Kullanarak Metin Çıkarma; Bu bölümde ise yukarıda kontürleme işlemi yapılmış plaka görselini okur ve metine dönüştürür.
•	5-)Tespit Edilen Plakayı Yazma; Burada ise artık tüm işlemler bitmiş ve yüklenen görselin üstüne plaka metni çıkartılır.
 
Web Application Bölümü
 
Kullanılan Araçlar:
•	Python
•	OpenCV
•	Html
•	CSS
Geliştirmeye Açık Alanlar:
Şu şekilde özetlenebilir:
•	Bir kamera sistemine bağlanarak gelen araçları anlık plakasını okur ve data setine atabiliriz böylelikle bir site otopark sistemi oluşturulabilir.



Ticarileşme Potansiyeli:
Web tabanlı bir site otopark sistemi yapılabilir. Öncelikle projemizi bir kamera sistemine bağlayabiliriz. Daha sonra gelen araçların anlık plakasını okutup data setine yazdırabiliriz. Önceden kayıtlı plaklarla eşleşen plakalar için otopark kapısı açılıp kapanabilir. Böylelikle tamamen otomatik çalışan bir site otopark sistemi yapabiliriz. 
