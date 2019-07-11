# Python-Selenium_Behave_POM_
Тестовое задание на эмуляцию перечня действий с сайтом посредством браузера 
c использованием python-selenium, behave, паттерна page-oriented-model.

Пакет выполнен на базе ОС Debian GNU/Linux 9.9 (stretch) и пакета python 3.5.6.
Требуется установить дополнительные пакеты, перечисленные в requirements.txt:
    pip install requirements.txt

Предусмотрены два способа запуска сценариев: фреймворк BEHAVE и UNITTEST.

1. Для запуска сценариев посредством unittest необходимо запусть в командной 
строке файл test_unittest.py: 
    % python test_unittest.py
2. Для запуска сценариев посредством behave необходимо перейти в папку features/
и в командной сроке набрать команду behave:
    % behave
