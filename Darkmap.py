#!/bin/python

# Importando las librerias que se van a ocupar 

import argparse
from colorama import Fore 
import time 
import nmap
import os

# Declarando variables de argumentos

parser = argparse.ArgumentParser(description="Darkmap")
parser.add_argument("-ip", "--target", help="Coloca el objetivo (la ip)")
args = parser.parse_args()

# Declarando una función

def darkmap():
    print(Fore.RED + """

 ######                       #     #
 #     #   ##   #####  #    # ##   ##   ##   #####
 #     #  #  #  #    # #   #  # # # #  #  #  #    #
 #     # #    # #    # ####   #  #  # #    # #    #
 #     # ###### #####  #  #   #     # ###### #####
 #     # #    # #   #  #   #  #     # #    # #
 ######  #    # #    # #    # #     # #    # #
 
 """+ Fore.RESET)
    
    # Escaneo de la IP
    ip = args.target
    nm = nmap.PortScanner()
    results = nm.scan(hosts=ip,arguments="-sT -n -Pn -T3")
    count=0

    # Mostrando resultados
    print("\nHost : %s" % ip)
    print("Estado : %s" % nm[ip].state())
    for proto in nm[ip].all_protocols():
        print("Protocolo : %s" % proto)
        print()
        lport = nm[ip][proto].keys()
        sorted(lport)
        print("\nEspera unos segundos :D...\n")
        time.sleep(2)
        for port in lport:
            print(Fore.GREEN + "Puerto : %s\tEstado : %s" % (port, nm[ip][proto][port]["state"])) 

# Declarando función principal
def main():
    if args.target:
        darkmap()
    else:
        os.system('python Darkmap.py --help')
# Declarando como principal la función main
if __name__ == '__main__':
    main()
