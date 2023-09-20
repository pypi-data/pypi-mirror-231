#!/usr/bin/env python3 
"""
Developped By Talel-Khairi Kchih
"""
import pyshark


# capture = pyshark.LiveRingCapture(interface='eno1')
capture = pyshark.LiveCapture(interface='eno1', output_file='test_docker.pcapng')
capture.sniff(timeout=2)

for packet in capture.sniff_continuously(packet_count=2):
    print('Just arrived:', packet)


capture.close()