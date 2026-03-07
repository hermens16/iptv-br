import urllib.request

url = "https://iptv-org.github.io/iptv/categories/entertainment.m3u"
urllib.request.urlretrieve(url, "../listas/samsung.m3u8")

print("Samsung atualizado")
