import random
import socket
import struct
from urllib.parse import urlencode
import requests
import bencoding
import parse

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

url = (torrentMetaData['announce']).decode('utf-8') + "?" + urlencode(query)
print('Connecting to torrent tracker..........', url)
res = requests.get(url)
print(type(res.text), type(res.content))
data = bencoding.Decoder(res.content).decode()
peerlist = data[b'peers']
print(len(peerlist))
print(type(data[b'peers']), data)

offset = 0
ip1 = struct.unpack_from("!i", peerlist, offset)[0]
firstip = socket.inet_ntoa(struct.pack("!i", ip1))
print(firstip)
