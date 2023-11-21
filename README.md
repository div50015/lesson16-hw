# qa_guru_python_8_16_pytest1

----
### Pytest. Применение фикстур и маркировки:

Реализован автотест для github.com, который: 
* заход на страницу 
* поиск кнопки Sign In 
* нажатие на нее 

Пропуск сценария мобильного теста  если соотношение сторон десктопное (и наоборот):
* test_if_skip.py

Переопределение параметра с помощью indirect: 
* test_parameterized.py

Применение разных фикстур для каждого (десктопный и мобильный размер) теста:
* test_with_fixtures.py