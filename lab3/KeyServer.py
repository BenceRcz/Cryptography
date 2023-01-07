# This .py file implements a keyserver

import socket as soc
import threading as th
import constants

# loggedInClients holds the Id-s of each clientSocket and their keys
loggedInClients = {}


# This function handles a registered clientSocket
def handle_registered_client(clientSocket, clientId, clientKey):
    isLoggedOut = False

    if clientId not in loggedInClients:
        loggedInClients[clientId] = clientKey

    while not isLoggedOut:
        msg = clientSocket.recv(2048).decode()
        if msg == 'exit':
            print('           - Client with id: ' + clientId + ' has logged out')
            isLoggedOut = True
        elif '<receivedNewId>' in msg:
            loggedInClients.pop(clientId, None)         # remove old id: key pair
            print('           - Server received new Id from clientSocket: ' + clientId)
            print('           - New Id from clientSocket: ', end='')
            msg = msg.split('<receivedNewId>')
            clientId = msg[0]
            loggedInClients[clientId] = clientKey
            print(clientId)
        elif '<receivedNewKey>' in msg:
            print('           - Server received new key from clientSocket with Id: ' + clientId)
            msg = msg.split('<receivedNewKey>')
            clientKey = msg[0]
            loggedInClients[clientId] = clientKey
            print('           - New key from clientSocket with Id: ' + clientId + ' = ' + clientKey)
    return


# This function checks if the received message is a valid Id
def msgIsValidId(receivedId):
    return receivedId.isdigit()


# This function handles a new joiner clientSocket to the server
def new_joiner(clientSocket):
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

    print('           - Server connected with new clientSocket: Id = ' + receivedId)

    handle_registered_client(clientSocket, receivedId, key)

    return


# This is the main function
def main():
    serverSocket = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
    serverSocket.bind(('', constants.KEYSERVER_PORT))
    serverSocket.listen(1)

    print('--------------------------HELLO--------------------------')
    print('------------------The server is running------------------')

    while True:
        clientSocket, address = serverSocket.accept()
        th.Thread(target=new_joiner, args=(clientSocket,)).start()

    return


if __name__ == "__main__":
    main()
