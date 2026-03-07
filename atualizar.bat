@echo off

cd C:\Users\User\Dev\iptv-br\scripts\pluto_tv_scraper
node index.js
copy plutotv_br.m3u8 C:\Users\User\Dev\iptv-br\listas\pluto.m3u8

cd C:\iptv-br\scripts

py plex.py
py samsung.py
py runtime.py

py juntar_listas.py

cd C:\Users\User\Dev\iptv-br

git add .
git commit -m "Atualização automática IPTV"
git push origin main