# Инструкция

главный файл проекта -- main.py

Его можно запустить либо напрямую, тогда надо будет вручную ввести путь в программе на целевом языке, путь к .json-файлу с описанием карты и робота, аргументы (число 0, если выполняется абстрактный код без участия робота, и любое значение иначе) и имя файла для записи результата.

Либо при запуске перенаправить stdin в файл, где эти 4 аргумента будут заранее записаны на отдельных строках

В качестве результата будут записаны состояние карты и робота по завершению программы, а также лог самого робота -- как он перемещался по карте.

Поиск выхода из лабиринта -- файл pathfinding
Примеры ввода -- файлы map.json, map1.json и т.д.
Примеры вывода -- файлы output1.txt, output2.txt и т.д.

