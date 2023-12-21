# ui-test
Приветствую на страничке зачётного приключения ~~"калькулятор на qt наносит ответный удар"~~

Задание состоит в написании несложного приложения с графическим пользовательским интерфейсом вместе с обвязкой для его использования, тестирования, распространения. Платформа любая, язык любой, тулкит любой. 

Результат решения задачи надо сдать посредством создания (одного) Pull Request (PR) в этом репозитории. Всё связанное с решением должно лежать в директории с фамилией и инициалами (кроме `.gitmodules`, при их использовании)

На подачу PR действует жёсткий дедлайн; время на выполнение задания ограничено 2 часами (PR, коммиты поданные после XX:YY:ZZ 21.12.2023 оцениваться не будут)

Основные требования:
1. Нужно выбрать и указать в сопровождающем файле платформу, под которую реализуется проект; на этой платформе будет производиться его проверка
1. Программа должна быть переносима (её запуск не должен вызывать непреодолимых трудностей на других машинах)
1. При использовании компилируемого языка программирования, решение должно сопровождаться рецептами для сборки (cmake, meson, gradle, ...). При использовании языка программирования, экосистема которого содержит способ распространения пакетов (pip, cargo, ...), реализованная программа должна быть готова к установке посредством этого инструмента.
1. Используемый сторонний код (библиотеки, модули и т.п.) должны обеспечиваться либо через специфичный экосистеме менеджер пакетов, либо через git submodules
1. Вместе с кодом сдаётся текстовое пояснение к установке, запуску и тестированию программы (на другой машине)
1. Должен быть реализован подключаемый ключём командной строки режим логгирования всех действий пользователя в вывод терминала/консоли
1. (если используемый язык допускает наследование) программа должна содержать не менее 2 виджетов, полученных путём наследования виджетов тулкита
1. Программа должна соответствовать обозначенным в разделе с датой идее и персональному макету (последнему соответствие не строгое, слова можно и нужно свои; характер расположения элементов окна нужно сохранить)
1. Программа должна корректно (без возникновения исключений) отрабатывать любой ввод пользователя

Очевидный совет: начинайте с коротких понятных действий; тянущееся работайте почти до упора в дедлайн.

Результат проверки и решение об отметке будет принято в течение суток

## 20231221
Нужно написать специфический (см. персональный макет) калькулятор.

kostitsyina_ad [mockups/6.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/6.drawio.svg)  
gordeev_an [mockups/13.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/13.drawio.svg)  
ishmanov_tf [mockups/4.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/4.drawio.svg)  
goryagin_da [mockups/2.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/2.drawio.svg)  
sharifullin_af [mockups/10.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/10.drawio.svg)  
ragrin_dr [mockups/8.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/8.drawio.svg)  
shanturov_mv [mockups/11.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/11.drawio.svg)  
kiselev_vg [mockups/7.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/7.drawio.svg)  
buj_at [mockups/3.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/3.drawio.svg)  
zvyagina_mo [mockups/12.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/12.drawio.svg)  
polyakova_kp [mockups/1.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/1.drawio.svg)  
markushina_la [mockups/9.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/9.drawio.svg)  
vekovshinin_va [mockups/5.drawio.svg](https://github.com/alexanderustinov/ui-test/tree/main/mockups/5.drawio.svg)  
