

1. visit: `http://www.uestc.edu.cn/` , try make an http request

2. [if don't know dns map and no local web cache] chrome do query dns for the URL, get `202.112.14.178`

3. chrome packs the http request, there are HTTP Request Head Line(`GET / HTTP/1.1`), and other Key-Value map params,like `Connection: keep-alive` means use persistent connection

4. Server(nginx) accept the request and handle it mainly URL, because I visit `/`, so nginx send it to php-fpm, and php set a session on response headers by nginx(if I, the request don't have), and return a text page

5. chrome accept the response headers, there are also http resonse head line, it tell me the http status is 200(means ok), and other Key-Value map, like `Set-Cookie` will set chrome some cookies.

6. chrome accept all Key-Value response headers, for `Content-Length` chrome know how many bytes was text entity

7. chrome interpret the text(`html/css/js` etc.)

8. make many request for the url, static resources needed, like `uestc.css`

9. all of the resources loaded and rerender and repainted DOM done. End
