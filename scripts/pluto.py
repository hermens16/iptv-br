import json
import urllib.request

url = "https://api.pluto.tv/v2/channels?start=0&stop=1000&region=BR&deviceType=web"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://pluto.tv/",
}

req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())

with open("../listas/pluto.m3u8", "w", encoding="utf-8") as f:

    f.write("#EXTM3U\n")

    for canal in data:

        nome = canal["name"]
        logo = canal.get("solidLogoPNG", {}).get("path", "")
        canal_id = canal["_id"]

        stream = f"https://service-stitcher.clusters.pluto.tv/stitch/hls/channel/{canal_id}/master.m3u8"

        f.write(f'#EXTINF:-1 tvg-id="{canal_id}" tvg-logo="{logo}" group-title="PLUTO",{nome}\n')
        f.write(stream + "\n")

print("Lista Pluto atualizada")
