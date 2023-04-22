# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](#Описание-проекта)  
[2. Какой кейс решаем?](#Какой-кейс-решаем)  
[3. Краткая информация о данных](#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](#Этапы-работы-над-проектом)  
[5. Результат](#Результат)    
[6. Выводы](#Выводы) 

__

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток, с помощью самого же компьютера. 
Это учебное задание от платформы SkillFactory.

:arrow_up:[к оглавлению](#Оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### Краткая информация о данных

:arrow_up:[к оглавлению](#Оглавление)


### Этапы работы над проектом  
1. Ознакомление с материалом
2. Освоение навыков работы с GitHub, благодаря помощи старших товарищей произошло стремительно, но поскольку эти навыки приобретались за несколько месяцев до начала работы с основным заданием проекта, пришлось заново их восстанавливать в пямяти, и честно признаться пока до конца разобраться не удалось. 
3. Поиск решения. Поскольку сама задача довольно проста, и материал для её решения изначально был представлен почти в полном объёме, от меня требовалось только принципиальное решение задачи быстроты поиска загаданного числа моим алгоритмом. Решение было найдено случайно, благодаря подсказке лектора Олега Булыгина, который в конце одного из своих вэбинаров посоветовал почитать книжку "Грокаем Алгоритмы" Адитьи Бхаргавы, в которой я обнаружил решение мой задачи. 
4. Решением оказался бинарный поиск, который Адитья приводит самым первым для примера алгоритмов. Немного повозившись с переменными для цикла whil (сначала я разместил их внутри цикла, из-за чего перед каждым новым шагом они возвращались к изначалььным значениям) мне удалось добиться удовлетворительной скорости поиска загаданного числа. 
5. Последним этапом стала подгрузка всех материалов на GitHub, и проверка кода на соответсnвие стандарту PEP8 

:arrow_up:[к оглавлению](#Оглавление)


### Результаты:  

Алгоритм поиска угадывает задуманное число в среднем за 8 попыток, при 1000 повторений. Это удовлетворительный результат. 

:arrow_up:[к оглавлению](#Оглавление)


### Выводы:  

1. Не стесняться просить о помощи.
2. Использовать все доступные инструменты и материалы.
3. Не пренебрегать советами учителей, лекторов и наставников.
4. Не откладывать дела в долгий ящик, так как память - вещь не совершенная
5. Никогда не сдаваться! 

:arrow_up:[к оглавлению](#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами.