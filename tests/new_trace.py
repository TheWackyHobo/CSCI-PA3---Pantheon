#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import sys

if len(sys.argv) != 5:
    print("Usage: python2 generate_trace.py <bandwidth_mbps> <packet_size_bytes> <duration_secs> <output_file>")
    sys.exit(1)

bandwidth_mbps = float(sys.argv[1])          # e.g., 50
packet_size = float(sys.argv[2])             # e.g., 1500
duration_secs = int(sys.argv[3])             # e.g., 60
output_file = sys.argv[4]

# Convert bandwidth to bytes per ms
bits_per_sec = bandwidth_mbps * 1e6
bytes_per_ms = bits_per_sec / 8.0 / 1000.0

trace = []
accumulator = 0.0

for ms in range(duration_secs * 1000):
    accumulator += bytes_per_ms
    while accumulator >= packet_size:
        trace.append(ms)
        accumulator -= packet_size

with open(output_file, 'w') as f:
    for t in trace:
        f.write("%d\n" % t)
