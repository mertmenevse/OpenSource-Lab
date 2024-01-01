# Projelerin Açıklaması
## (OpenSource1) Proje 1: Flask API Kullanıcı Yönetimi
Bu Python script'i, Flask ve Flask-RESTful kütüphanelerini kullanarak bir web API uygulamasını başlatır. Uygulama, bir CSV dosyasında saklanan kullanıcı verilerini işleyen basit bir API sağlar. İşlevselliği şu şekilde özetleyebiliriz:

***1. Flask ve Flask-RESTful Kütüphaneleri İçe Aktarılır:***
- `from flask import Flask, request`
- `from flask_restful import Api, Resource`
- `import pandas as pd`

***2.Flask Uygulaması ve API Oluşturulur:***
- `app = Flask(__name__)`
- `api = Api(app)`

***3. 'Users', 'Cities' ve 'Name' Sınıfları Tanımlanır:***
- `Users`: Tüm kullanıcıları getirmek, yeni bir kullanıcı eklemek ve bir kullanıcıyı silmek için HTTP GET, POST ve DELETE yöntemlerini içerir.
- `Cities`: Şehir verilerini getirmek için HTTP GET yöntemini içerir.
- `Name`: Belirli bir kullanıcı adına sahip bir kaydı getirmek için HTTP GET yöntemini içerir.

***4. 'Users' Sınıfı Metotları:***
- `get`: Tüm kullanıcıları CSV dosyasından okuyarak bir JSON yanıtı döndürür.
- `post`: Gelen JSON verisine dayalı olarak yeni bir kullanıcı ekler ve bir onay mesajı döndürür.
- `delete`: Belirtilen isme sahip bir kullanıcıyı CSV dosyasından siler ve bir onay mesajı döndürür.

***5. 'Cities' Sınıfı Metodu:***
- `get`: Şehir verilerini CSV dosyasından okuyarak bir JSON yanıtı döndürür.

***6. 'Name' Sınıfı Metodu:***
- `get`: Belirli bir isme sahip bir kullanıcıyı CSV dosyasından bulur ve bir JSON yanıtı döndürür. Eğer belirtilen isimde bir kullanıcı bulunamazsa 404 hatası döndürür.

***7. URL End Noktaları Eklenir:***
- `/users`: Tüm kullanıcıları yöneten Users sınıfına yönlendirilir.
- `/cities`: Şehir verilerini yöneten Cities sınıfına yönlendirilir.
- `/<string:name>`: Belirli bir kullanıcı adına sahip kaydı getiren Name sınıfına yönlendirilir.

***8. Uygulama Başlatılır:***
- `if __name__ == '__main__':`
-     `app.run()`

Bu, uygulamayı çalıştırır. Eğer uygulamayı dış dünyadan erişilebilir yapmak istiyorsanız, app.run(host="0.0.0.0", port=5000) şeklinde belirli bir IP adresi ve port numarası da verebilirsiniz.

Bu API, kullanıcı verilerini CSV dosyasında basit bir şekilde saklamakta, bu verilere erişmek, eklemek ve silmek için HTTP isteklerine yanıt vermektedir.

## (OpenSource2) Proje 2: Lorem Ipsum
Lorem Ipsum Nedir ve Ne Anlama Gelir?
Lorem Ipsum yaklaşık 500 yıl önce bir matbaacının baskılar için hazırladığı font model kitabında kullanılmıştır. Yıllar geçtikçe kullanım alanları da kullanan kişi sayısı da artarak devam etmiştir. Kullanan insanlar uzun yıllar bunun anlamsız kelimelerden oluşan bir metin olduğunu düşündüler. Ancak sonradan edinilen bulgular aslında gerçeğin çok farklı olduğunu ortaya koydu.

Lorem Ipsum'un tarihi milattan önce 45 (MÖ.43) yılına kadar dayanıyor. O tarihlerde Çiçero tarafından yazılan "İyi ve Kötünün Uç Sınırları" kitabının 1.30.32 paragrafında geçtiği sonradan öğrenilmiştir. Kitap aynı zamanda 1500'lü yıllarda Avrupa'da Rönesans dönemi ile popüler olmuş, aynı dönemde Lorem Ipsum'u ilk kullanan matbaacıya da muhtemelen bu vesileyle ulaşmış.

Lorem Ipsum, baskı ve yazılı tasarım endüstrilerinde metin düzenleme ve yer tutma amacıyla sıkça kullanılan taklit metinlerden biridir. Metin, Latince kökenli olup "acı, sıkıntı" anlamına gelmez; tamamen rastgele seçilmiş kelimeler ve dilbilgisi öğelerinden oluşur. Lorem Ipsum'un kullanılma amacı, bir tasarımın metin içeriğini değerlendirmek ve düzenlemek için gerçek içerik olmadan bir yer tutucu sağlamaktır.

Lorem Ipsum metni, bilinçli olarak anlamsız veya çelişkili kelimeler içerir, böylece bir tasarımın görünümüne odaklanabilirsiniz, gerçek içerikle dikkatinizin dağılmaması için. Bu metin, tipografi, yazı tipi seçimi, sayfa düzeni gibi görsel unsurların değerlendirilmesi aşamasında tasarımcılara ve yazı işleri profesyonellerine yardımcı olmak için kullanılır.

Lorem Ipsum'un kökeni M.Ö. 45 tarihli "de Finibus Bonorum et Malorum" (İyi ve Kötünün Sınırları) eseriyle bağlantılıdır. Metin, Rönesans dönemi olan 15. yüzyıldan beri kullanılmaktadır. günümüzde ise tipografi ve grafik tasarım uygulamalarında yaygın olarak karşılaşılan bir yer tutucu metin haline gelmiştir.

Yıllardır kullanılan Lorem Ipsum taslağı;
> "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

Lorem Ipsum Anlamı Nedir?
Yazının bir bütün olarak anlamı bulunmamaktadır. Ancak Çiçero'dan alınan kısım ve anlamı şöyle;

> "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."

> "Acıyı seven, arayan ve ona sahip olmak isteyen hiç kimse yoktur. Nedeni basit. Çünkü o acıdır..."

Yazının geri kalan kısmı ise latin harflerinden ilk bakışta anlamlı bir yazı gibi görünebilecek şekilde rasgele yazılmıştır.  

Lorem Ipsum Neden Kullanılır?
Yapılan araştırmalar gösteriyor ki, insanlar bir baskı ürününü ya da dijital tasarımı değerlendirirken kendilerini yazıya ve onun anlamına kaptırmadan objektif değerlendirme yapamıyorlar. Bu nedenle Lorem Ipsum insanların tasarıma daha iyi odaklanmaları ve aynı zamanda anlamlı bir yazı formuna çok benzer bir örnekle birlikte tasarımı görebilmeleri için kullanılır.  

Bu kullanımın yıllarca süregelen bir gelenek olduğunu söyleyebiliriz. Günümüzde hala birçok insan tarafından aktif olarak kullanıldığını da düşünürsek, matbaa, online ve tasarım dünyasında kullanılmaması için hiçbir sebep yok.

Örnek olarak oluşturulmuş 2 paragraf uzunluğundaki Lorem Ipsum örneğini de buraya bırakalım. Belki de arkasında yatan başka gizemleri de siz çözebilirsiniz.

> "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque quis facilisis velit. Nunc justo lorem, feugiat molestie faucibus ac, consequat nec magna. Praesent convallis tortor et tortor dapibus, a tincidunt felis finibus. Quisque purus nisl, malesuada id lacinia nec, sollicitudin ut eros. Mauris mollis mauris in felis viverra, eget pulvinar lorem porta. Sed id ullamcorper massa, eget tempus libero. Proin eu rhoncus mauris. Mauris ac pharetra turpis.

> Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse mattis, enim ut sodales bibendum, purus tellus aliquam felis, vel placerat lectus massa vitae justo. Curabitur pellentesque a quam vel aliquam. In ornare ultricies nunc, nec eleifend est fringilla nec. Cras vestibulum eros ultricies fringilla laoreet. Suspendisse sodales odio risus, et ultricies leo elementum consequat. Fusce metus enim, tristique eu velit eleifend, fringilla tristique purus. Mauris pharetra posuere mauris, id auctor nunc eleifend eget. Maecenas in justo sit amet est volutpat lobortis vitae id nisl. Praesent in quam ut massa fermentum tempus. In porttitor magna et justo ullamcorper consectetur. Nullam in ante a elit maximus eleifend. Nunc neque sem, dapibus a viverra ac, sodales volutpat tortor."

### Kod Açıklamaları
Bu Python script'i, requests kütüphanesini kullanarak JSONPlaceholder adlı bir JSON API ile etkileşimde bulunur. Bu API, test verileri sağlayan bir hizmettir. Script, bu API'ye `HTTP` `GET`, `POST` ve `DELETE` istekleri gönderir ve alınan yanıtları işleyerek CSV dosyalarına yazar. Kodun işlevselliği şu şekildedir:

***1. API Endpoint URL'si Belirlenir:***
- `api_url = "https://jsonplaceholder.typicode.com/todos"`
- Bu URL, JSONPlaceholder servisinin "todos" adlı endpoint'ine işaret eder. Bu endpoint, kullanıcılara ait görevleri temsil eden test verilerini sağlar.

***2. HTTP GET İsteği Gönderilir:***
- `response_get = requests.get(api_url)`
- Bu satır, belirtilen URL'ye bir HTTP GET isteği gönderir.

***3. HTTP GET Yanıtı İşlenir:***
- Yanıt başarılı ise (HTTP status kodu 200), JSON formatındaki yanıtı işler ve ekrana yazdırır.
- JSON verisi CSV dosyasına yazılır.
- `if response_get.status_code == 200:`
-     `data_get = response_get.json()`
-     #JSON verisini işleme ve CSV dosyasına yazma işlemleri burada yapılır.
- `else`:
-     #HTTP GET isteğinde bir hata varsa, hata kodunu ve mesajını yazdırır.

***4. HTTP POST İsteği Gönderilir:***
- `new_todo = {"userId": 1, "title": "New Todo", "completed": False}`
- `response_post = requests.post(api_url, json=new_todo)`
- Bu satır, belirtilen URL'ye bir HTTP POST isteği gönderir. Yeni bir görev eklemek için kullanılır.

***5. HTTP POST Yanıtı İşlenir:***
- Yanıt başarılı ise (HTTP status kodu 201), JSON formatındaki yanıtı işler ve ekrana yazdırır.
- JSON verisi CSV dosyasına yazılır.
- `if response_post.status_code == 201:`
-     `data_post = response_post.json()`
-     #JSON verisini işleme ve CSV dosyasına yazma işlemleri burada yapılır.
- `else:`
-     #HTTP POST isteğinde bir hata varsa, hata kodunu ve mesajını yazdırır.

***6. HTTP DELETE İsteği Gönderilir:***
- `todo_id_to_delete = 1`
- `delete_url = f"{api_url}/{todo_id_to_delete}"`
- `response_delete = requests.delete(delete_url)`
- Bu satır, belirtilen URL'ye bir HTTP DELETE isteği gönderir. Belirli bir görevin silinmesi için kullanılır.

***7. HTTP DELETE Yanıtı İşlenir:***
- Yanıt başarılı ise (HTTP status kodu 200), ekrana başarı mesajı yazdırır ve bu mesajı CSV dosyasına yazar.
- `if response_delete.status_code == 200:`
-     #HTTP DELETE isteği başarılı ise başarı mesajını yazdırır ve CSV dosyasına yazar.
- `else:`
-     #HTTP DELETE isteğinde bir hata varsa, hata kodunu ve mesajını yazdırır.
- Bu script, bir API ile etkileşimde bulunarak alınan yanıtları işleyip, bu yanıtları CSV dosyalarına yazarak temel HTTP işlemlerini gösterir.

**Lorem Ipsum Görselleri**

![LoremIpsumDesign](https://github.com/mertmenevse/OpenSource-Lab/assets/78734566/8c26f3e4-7cc3-4c99-aa86-4de33a88b1f3)
![1_ddyz8qnOhFeFKY-_c3tleQ](https://github.com/mertmenevse/OpenSource-Lab/assets/78734566/36cf05ed-7c73-4c5b-b6e4-ae72df88a532)
![5294e6d0-53ed-4a4a-a350-7eaeab72ac93](https://github.com/mertmenevse/OpenSource-Lab/assets/78734566/f7d63aca-f8f4-459f-bff1-899ee9b3a02e)
![lorem-ipsum-nedir-1024x443](https://github.com/mertmenevse/OpenSource-Lab/assets/78734566/8f2578c5-b6a0-4fe9-825e-53e179d9da8b)

**HAVELSAN**

![Havelsan_logo svg](https://github.com/mertmenevse/OpenSource-Lab/assets/78734566/f1e37b50-6e17-4319-b3e3-f1c6e0387d4a)
