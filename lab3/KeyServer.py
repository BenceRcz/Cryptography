# This .py file implements a keyserver

import logging as logger
import socket as soc
import threading as th
import constants
from lab2.encryptors import solitaire
from lab2.byte_array_encryption import (generate_key_with_data_len_give)

# loggedInClients holds the Id-s of each clientSocket and their keys
loggedInClients = {}

# clientSockets holds the sockets for every logged in client
clientSockets = {}


def handle_registered_client(clientSocket, clientId, clientKey):
    """
    Handles a registered clientSocket
    """
    isLoggedOut = False

    if clientId not in loggedInClients:
        loggedInClients[clientId] = clientKey

    while not isLoggedOut:
        msg = clientSocket.recv(2048).decode()
        if msg == 'LOGOUT':
            logger.info('           - Client with id: ' + clientId + ' has logged out')
            isLoggedOut = True
            loggedInClients.pop(clientId, None)
        elif msg == 'GETCLIENTS':
            logger.info('           - Client with id requested logged in clients list: ' + clientId)
            returnMsg = ' '.join(loggedInClients.keys())
            clientSocket.send(returnMsg.encode('ascii'))
            logger.info('           - Ids sent')
        elif '<receivedNewKey>' in msg:  # when a client wants a new public key send a message in the following
            # format clientsID<receivedNewKey>newKey
            logger.info('           - Server received new key from clientSocket with Id: ' + clientId)
            msg = msg.split('<receivedNewKey>')
            clientKey = msg[0]
            loggedInClients[clientId] = clientKey
            logger.info('           - New key from clientSocket with Id: ' + clientId + ' = ' + clientKey)
        elif '<sendMessageWithLength>' in msg:
            pass
        else:
            returnMsg = 'Requested Id not logged in'
            print('           - Request denied user is not logged in')

            clientSocket.send(returnMsg.encode('ascii'))

    return


def msgIsValidId(receivedId):
    """
    Checks if the received messageToBeEncrypted is a valid Id
    """
    return receivedId.isdigit() and receivedId not in loggedInClients


def new_joiner(clientSocket):
    """
    Handles a new joiner clientSocket to the server
    """
    returnMsg = ''
    key = ''
    receivedId = 0

    print('           - Server connected with new clientSocket: Waiting for Id')
    waitForId = True
    while waitForId:
        msg = clientSocket.recv(2048).decode()
        print('           - Server received Id from clientSocket: ', end='')
        msg = msg.split('<receivedId>')
        receivedId = msg[0]
        key = msg[1]
        print(receivedId)
        if msgIsValidId(receivedId):
            print('           - Id is valid')
            waitForId = False
            returnMsg = 'OK'
        else:
            print('           - Id is invalid')
            returnMsg = 'Id is invalid'

        clientSocket.send(returnMsg.encode('ascii'))

    logger.info('           - Server connected with new clientSocket: Id = ' + receivedId)

    clientSockets[receivedId] = clientSocket
    handle_registered_client(clientSocket, receivedId, key)

    return


def main():
    """Main function"""
    serverSocket = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
    serverSocket.bind(('', constants.KEYSERVER_PORT))
    serverSocket.listen(1)

    logger.info('--------------------------HELLO--------------------------')
    logger.info('------------------The server is running------------------')

    while True:
        clientSocket, address = serverSocket.accept()
        th.Thread(target=new_joiner, args=(clientSocket,)).start()


if __name__ == "__main__":
    main()
