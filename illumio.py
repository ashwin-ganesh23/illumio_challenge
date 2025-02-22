'''
The program generates an output file containing the following: 
Count of matches for each tag, count of port and protocol pairings

The program should read a csv file and a plain text file.
The csv file contains the flow log data.
The plain text file contains the mappings of the port and protocol to the tag.

The program should generate an output file containing the following: 
Count of matches for each tag, count of port and protocol pairings

'''

import socket
from collections import defaultdict

mappings_dict = {}
tag_counts = {}
match_count = defaultdict(int)
port_protocol_count = defaultdict(int)


def get_protocol_name(protocol_number):
    for name, value in socket.__dict__.items():
        if name.startswith("IPPROTO_") and value == protocol_number:
            return name[8:].lower()
    return None

def get_mappings(mappings_file):
    #read a plain text file 
    with open(mappings_file, 'r') as file:
        mappings = file.readlines()

    #remove the newline character from the mappings
    mappings = [mapping.strip() for mapping in mappings if mapping]

    mappings = [mapping for mapping in mappings if mapping]

    for mapping in mappings:
        mapping = mapping.strip()
        mapping = mapping.split(',')
        mappings_dict[(mapping[0], mapping[1].lower())] = mapping[2]

def find_matches(flow_log_file):
    with open(flow_log_file, 'r') as file:
        csv_file = file.readlines()

    #remove the newline character from the csv file
    csv_file = [line.strip() for line in csv_file if len(line) > 2]    

    #iterate through the csv file
    for row in csv_file:
        row = row.split(' ')

        #extract the dst port and protocol from the row
        dst_port = row[6]
        protocol = int(row[7])

        protocol_name = get_protocol_name(int(protocol))
        port_protocol_count[(dst_port, protocol_name)] += 1

        #check if the dst port and protocol are in the mappings_dict
        if (dst_port, protocol_name) in mappings_dict:
            tag = mappings_dict[(dst_port, protocol_name)]
            match_count[tag] += 1
        else:
            tag = "Untagged"
            match_count[tag] += 1

def write_outputs():
    #write the match_count to a csv file
    with open('match_count.csv', 'w') as file:
        for key in match_count:
            file.write(f"{key},{match_count[key]}\n")

    with open('port_protocol_count.csv', 'w') as file:
        for key in port_protocol_count:
            file.write(f"{key[0]},{key[1]},{port_protocol_count[key]}\n")

def get_port_protocol_count(flow_log_file, mappings_file):
    get_mappings(mappings_file)

    find_matches(flow_log_file)

    write_outputs()

def main():
    get_port_protocol_count('illumio_data.csv', 'mappings.txt')

if __name__ == "__main__":
    main()