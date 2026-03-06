@echo off

cd C:\iptv-br\scripts\pluto_tv_scraper

node index.js

copy plutotv_br.m3u8 C:\iptv-br\listas\pluto.m3u8

cd C:\iptv-br\scripts

py juntar_listas.py

cd C:\iptv-br

git add .
git commit -m "Atualização automática IPTV"
git push origin main