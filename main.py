import asyncio

import parse
import trackerequest
import random
from urllib.parse import urlencode

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
print(url)
trackerequest.main('www.google.com')
loop = asyncio.get_event_loop()
loop.run_until_complete(trackerequest.main(url))
