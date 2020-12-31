#!/usr/bin/env python3

import parse
import trackeresponse
import random
from urllib.parse import urlencode
import requests
import bencoding
import parse
import ipaddress

path = './torrents/ubuntu-20.04.1-desktop-amd64.iso.torrent'

torrentMetaData = parse.parse(path)

# generate random peer_id of 20 bytes
peerRandom = ''
for i in range(12):
    peerRandom += str(random.randint(0, 9))
peerId = '-XT1765-' + ''.join(peerRandom)

# prepare the query params
query = {
    'info_hash': torrentMetaData['info_hash'],
    'peer_id': peerId,
    'port': 6881,
    'uploaded': 0,
    'downloaded': 0,
    'left': torrentMetaData['left'],
    'compact': 1,
    'event': 'started'
}

# make request to tracker
url = (torrentMetaData['announce']).decode('utf-8') + "?" + urlencode(query)
res = requests.get(url)

# decode the binary data and store the peerlist bytes
data = bencoding.Decoder(res.content).decode()
peerlist = data[b'peers']


# offset = 0
# ip1 = struct.unpack_from("!i", peerlist, offset)[0]
# # firstip = socket.inet_ntoa(struct.pack("!i", ip1))
# # print(firstip)
# ip_list = []
# for offset2 in range(0,12,6):
#     unpacked_ip = struct.unpack_from("!i", peerlist, offset2)[0]
#     dotted_ip = struct.pack('!i', unpacked_ip)
#     ip_list.append(ipaddress.ip_address(dotted_ip))


# for item in ip_list:
#     print("from the loop", item)

# ip2 = trackeresponse.parsebytestoip(ip1)
# print("Ip from trackerresponse", ip2)

# get the ip and ports from the bytes (first 4 bytes are ip and next 2 bytes are port)

ipaddresslist = trackeresponse.parsebytestoip(peerlist)
portslist = trackeresponse.parsebytestoport(peerlist)

peerdict = dict()
for i in range(len(ipaddresslist)):
    peerdict[ipaddresslist[i]] = portslist[i]

for key, value in peerdict.items():
    print(key,":",value)