# This .py file implements client_1


import constants
import socket as soc
from MerkleHellman import *
# from MerkleHellman import (generate_private_key, create_public_key, encrypt_mh, decrypt_mh)
import threading as th


# Client1s private key
privateKey = []
publicKey = []


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
    print('--           Send: send message to someone          --')
    print('------------------------------------------------------')
    return


# This function handles the communication with the KeyServer
def communicate_with_server(serverSocket, clientId):
    global publicKey
    global privateKey
    waitForResp = False
    isKey = False
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
            print('          - Your Key is: ' + ','.join(str(v) for v in publicKey))
        elif userInput == 'ChangeKey':
            privateKey = generate_private_key(8)
            publicKey = create_public_key(privateKey)
            msg = str(clientId) + '<receivedNewKey>' + ','.join(str(v) for v in publicKey)
        elif userInput == 'Logout':
            msg = 'LOGOUT'
        elif userInput == 'LoggedIn':
            msg = 'GETCLIENTS'
            waitForResp = True
            isKey = True
        elif userInput == 'Send':
            msgTo = input('Add the user id of the person you want to send a message to: ')
            messageToUser = input('Please add your message: ')
            waitForResp = True
            msg = str(msgTo) + '<sendMessageWithLength>' + str(len(messageToUser))
            serverSocket.send(msg.encode('ascii'))

        if msg != '':
            serverSocket.send(msg.encode('ascii'))
            if waitForResp:
                msg = serverSocket.recv(2048).decode()
                if not isKey:
                    print('          - Logged in clients: ' + msg)
                else:
                    # TODO DECRYPT KEY
                    print('          - Received Key: ' + str(receivedMsg))
                    isKey = False
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
        msg = str(clientId) + '<receivedId>' + ','.join(str(v) for v in publicKey)
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
    global privateKey
    global publicKey
    privateKey = generate_private_key(8)
    publicKey = create_public_key(privateKey)

    clientId = constants.INITIAL_CLIENT_ID

    serverSocket = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
    serverSocket.connect(('localhost', constants.KEYSERVER_PORT))

    register_to_server(serverSocket, clientId)

    return


if __name__ == '__main__':
    main()
