# This .py file implements client_1


import constants
import logging as logger
import socket as soc
from MerkleHellman import *
# from MerkleHellman import (generate_private_key, create_public_key, encrypt_mh, decrypt_mh)


# Client1s private key
privateKey = []
publicKey = []


def print_usage():
    """
    Prints commands available for the user
    """
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


def communicate_with_server(serverSocket, clientId):
    """
    Handles the communication with the KeyServer
    """
    global publicKey
    global privateKey
    waitForResp = False
    isKey = False
    print_usage()
    msg = ''
    receivedMsg = ''

    while True:
        userInput = input('Waiting for command ')
        userInput = userInput.upper()
        if userInput == 'EXIT':
            break
        elif userInput == 'HELP':
            print_usage()
        elif userInput == 'VIEWID':
            print('          - Your Id is: ' + str(clientId))
        elif userInput == 'VIEWKEY':
            print('          - Your Key is: ' + ','.join(str(v) for v in publicKey))
        elif userInput == 'CHANGEKEY':
            privateKey = generate_private_key(8)
            publicKey = create_public_key(privateKey)
            msg = str(clientId) + '<receivedNewKey>' + ','.join(str(v) for v in publicKey)
        elif userInput == 'LOGOUT':
            msg = 'LOGOUT'
        elif userInput == 'LOGGEDIN':
            msg = 'GETCLIENTS'
            waitForResp = True
            isKey = True
        elif userInput == 'SEND':
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


def register_to_server(serverSocket, clientId):
    """
    Handles the registration of the client into the KeyServer
    """
    global publicKey
    logger.info('         - Connected with key server')
    isLoggedIn = False
    msg = ''
    receivedMsg = ''
    
    while not isLoggedIn:
        msg = str(clientId) + '<receivedId>' + ','.join(str(v) for v in publicKey)
        logger.info('         - Sending messageToBeEncrypted: ' + msg)
        serverSocket.send(msg.encode('ascii'))
        receivedMsg = serverSocket.recv(2048).decode()
        if receivedMsg == 'OK':
            isLoggedIn = True
        elif receivedMsg == "REJECTED":
            clientId = clientId + 1
        else:
            logger.error("SERVER ERROR! could not log in")

    logger.info('         - Successfully registered with following Id: ' + str(clientId))

    communicate_with_server(serverSocket, clientId)

    return


def generate_keys():
    """
    Generate private and public key for the client
    """
    global privateKey
    global publicKey
    privateKey = generate_private_key(8)
    publicKey = create_public_key(privateKey)

    return


def init_client():
    """
    Initialize client id, connect to server and generate client keys
    """
    generate_keys()
    clientId = constants.INITIAL_CLIENT_ID
    serverSocket = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
    serverSocket.connect(('localhost', constants.KEYSERVER_PORT))

    return clientId, serverSocket


def main():
    serverSocket, clientId = init_client()
    register_to_server(serverSocket, clientId)

    return


if __name__ == '__main__':
    main()
