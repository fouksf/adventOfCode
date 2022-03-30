from functools import reduce

class Packet:
    def __init__(self, version, typeId):
        self.version = version
        self.typeId = typeId
        self.subpackets = []
        self.value = None

    def add_subpacket(self, subpacket):
        self.subpackets.append(subpacket)
    
    def set_value(self, value):
        self.value = value

def parse_input(file_name):
    input = list(map(lambda hex: bin(int(hex, 16))[2:].zfill(4), list(open(file_name, "r").read())))
    return ''.join(input)

def read_packet_version(bits):
    version = int(bits[0:3], 2)
    return (version, bits[3:])

## 4 is literal value
def read_packet_type(bits):
    typeId = int(bits[0:3], 2)
    return (typeId, bits[3:])

def read_literal_value(bits):
    binary_number = ''
    for chunk in [bits[i:i + 5] for i in range(0, len(bits), 5)]:
        binary_number += chunk[1:]
        if chunk[0] == '0':
            return (int(binary_number, 2), bits[(len(binary_number) // 4) * 5:])
    

def read_lenght_bit(bits):
    return (15 if bits[0] == '0' else 11, bits[1:])

def read_length_value(bits, length):
    return (int(bits[0: length], 2), bits[length:])

def read_packet(bits):
    (version, bits) = read_packet_version(bits)
    (typeId, bits) = read_packet_type(bits)
    packet = Packet(version, typeId)

    if typeId == 4:
        (value, bits) = read_literal_value(bits)
        packet.set_value(value)
        return (packet, bits)
    else:
        (length, bits) = read_lenght_bit(bits)
        (length_value, bits) = read_length_value(bits, length)
        if length == 15:
            ## read all subpackets in the number of bits that is length_value
            subpacket_bits = bits[:length_value]
            while subpacket_bits:
                (subpacket, subpacket_bits) = read_packet(subpacket_bits)
                packet.add_subpacket(subpacket)
            return (packet, bits[length_value:])
        else:
            ## read number of subpacket equal to length_value
            for i in range(length_value):
                (subpacket, bits) = read_packet(bits)
                packet.add_subpacket(subpacket)
            return (packet, bits)

def get_sum_of_version(packet):
    if packet.value:
        return packet.version
    else:
        return packet.version + sum(map(lambda subpacket: get_sum_of_version(subpacket), packet.subpackets))

def get_expression_value(packet):
    subpacket_values = list(map(lambda subpacket: get_expression_value(subpacket), packet.subpackets))
    if packet.typeId == 0:
        return sum(subpacket_values)
    elif packet.typeId == 1:
        return reduce(lambda x, y: x * y, subpacket_values)
    elif packet.typeId == 2:
        return min(subpacket_values)
    elif packet.typeId == 3:
        return max(subpacket_values)
    elif packet.typeId == 4:
        return packet.value
    elif packet.typeId == 5:
        return 1 if subpacket_values[0] > subpacket_values[1] else 0
    elif packet.typeId == 6:
        return 1 if subpacket_values[0] < subpacket_values[1] else 0
    elif packet.typeId == 7:
        return 1 if subpacket_values[0] == subpacket_values[1] else 0



input = parse_input("2021/16/input.txt")
(packet, bits) = read_packet(input)
print(get_expression_value(packet))


