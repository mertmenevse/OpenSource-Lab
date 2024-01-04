## (OpenSource3) Proje 3: gunicorn ve nginx servislerinin entegre edilmesi
- Uygulamanın servis haline getirilmesi
- Gunicorn ve Nginx'i birlikte kullanmak, Python uygulamanızı daha verimli ve güvenli bir şekilde dağıtmak için yaygın bir yaklaşımdır. Gunicorn, Python uygulamanızı çalıştırmak için kullanılan bir WSGI sunucusudur, Nginx ise bu uygulamaya gelen HTTP isteklerini yöneten bir web sunucusudur.

- İşte Gunicorn ve Nginx'in birlikte kullanılması için temel adımlar:

***1. Gunicorn Kurulumu:***
- İlk olarak, Gunicorn'u projenize ekleyin. Projede kullanılan sanal ortamda şu komutu kullanabilirsiniz:
- `pip install gunicorn`

***2.Gunicorn ile Uygulamayı Çalıştırma:***
- Python uygulamanızı Gunicorn ile başlatmak için terminalde şu komutu kullanabilirsiniz:
- `gunicorn -w 4 -b 0.0.0.0:8000 app:app`
- Bu komut, uygulamanızı app adlı modüldeki app adlı nesne üzerinden çalıştıracaktır. -w parametresi, çalışan işçi (worker) sayısını belirtir.

***3. Nginx Kurulumu:***
- Nginx'i kurmak için sisteminize uygun bir komut kullanabilirsiniz. Örneğin, Ubuntu için:
- `sudo apt-get update`
- `sudo apt-get install nginx`

***4. Nginx Konfigürasyonu:***
Nginx konfigürasyon dosyanızı açın ve aşağıdaki gibi düzenleyin:
- `server {
    listen 80;
    server_name your_domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static {
        alias /path/to/your/static/folder;
    }

    location /media {
        alias /path/to/your/media/folder;
    }}`
- Bu konfigürasyon, Nginx'in gelen HTTP isteklerini Gunicorn üzerinde çalışan Python uygulamasına yönlendirmesini sağlar. proxy_pass kısmında Gunicorn'un çalıştığı adres ve portu belirtmelisiniz.

***5. Nginx'i Yeniden Başlatma:***
- Konfigürasyonunuzu değiştirdikten sonra Nginx'i yeniden başlatmalısınız:
- `sudo service nginx restart`
- Bu adımları takip ederek, Gunicorn ve Nginx'i bir arada kullanabilir ve Python uygulamanızı daha etkili bir şekilde dağıtabilirsiniz. Unutmayın ki, gerçek bir uygulama için bu adımları güvenlik önlemleri ve performans iyileştirmeleriyle birleştirmeniz önemlidir.
![Screenshot-from-2022-06-07-13-54-06](https://github.com/mertmenevse/OpenSource-Lab/assets/78734566/788f6f9c-6ec3-4a69-b079-2f2a37f0245e)
