import requests
import csv

# API endpoint URL'si
api_url = "https://jsonplaceholder.typicode.com/todos"

# GET isteği gönderme
response_get = requests.get(api_url)

# Yanıtı kontrol etme
if response_get.status_code == 200:
    # Yanıt JSON formatında ise verileri işleme
    data_get = response_get.json()
    print("GET İsteği Yanıtı:", data_get)

    # CSV dosyasına yazma
    with open("get_response.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data_get[0].keys())
        writer.writeheader()
        writer.writerows(data_get)
    print("GET İsteği Yanıtı CSV dosyasına yazıldı.")
else:
    print("GET İsteği Hata Kodu:", response_get.status_code)
    print("GET İsteği Hata Mesajı:", response_get.text)

# POST isteği gönderme
new_todo = {"userId": 1, "title": "New Todo", "completed": False}
response_post = requests.post(api_url, json=new_todo)

# Yanıtı kontrol etme
if response_post.status_code == 201:
    # Yanıt JSON formatında ise verileri işleme
    data_post = response_post.json()
    print("POST İsteği Yanıtı:", data_post)

    # CSV dosyasına yazma
    with open("post_response.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data_post.keys())
        writer.writeheader()
        writer.writerow(data_post)
    print("POST İsteği Yanıtı CSV dosyasına yazıldı.")
else:
    print("POST İsteği Hata Kodu:", response_post.status_code)
    print("POST İsteği Hata Mesajı:", response_post.text)

# DELETE isteği gönderme
todo_id_to_delete = 1
delete_url = f"{api_url}/{todo_id_to_delete}"
response_delete = requests.delete(delete_url)

# Yanıtı kontrol etme
if response_delete.status_code == 200:
    print("DELETE İsteği Başarıyla Gerçekleştirildi.")

    # CSV dosyasına yazma
    with open("delete_response.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["DELETE İsteği Başarıyla Gerçekleştirildi"])
    print("DELETE İsteği Yanıtı CSV dosyasına yazıldı.")
else:
    print("DELETE İsteği Hata Kodu:", response_delete.status_code)
    print("DELETE İsteği Hata Mesajı:", response_delete.text)
