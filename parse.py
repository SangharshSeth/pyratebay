import bencoding
from hashlib import sha1


def parse(torrentfile):
    parsedata = {}
    with open(torrentfile, 'rb') as unparsed:
        metaData = bencoding.Decoder(unparsed.read()).decode()
        torrentInfo = bencoding.Encoder(metaData[b'info']).encode()
        infoHash = sha1(torrentInfo).digest()
        parsedata['announce'] = metaData[b'announce']
        parsedata['info_hash'] = infoHash
        parsedata['left'] = metaData[b'info'][b'length']
    return parsedata
