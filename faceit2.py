import requests
from bs4 import BeautifulSoup

# URL страницы, с которой вы хотите собрать данные
url = "https://faceitstats.com/player/StreXxxx"

# Отправляем GET-запрос к странице
response = requests.get(url)

# Проверяем статус ответа, чтобы убедиться, что запрос прошел успешно
if response.status_code == 200:
    # Создаем объект BeautifulSoup для обработки HTML-кода страницы
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Найдите элементы на странице, в которых содержатся нужные вам данные
    # Используйте инструменты разработчика браузера (например, инспектор элементов) для изучения структуры страницы
    
    # Пример: извлечение никнейма игрока
    nickname_element = soup.find("span", class_="nickname")
    if nickname_element:
        nickname = nickname_element.text
        print("Никнейм игрока:", nickname)
        
    # Пример: извлечение рейтинга игрока
    rating_element = soup.find("div", class_="rating")
    if rating_element:
        rating = rating_element.text
        print("Рейтинг игрока:", rating)
        
    # Продолжайте извлекать другие нужные вам данные, следуя аналогичному подходу
else:
    print("Ошибка при запросе страницы")
