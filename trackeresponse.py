#!/usr/bin/env python3

import socket
import struct


def parsebytestoip(data):
    ip_list = []
    for offset in range(0, 120, 6):
        # unpack the buffer which returns a tuple, ! is for network endian or big endian and I is for unsigned integer
        unpacked_buffer = struct.unpack_from('!I', data, offset)[0]
        packed_buffer_for_ntoa = struct.pack(
            '!I', unpacked_buffer)  # pack it for input to inet_ntoa
        ip_dotted_form = socket.inet_ntoa(packed_buffer_for_ntoa)
        ip_list.append(ip_dotted_form)

    return ip_list


def parsebytestoport(portdata):
    port_list = []
    for offset in range(4, 120, 2):
        port = struct.unpack_from('!H', portdata, offset)[0]
        port_list.append(port)
    return port_list
