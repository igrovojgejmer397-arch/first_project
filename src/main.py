import os
from dotenv import load_dotenv

def print_author():
    # Загружаем переменные из .env файла
    load_dotenv()
    
    # Читаем значение AUTHOR из переменных окружения
    author = os.getenv('AUTHOR')
    
    # Проверяем, что переменная найдена
    if author:
        print(f"Автор проекта: {author}")
    else:
        print("Автор не указан в файле .env")

# Вызываем функцию
if __name__ == "__main__":
    print_author()
