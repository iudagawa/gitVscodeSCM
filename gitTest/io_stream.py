"""
 Ver1.0
"""
import io
import requests
import zipfile

#ストリング形式　
f = io.StringIO()
f.write('abcd')
f.seek(0)
print(f.read()) #abcd

#バイナリ形式　
f = io.BytesIO()
f.write(b'abcd')
f.seek(0)
print(f.read()) #b'abcd'

# URLからZipファイルをダウンロードしメモリに展開する
# 含まれているファイルを調べる
# 表示可能な特定のファイルをprint()する
url = ('https://www.python.org/ftp/python/3.9.7/'
       'python-3.9.7-embed-amd64.zip')
f = io.BytesIO()
r = requests.get(url)
f.write( r.content )
with zipfile.ZipFile(f) as z:
    fl = z.filelist
    i=1
    for fname in fl:
        print( 'No{}:{}'.format(i,fname) )
        i+=1
    with z.open('LICENSE.txt') as x:
        print(x.read().decode())
