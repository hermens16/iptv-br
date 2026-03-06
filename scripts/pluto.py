import json
import urllib.request

url = "https://service-channels.clusters.pluto.tv/v1/guide?start=0&stop=24&country=BR"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())

canais = data["channels"]

with open("../listas/pluto.m3u8", "w", encoding="utf-8") as f:

    f.write("#EXTM3U\n")

    for canal in canais:

        nome = canal["name"]
        canal_id = canal["_id"]
        logo = canal.get("colorLogoPNG", {}).get("path", "")

        stream = f"https://service-stitcher.clusters.pluto.tv/stitch/hls/channel/{canal_id}/master.m3u8"

        f.write(f'#EXTINF:-1 tvg-id="{canal_id}" tvg-logo="{logo}" group-title="PLUTO",{nome}\n')
        f.write(stream + "\n")

print("Lista Pluto gerada com sucesso!")
