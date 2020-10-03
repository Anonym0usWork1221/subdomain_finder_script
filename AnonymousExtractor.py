import requests
import time
import urllib3
import os
import sys
#Version
version = 1.0
#Show
def anonymousSH():
    print("\t\t███████████████████████████████")
    print("\t\t████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬████")
    print("\t\t██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██")
    print("\t\t█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬█")
    print("\t\t█╬╬╬███████╬╬╬╬╬╬╬╬╬███████╬╬╬█")
    print("\t\t█╬╬██╬╬╬╬███╬╬╬╬╬╬╬███╬╬╬╬██╬╬█")
    print("\t\t█╬██╬╬╬╬╬╬╬██╬╬╬╬╬██╬╬╬╬╬╬╬██╬█")
    print("\t\t█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬█")
    print("\t\t█╬╬╬╬█████╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬█")
    print("\t\t█╬╬█████████╬╬╬╬╬╬╬█████████╬╬█")
    print("\t\t█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬█")
    print("\t\t█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█")
    print("\t\t█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█")
    print("\t\t█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█")
    print("\t\t█╬╬╬▓▓▓▓╬╬╬╬╬╬╬█╬╬╬╬╬╬╬▓▓▓▓╬╬╬█")
    print("\t\t█╬╬▓▓▓▓▓▓╬╬█╬╬╬█╬╬╬█╬╬▓▓▓▓▓▓╬╬█")
    print("\t\t█╬╬╬▓▓▓▓╬╬██╬╬╬█╬╬╬██╬╬▓▓▓▓╬╬╬█")
    print("\t\t█╬╬╬╬╬╬╬╬██╬╬╬╬█╬╬╬╬██╬╬╬╬╬╬╬╬█")
    print("\t\t█╬╬╬╬╬████╬╬╬╬███╬╬╬╬████╬╬╬╬╬█")
    print("\t\t█╬╬╬╬╬╬╬╬╬╬╬╬╬███╬╬╬╬╬╬╬╬╬╬╬╬╬█")
    print("\t\t██╬╬█╬╬╬╬╬╬╬╬█████╬╬╬╬╬╬╬╬█╬╬██")
    print("\t\t██╬╬██╬╬╬╬╬╬███████╬╬╬╬╬╬██╬╬██")
    print("\t\t██╬╬▓███╬╬╬████╬████╬╬╬███▓╬╬██")
    print("\t\t███╬╬▓▓███████╬╬╬███████▓▓╬╬███")
    print("\t\t███╬╬╬╬▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬███")
    print("\t\t████╬╬╬╬╬╬╬╬╬╬███╬╬╬╬╬╬╬╬╬╬████")
    print("\t\t█████╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬█████")
    print("\t\t██████╬╬╬╬╬╬╬╬███╬╬╬╬╬╬╬╬██████")
    print("\t\t███████╬╬╬╬╬╬╬███╬╬╬╬╬╬╬███████")
    print("\t\t████████╬╬╬╬╬╬███╬╬╬╬╬╬████████")
    print("\t\t█████████╬╬╬╬╬███╬╬╬╬╬█████████")
    print("\t\t███████████╬╬╬╬█╬╬╬╬███████████")
    print("\t\t███████████████████████████████")
    print("\n")
    print("░█████╗░███╗░░██╗░█████╗░███╗░░██╗██╗░░░██╗███╗░░░███╗░█████╗░██╗░░░██╗░██████╗")
    print("██╔══██╗████╗░██║██╔══██╗████╗░██║╚██╗░██╔╝████╗░████║██╔══██╗██║░░░██║██╔════╝")
    print("███████║██╔██╗██║██║░░██║██╔██╗██║░╚████╔╝░██╔████╔██║██║░░██║██║░░░██║╚█████╗░")
    print("██╔══██║██║╚████║██║░░██║██║╚████║░░╚██╔╝░░██║╚██╔╝██║██║░░██║██║░░░██║░╚═══██╗")
    print("██║░░██║██║░╚███║╚█████╔╝██║░╚███║░░░██║░░░██║░╚═╝░██║╚█████╔╝╚██████╔╝██████╔╝")
    print("╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░░░░╚═╝░╚════╝░░╚═════╝░╚═════╝░")
    print("\n")
    print("███████╗██╗░░██╗████████╗██████╗░░█████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗")
    print("██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║")
    print("█████╗░░░╚███╔╝░░░░██║░░░██████╔╝███████║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║")
    print("██╔══╝░░░██╔██╗░░░░██║░░░██╔══██╗██╔══██║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║")
    print("███████╗██╔╝╚██╗░░░██║░░░██║░░██║██║░░██║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║")
    print("╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝")
    print("\n")
    print(f"VERSION : {version}")
    print('\n')
    print("▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄")
    print("░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ")
    print('\n\n')
    time.sleep(1)
def parse_url(url):
    try:
        host = urllib3.util.url.parse_url(url).host
    except Exception as e:
        print('[*] Invalid domain, type valid One')
        sys.exit(1)
    return host

def Make_file(subdomain, output_file):
    with open(output_file, 'a') as ss:
        ss.write(subdomain + ",0.0.0.1"+ '\n')
        ss.close()
def main():
    anonymousSH()
    subdomains = []    
    attacks = input("[*] How Much Domains You want to put: ")
    domains = []
    d = 1
    if attacks.isnumeric():
        attacks_int = int(attacks)
        while d < attacks_int +1:
            gets = input("[*] Input Your " + str(d) + " Domain : ")
            domains.append(gets)
            d +=1       
    else:
        sys.exit(1)
    output = str(input("[*] Enter File Name to save: "))
    print("\n")
    print("░█▀▀█ █▀▀ ▀▀█▀▀ █──█ █▀▀ █▀▀█ ─▀─ █▀▀▄ █▀▀▀ 　 ▀█▀ █▀▀▄ █▀▀ █▀▀█ ─ ─ ─ ")
    print("░█─▄▄ █▀▀ ──█── █▀▀█ █▀▀ █▄▄▀ ▀█▀ █──█ █─▀█ 　 ░█─ █──█ █▀▀ █──█ ▄ ▄ ▄  ")
    print("░█▄▄█ ▀▀▀ ──▀── ▀──▀ ▀▀▀ ▀─▀▀ ▀▀▀ ▀──▀ ▀▀▀▀ 　 ▄█▄ ▀──▀ ▀── ▀▀▀▀ █ █ █")
    print("\n\n")
    for t in domains:
        target = parse_url(t)
        try:
            request = requests.get(f'https://crt.sh/?q=%.{target}&output=json')
        except:
            print("[*] ####################   CONNECTION FAILED PLEASE CHECK YOUR NETWORK CONNECTION     ###################  [*]")
            sys.exit(1)
        if request.status_code != 200:
            print('[*] Information not Available For that Target!')
            sys.exit(1)
        for (key,value) in enumerate(request.json()):
            subdomains.append(value['name_value'])
        print(f"\n[!] **************** TARGET ATTACK : {target} *********************** \n")
        Tries = sorted(set(subdomains))
    for w in Tries:
        print(f'{w}\n')
        if output is not None:
            Make_file(w, output)
    print("\n\n[!!] DONE EXTRACTION SUBSCRIBE TO MY CHANNEL FOR MORE HACKING TOOLS...........\n")
    try:
        os.startfile(output)
    except:
        pass
    print("\t─█▀▀█ █▀▀▄ █▀▀█ █▀▀▄ █▀▀█ █──█ █▀▄▀█ █▀▀█ █──█ █▀▀")
    print("\t░█▄▄█ █──█ █──█ █──█ █──█ █▄▄█ █─▀─█ █──█ █──█ ▀▀█")
    print("\t░█─░█ ▀──▀ ▀▀▀▀ ▀──▀ ▀▀▀▀ ▄▄▄█ ▀───▀ ▀▀▀▀ ─▀▀▀ ▀▀▀")
    print("\n\n")     
if __name__=='__main__':
    main()