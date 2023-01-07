# This .py file implements client_1


import constants
import socket as soc
import threading as th


# Initial clientSocket Id, also the port it will be connecting to
INITIAL_CLIENT_ID = 4001


# This function handles the login to the KeyServer
def register_to_server(serverSocket, clientId, clientKey):
    print('         - Connected with key server')
    isLoggedIn = False
    msg = ''
    receivedMsg = ''
    while not isLoggedIn:
        msg = str(clientId) + '<receivedId>' + clientKey
        print('         - Sending message: ' + msg)
        serverSocket.send(msg.encode('ascii'))
        receivedMsg = serverSocket.recv(2048).decode()
        if receivedMsg == 'OK':
            isLoggedIn = True
        else:
            clientId += 1
    print('         - Successfully registered with following Id: ' + str(clientId))
    return


def main():
    key = 'abcdefgh'
    clientId = INITIAL_CLIENT_ID

    serverSocket = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
    serverSocket.connect(('localhost', constants.KEYSERVER_PORT))

    register_to_server(serverSocket, clientId, key)

    return


if __name__ == '__main__':
    main()
