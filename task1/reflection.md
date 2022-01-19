Моё решение смесь процедурного/функционального и ООП подхода. 
1. ОПП часть. Есть "главный" класс Robot - это модель реального робота он умеет выполнять все команды, так же инкапсулирует его состояние. Так же есть 2 класса, которые умеют работать с координатами и углами.
2. Функциональный подход. Эта часть состоит их набора функций и отвечает за парсинг входного файла. Главная функция считывает построчно входной файл, разбивает строку на токены, получает нужную функцию для работы с командой и вызывает её. Функции для работы с командой преобразовывают параметры в нужный формат и вызывают нужную функцию робота.

Данный подход считаю оптимальным для данной задачи. Можно улучшить программу инкапсулировав парсинг в отдельный класс - это упростит дальнейшие модификации, если входная программа начнет значительно усложнятся.