
"# testleadhit" 
Тестовое задание для leadhit.

Для запуска тестов 
1) В терминале вводим ( docker build --rm -t leadhittest -f Dockerfiletest . )
2) В терминале вводим (  docker run --rm --name mycontainer -p 80:80 leadhittest )

Для запуска приложения
1) В терминале вводим ( docker build --rm -t leadhit .  )
2) В терминале вводим ( docker run --rm --name mycontainer -p 80:80 leadhit )
3) Для тестирования приложения своими запросами рекомендую использовать приложение Postman (Ссылка на установку: https://www.postman.com/)
4) https://www.youtube.com/watch?v=7mQ3S1OJz0g - Видео как установить postman
