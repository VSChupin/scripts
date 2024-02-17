import os
import time
import zipfile

folder_path = '/home/vladimir/Downloads'

while True:
    files = os.listdir(folder_path)
    for file in files:
        if file.endswith('.zip') or file.endswith('.rar') or file.endswith('.7z'):
            file_path = os.path.join(folder_path, file)
            try:
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(zip_ref.filename.split('.')[0])
                    os.remove(file_path)
                    print(f"Архив {file} успешно разархивирован и удален")
            except zipfile.BadZipFile:
                print(f"Архив {file} еще не скачан или поврежден. Ждем..")
            except zipfile.LargeZipFile:
                print(f"Архив {file} слишком большой для разархивации")
    
    time.sleep(5)  # Проверка папки каждые 10 секунд

