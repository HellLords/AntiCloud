import socket
import sys, os

os.system("clear")

file = open("subdomain.txt")
content = file.read()
subdomain = content.splitlines()

print(f"""
\033[31m\033[01m
    _          _   _  ____ _                 _ 
   / \\   _ __ | |_(_)/ ___| | ___  _   _  __| |
  / _ \\ | '_ \\| __| | |   | |/ _ \\| | | |/ _` |\033[01m\033[0m
 / ___ \\| | | | |_| | |___| | (_) | |_| | (_| |
/_/   \\ \\_| |_|\\__|_|\\____|_|\\__/ \\__,_|\\__,_|


        .:AntiCloud:. T.ME/HellLords

Под-Доменов в базе : {str(len(subdomain))}
Введите домен для поиска поддоменов
Пример: example.com
""")
domain = input("[DOMAIN]: ")
general_ip = socket.gethostbyname(domain)
print("Сканирование доменов началось! ...")
print(f"GENERAL-IP: {general_ip}")
for i in subdomain:
	try:
		ip = socket.gethostbyname(f"{i}.{domain}")
		if ip != general_ip:
			print(f"SB: {i}.{domain} - {ip}")
	except:pass
