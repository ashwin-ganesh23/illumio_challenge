# illumio_challenge
Illumio Technical Assessment

This program takes in two arguments to the get_port_protocol_count(flow_log_file, mappings_file) function that specify the input file names and writes the match count to match_count.csv and port protocol occurrences in port_protocol_count.csv.

Simply specify the input files in the get_port_protocol_count function and run ```python3 illumio.py```

This solution matches protocol with case insensitivity and uses built-in python packages.

It utilizes the ```socket``` package to access protocol name - number pairings to convert the given protocol numbers from the flow logs into protocol names.

Thank you for reading! 
