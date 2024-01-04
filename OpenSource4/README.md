## (OpenSource4) Proje 4: Docker
- Eğer Python uygulamasını Docker üzerinde çalıştırmak istiyorsanız, aşağıdaki adımları takip edebilirsiniz:
***1. İlk olarak, projenizin bulunduğu dizine gidin ve bir `Dockerfile` oluşturun.***
- #Use the official Python image as the base image
- `FROM python:3.8`

- #Set the working directory in the container
- `WORKDIR /app`

- #Copy the current directory contents into the container
- `COPY . /app`

- #Install any needed packages specified in requirements.txt
- `RUN pip install -r requirements.txt`

- #Define environment variable
- `ENV NAME World`

- #Run app.py when the container launches
- `CMD ["python", "app.py"]`

***2. Ardından, Docker imajınızı oluşturun:***
- `docker build -t my-python-app .`
- Bu komut, bulunduğunuz dizindeki Dockerfile kullanılarak `my-python-app` adında bir Docker imajı oluşturur.

***3. Docker imajını çalıştırın:***
- `docker run my-python-app`
- Bu adımları takip ederek, Python uygulamanızı Docker üzerinde çalıştırabilirsiniz. Ayrıca, projenizin bağımlılıklarını belirttiğiniz bir `requirements.txt` dosyası varsa, bu dosyayı Dockerfile içinde kullanabilir ve bağımlılıkların Docker imajına yüklenmesini sağlayabilirsiniz.
![what-is-docker](https://github.com/mertmenevse/OpenSource-Lab/assets/78734566/0d5f32fb-33b1-44a6-ac21-ee1bb3097a2b)
