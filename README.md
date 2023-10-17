# rus-edge-tts-webui
Русскоязычный интерфейс для edge tts 
Код взят у https://github.com/ycyy/edge-tts-webui и локализован мной.

![Скрин интерфейса](https://github.com/hinaichigo-fox/edge-tts-webui/blob/main/интерфейс.jpg)

# О файлах
```
Файлы интерфейс.jpg и реадми можете удалять они вам не нужны.
app.py - код нейронки.
example - записи голосов для нейронки. Без этой папки и записей в ней работать ничего не будет!!!
style.css - размеры и цвета кнопок и окон.
```

# Установка
```
Для ленивых на винде:
git clone https://github.com/hinaichigo-fox/rus-edge-tts-webui.git
Запускаете install.bat
```
```
Для всех
git clone https://github.com/hinaichigo-fox/rus-edge-tts-webui.git
cd rus-edge-tts-webui
pip install edge-tts
pip install gradio
pip install asyncio
```

# Запуск
```
Запускаете start.bat
далее в консоли появится строчка Running on local URL:  http://0.0.0.0:7860 у вас будут другие цифры. Копируем адрес и вводим в браузер. 
```
```
Если не запускали батники
cd rus-edge-tts-webui
python app.py
далее в консоли появится строчка Running on local URL:  http://0.0.0.0:7860 у вас будут другие цифры. Копируем адрес и вводим в браузер. 
```

Вроде все понятно объяснил. Всем удачи!
```
Планы на будущее: 
1.Добавить словарь
2.Добавить формат .wav на выход.
3.Автоматическое открытие браузера.
```

Спасибо https://github.com/NeuroSenko за помощь по батникам
