import requests

data = {
    "Kuldeep": "Saini"
        }


g= requests.get("https://httpbin.org/get")
p = requests.post("https://httpbin.org/post", data=data)
# print(a.text)
# url = "https://github.com/typicode/demo/blob/master/db.json"

print(g.url)
print(g.status_code)
# print(g.content)
# print(p.status_code)
print(p.reason)
# print(p.elapsed)
# print(p.is_permanent_redirect)

