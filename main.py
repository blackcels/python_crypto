import sys, re

""" Séparateur """
SLASH = "/"
WHITE_SPACE = " "

""" Constantes """
YES = ["Y","y"]
SERVER = "server"
CLIENT = "client"
IS_SERVER = False

""" Liste des commandes """
CONNECT = "/connect"
MESSAGE = "/msg"
EXIT = "/exit"
ENCRYPT = "/encrypt"
SEND_KEY = "/share"




""" Function """
def valid_ip_address(hostIP):
    pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    test = pat.match(hostIP)
    return test


""" Début du script """
print("Are you prefer to be a server or client? ")
prefer = input("[server/client] #>")
if SERVER == prefer:
    IS_SERVER = True
elif CLIENT == prefer:
    IS_SERVER = False

while True:
    enter = input("#>")

    if len(enter) == 0:
        enter =" "

    if  SLASH == enter[0]:
        split_list = enter.split(WHITE_SPACE)
        if CONNECT == split_list[0] and not IS_SERVER:
            ip = ""
            if len(split_list) > 1:
                ip = split_list[1]

            if len(ip) == 0:
                ip = "127.0.0.1"
                print("IP is ", ip) 
            elif len(ip) > 0 and  valid_ip_address(ip):
                # TODO Set ip of server mate
                print("IP is ",ip)
            else:
                print("Ip address is'nt valid")
                continue
        if MESSAGE == split_list[0]:
            # TODO Send message in clear
            print("msg")
        if ENCRYPT == split_list[0]:
            # TODO Select cryto program
            print("encrypt")
        if SEND_KEY == split_list[0]:
            # TODO Send key
            print("sendkey")
        if EXIT == split_list[0]:
            print("Are you sure to exit application ?")
            response = input("[Y/N] #>")
            if YES[0] == response or YES[1] == response:
                # TODO Stop connection
                sys.exit(0)
            else:
                continue
    else:
        print("Command Exemple :")
        print("\t/connect <ip> => connect to server")
        print("\t/msg <message> => send message without encrypt")
        print("\t/send-key => send key to mate \n\t\t /!\\ if nothing crypto program choose them choose one \t\t /!\\ \n\t\t /!\\ if nothing key of uncrypt set them display message in raw\t /!\\")
        print("\t/exit => exit to application")