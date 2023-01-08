# This .py file implements client_1


import constants
import socket as soc
from MerkleHellman import *
# from MerkleHellman import (generate_private_key, create_public_key, encrypt_mh, decrypt_mh)
import threading as th


# Client1s private key
privateKey = generate_private_key(8)
publicKey = create_public_key(privateKey)


# This function prints the commands available for the KeyServer
def print_usage():
    print('------------------KEYSERVER COMMANDS------------------')
    print('--           Help: prints usage again               --')
    print('--           Exit: Stops the app                    --')
    print('--           ViewID: returns your id                --')
    print('--           LoggedIn: returns logged in Ids        --')
    print('--           ViewKey: returns your key              --')
    print('--           ChangeKey: changes your key            --')
    print('--        LogOut: Logs out of the KeyServer         --')
    print('------------------------------------------------------')
    return


# This function handles the communication with the KeyServer
def communicate_with_server(serverSocket, clientId):
    global publicKey
    waitForResp = False
    print_usage()
    msg = ''
    receivedMsg = ''

    while True:
        userInput = input('Waiting for command ')
        if userInput == 'Exit':
            break
        elif userInput == 'Help':
            print_usage()
        elif userInput == 'ViewID':
            print('          - Your Id is: ' + str(clientId))
        elif userInput == 'ViewKey':
            print('          - Your Key is: ' + publicKey)
        elif userInput == 'ChangeKey':
            newKey = 'new key'                                          # TO BE IMPLEMENTED
            msg = newKey
        elif userInput == 'Logout':
            msg = 'LOGOUT'
        elif userInput == 'LoggedIn':
            msg = 'GETCLIENTS'
            waitForResp = True
        elif msg != '':
            serverSocket.send(msg.encode('ascii'))
            if waitForResp:
                msg = serverSocket.recv(2048).decode()
                print('          - Logged in clients: ' + msg)
                waitForResp = False
            msg = ''

    return


# This function handles the registration of the client into the KeyServer
def register_to_server(serverSocket, clientId):
    global publicKey
    print('         - Connected with key server')
    isLoggedIn = False
    msg = ''
    receivedMsg = ''
    
    while not isLoggedIn:
        msg = str(clientId) + '<receivedId>' + publicKey
        print('         - Sending messageToBeEncrypted: ' + msg)
        serverSocket.send(msg.encode('ascii'))
        receivedMsg = serverSocket.recv(2048).decode()
        if receivedMsg == 'OK':
            isLoggedIn = True
        else:
            clientId = clientId + 1

    print('         - Successfully registered with following Id: ' + str(clientId))

    communicate_with_server(serverSocket, clientId)

    return


def main():
    clientId = constants.INITIAL_CLIENT_ID

    serverSocket = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
    serverSocket.connect(('localhost', constants.KEYSERVER_PORT))

    register_to_server(serverSocket, clientId)

    return


if __name__ == '__main__':
    main()
