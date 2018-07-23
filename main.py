import sys, re
from partie_cryptage.huffman import HuffmanCode

""" Séparateur """
SLASH = "/"
WHITE_SPACE = " "

""" Constantes """
YES = ["Y","y"]
SERVER = "server"
CLIENT = "client"
IS_SERVER = False
HUFFMAN = False
RSA = False

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

def docs():
    print("Command Exemple :")
    print("\t/connect <ip> => connect to server")
    print("\t/encrypt <crypto_name> <AUTO/MAN> => select crypto program \n\t\t /!\\if is huffman them possibilitie of manuel MAN or Auto AUTO generate KEY\t /!\\")
    print("\t/msg <message> => send message without encrypt")
    print("\t/share => send key to mate \n\t\t /!\\ if nothing crypto program choose them choose one \t\t /!\\ \n\t\t /!\\ if nothing key of uncrypt set them display message in raw\t /!\\")
    print("\t/exit => exit to application")

def input_processing(enter):

    if len(enter) == 0:
        enter = " "

    if  SLASH == enter[0] and len(enter) > 1 :
        split_list = enter.split(WHITE_SPACE)
        if CONNECT == split_list[0] and not IS_SERVER:
            ip = ""
            if len(split_list) > 1:
                ip = split_list[1]
            if len(ip) == 0:
                ip = "127.0.0.1"
                # ICI SET IP ADDRESS CLIENT
                print("IP is ", ip) # A supprimer
            elif len(ip) > 0 and  valid_ip_address(ip):
                # TODO Set ip of server mate
                # ICI SET IP ADDRESS CLIENT
                print("IP is ",ip) # A supprimer
            else:
                print("Ip address is'nt valid")

        elif IS_SERVER : 
            print("You are a server, you have not access at this command !!")
            docs()
            
        if MESSAGE == split_list[0]:
            # TODO Send message in clear
            print("msg")
        if ENCRYPT == split_list[0]:
            if len(split_list) > 1:
                if split_list[1] == "HUFF" and not RSA:
                    # TODO Huffman
                    HUFFMAN = True
                    RSA = False
                    if len(split_list) > 2 and split_list[2] == "MAN": 
                        print("is huffman MAN")  # A supprimer
                        # ICI CODE HUFFMAN MANUEL
                    else:
                        print("is huffman AUTO") # A supprimer
                        # ICI CODE HUFMAN AUTO
                elif split_list[1] == "RSA" and not HUFFMAN:
                    # TODO RSA
                    HUFFMAN = False
                    RSA = True
                    print("is RSA") # A supprimer
                    # ICI RSA
                else:
                    print("No cryto program")
            else:
                HUFFMAN = False
                RSA = False
                docs()
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
        docs()

""" Début du script """
print("Are you prefer to be a server or client? ")
prefer = input("[server/client] #>")
if SERVER == prefer:
    IS_SERVER = True
elif CLIENT == prefer:
    IS_SERVER = False