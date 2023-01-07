# This .py file implements client_1


import constants
import socket as soc
import threading as th


# Initial clientSocket Id, also the port it will be connecting to
INITIAL_CLIENT_ID = 4001


# This function prints the commands available for the KeyServer
def print_usage():
    print('------------------KEYSERVER COMMANDS------------------')
    print('--           Help: prints usage again               --')
    print('--           Exit: Stops the app                    --')
    print('--           ViewID: returns your id                --')
    print('--           ViewKey: returns your key              --')
    print('--           ChangeKey: changes your key            --')
    print('--        LogOut: Logs out of the KeyServer         --')
    print('------------------------------------------------------')
    return


# This function handles the communication with the KeyServer
def communicate_with_server(serverSocket, clientId, clientKey):
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
            print('          - Your Key is: ' + clientKey)
        elif userInput == 'ChangeKey':
            newKey = 'new key'                                          # TO BE IMPLEMENTED
            msg = newKey
        elif userInput == 'Logout':
            msg = 'LOGOUT'
        elif msg != '':
            serverSocket.send(msg.encode('ascii'))
            msg = ''

    return


# This function handles the registration of the client into the KeyServer
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
            clientId = clientId + 1

    print('         - Successfully registered with following Id: ' + str(clientId))

    communicate_with_server(serverSocket, clientId, clientKey)

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
