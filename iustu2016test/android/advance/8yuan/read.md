
[reference1](https://github.com/loadfield/go-music/blob/master/controllers/netease-music.go)

[reference2](https://github.com/yanunon/NeteaseCloudMusic/wiki/%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90API%E5%88%86%E6%9E%90)


1. search in music.163.com: `Skyfall`
2. select the song needed, current url is  `http://music.163.com/#/song?id=29732222`, so get id is `29732222`
3. `curl "http://music.163.com/api/song/detail/?id=29732222&ids=%5B29732222%5D"` to get details
4. Get Response JSON: `songs->hMusic->dfsId` is `1364493976539078`
5. use follow python code to calc encrypt string
6. download `GET http://m1.music.126.net/[encrypted_song_id]/[song_dfsId].mp3`, the `[encrypted_song_id]` got from step 5,  `[song_dfsId]` is `dfsId`. The final url is
`http://p1.music.126.net/3QK08uLIA_HLeqwPaEyI9w==/1364493976539078.mp3`

```python
import md5

def encrypted_id(id):
    byte1 = bytearray('3go8&$8*3*3h0k(2)2')
    byte2 = bytearray(id)
    byte1_len = len(byte1)
    for i in xrange(len(byte2)):
        byte2[i] = byte2[i]^byte1[i%byte1_len]
    m = md5.new()
    m.update(byte2)
    result = m.digest().encode('base64')[:-1]
    result = result.replace('/', '_')
    result = result.replace('+', '-')
    return result
    # encrypted_id(1364493976539078) == 3QK08uLIA_HLeqwPaEyI9w==`
```



```bash
1364493976539078.mp3  100%[=========================>]   9.24M  3.86MB/s    in 2.4s
```
