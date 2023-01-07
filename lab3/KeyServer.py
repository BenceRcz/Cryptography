# This .py file implements a keyserver

import socket as soc
import threading as th

# loggedInClients holds the Id-s of each client and their keys
loggedInClients = {}


# This function handles a registered client
def handle_registered_client(client, clientId, clientKey):
    isLoggedOut = False

    if clientId not in loggedInClients:
        loggedInClients[clientId] = clientKey

    while not isLoggedOut:
        msg = client.recv(2048).decode()
        if msg == 'exit':
            print('           - Client with id: ' + clientId + ' has logged out')
            isLoggedOut = True
        elif '<receivedNewId>' in msg:
            loggedInClients.pop(clientId, None)         # remove old id: key pair
            print('           - Server received new Id from client: ' + clientId)
            print('           - New Id from client: ', end='')
            msg.split('<receivedNewId>')
            clientId = msg[0]
            loggedInClients[clientId] = clientKey
            print(clientId)
        elif '<receivedNewKey>' in msg:
            print('           - Server received new key from client with Id: ' + clientId)
            msg.split('<receivedNewKey>')
            clientKey = msg[0]
            loggedInClients[clientId] = clientKey
            print('           - New key from client with Id: ' + clientId + ' = ' + clientKey)
    return


# This function checks if the received message is a valid Id
def msgIsValidId(receivedId):
    return receivedId.isdigit()


# This function handles a new joiner client to the server
def new_joiner(client):
    print('           - Server connected with new client: Waiting for Id')
    waitForId = True
    while waitForId:
        msg = client.recv(2048).decode()
        print('           - Server received receivedId from client: ', end='')
        msg.split('<receivedId>')
        receivedId = msg[0]
        key = msg[1]
        print(receivedId)
        if msgIsValidId(receivedId):
            print('Id is valid')
            waitForId = False
        else:
            print('Id is invalid')

    print('           - Server connected with new client: With Id: ' + receivedId)

    handle_registered_client(client, receivedId, key)

    return


# This is the main function
def main():
    serverSocket = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
    serverSocket.bind(('', 4000))
    serverSocket.listen(1)

    print('--------------------------HELLO--------------------------')
    print('------------------The server is running------------------')

    while True:
        client, address = serverSocket.accept()
        th.Thread(target=new_joiner(), args=(client,)).start()
        # handle_nickname(client)

    return


if __name__ == "__main__":
    main()
