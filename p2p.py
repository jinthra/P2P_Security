import time
import sys
from random import randint
from tools import fileManager
from tools.client import Client
from tools.server import Server
from tools.constants import *



"""
    This class will take care of converting client to server
"""
class p2p:
    # make ourself the default peer
    peers = ['157.26.66.X']


def main():
    # if the server breks we try to make a client a new server
    #msg = convert()


    msg = fileManager.convert_to_bytes()
    while True:
        try:
            print("-" * 21 + "Trying to connect" + "-" * 21)
            # sleep a random time between 1 -5 seconds
            time.sleep(randint(RAND_TIME_START,RAND_TIME_END))
            for peer in p2p.peers:
                try:
                    client = Client(peer)
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass


                # become the server
                try:
                    server = Server(msg)
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    pass

        except KeyboardInterrupt as e:
            sys.exit(0)

if __name__ == "__main__":
    main()