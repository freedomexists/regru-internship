HTTP - протокол передачи гипертекста.
Описывает процесс общения клиента и сервера. Общение проиходит по средствам запросов и ответов на них.
Без использования дополнительных технологий HTTP не сохраняет промежуточных состояний "диолога". Используется повсеместно в WEB
для получения информации с веб-сайтов.

Request URL: https://app.reg.academy/admin - URL-адрес целевого API/сайта (домен app.reg.academy, адрес внутри домена /admin) \
Request Method: GET - метод запроса (мы хотим что-то получить)\
Status Code: 200 OK - статус запроса (не понял как он попал в запрос, обычно его шлет сервер в ответе) \
Remote Address: 89.108.89.128:443 - ip:port адресата \
Referrer Policy: no-referrer-when-downgrade - этот флаг не позволит браузеру сообщить целевому серверу откуда мы пришли, если сайт-назначение не секьюрен (не HTTPS). В нашем случае бесполезен, видимо. \
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,  - тут мы видим список MIME-типов контента страницы, которые мы готовы принять в ответ на этот запрос. Мы готовы на HTML, XHTML, XML (с коэф-м предпочтения 0,9), WebP, APNG. \
Accept-Encoding: gzip, deflate, br - допустимые форматы сжатия \
Accept-Language: en-US,en;q=0.9,ru;q=0.8 - допустимые языки с коэфициентами предпочтения (US-En предпочитаем больше, чем en, а en больше, чем ru)\
Cache-Control: no-cache -принуждает кэш отправлять запрос на исходный сервер каждый раз для валидации, прежде чем выдать кэшированную копию. \
Connection: keep-alive - указания такого статуса заголовка позволяет сообщить, что мы готовы на многократные запросы с установленным соединением \
Cookie: connect.sid=s123123123E - собственно передача куки-айди для аутентификации, например \
Host: app.reg.academy - домен целевого ресурса \
Pragma: no-cache - то же что и Cache-Control, но для старой версии протокола (1.0) \
Referer: https://app.reg.academy/admin/schools - адрес откуда мы перешли по ссылке \
Upgrade-Insecure-Requests: 1 - сообщаем серверу, что мы хотим HTTPS, если возможно \
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36 - информация о нашей системе \


Request URL: https://app.reg.academy/admin/schools/ \
Request Method: PUT - сообщаем, что мы хотим что-то загрузить на целевой URL \
Status Code: 200 OK \
Remote Address: 89.108.89.128:443 \
Referrer Policy: no-referrer-when-downgrade \
Accept: application/json, text/plain, \
Accept-Encoding: gzip, deflate, br\
Accept-Language: en-US,en;q=0.9,ru;q=0.8\
Cache-Control: no-cache\\
Connection: keep-alive\\
Content-Length: 86 - заголовок сущности загружаемого объекта. отображает кол-во символов загружаемого объекта \
Content-Type: application/json;charset=UTF-8 - Формат и способ представления сущности \
Cookie: connect.sid=s%s123123123E - (s% - странная фигня, неведомая интернету)\
csrf-token: bsARqevf-Uc1JBrBCxTuOPVnRgvL2gSEtcys - токен, для подтверждения что загружаемые данные загружаются в той же сессии и с того же устройства, с которого произошел логин \
Host: app.reg.academy \
Origin: https://app.reg.academy - адрес откуда будет производится загрузка \
Pragma: no-cache \
Referer: https://app.reg.academy/admin/schools \
Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36 \
X-Requested-With: XMLHttpRequest - сообщаем, что запросы шлем и принимаем ответы используя AJAX \