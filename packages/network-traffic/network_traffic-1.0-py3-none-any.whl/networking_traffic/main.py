#!/usr/bin/env python3 
"""
Developped By Talel-Khairi Kchih
"""

import pyshark

print("______ Welcome To Networking Traffic Package______ ")
################################
# cap = pyshark.FileCapture('/home/g360546rts/tt.pcapng')
# print(f'___cap____{cap}')
# # <FileCapture /tmp/mycapture.cap (589 packets)>
# # cap = cap[5]
# print(f'___###_____{type(cap)}')


# # for packet in cap:
# #     print("___###_____",packet.layers)
# k = 0
# for i in cap:
    # print("##############",i)

##########################
# import pyshark

# capture = pyshark.LiveCapture(interface='eno1')
# for packet in capture:
#     if 'ETH Layer' in str(packet.layers):
#         field_names = packet.eth._all_fields
#         field_values = packet.eth._all_fields.values()
#         for field_name, field_value in zip(field_names, field_values):
#             print(f'{field_name}: {field_value}')

##########################################

print("______ Count packet______ ")
cap = pyshark.FileCapture('/home/g360546rts/tt.pcapng')


cap.load_packets()
packet_amount = len(cap)
print("_____amount_____",packet_amount)

###########################################
print("______ Show Live Capture______ ")
capture = pyshark.LiveCapture(interface='eno1', output_file='test_docker.pcapng')
capture.sniff(timeout=5)
capture
print("capture", capture)
capture[1]
print("capture", capture[1])

pkt = capture[1]
layers = pkt.layers
print("########################")
print("########################",layers)
print(pkt.ETH)



# for i in capture:
#     print("___dir_____",i)



# for packet in capture.sniff_continuously(packet_count=5):
#     print('Just arrived:', packet)