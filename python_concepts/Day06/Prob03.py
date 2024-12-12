
import re
url= "www.google.com/:<search?%/%&new%23movies-2024%~!/%region?]/$%~fetched&/-^$result &-/@%#=res.aspx"

while(re.search(r"/", url)):
    res = re.search(r"/", url)
    print(url[:res.start()])
    url = url[res.end():]
    print("-" * 60)

print(url)
