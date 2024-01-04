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

