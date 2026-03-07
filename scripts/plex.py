import urllib.request

url = "https://iptv-org.github.io/iptv/countries/br.m3u"
urllib.request.urlretrieve(url, "../listas/plex.m3u8")

print("Canais Brasil atualizados")
