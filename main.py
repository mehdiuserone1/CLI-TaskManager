import argparse
import json

with open('data.json', 'r') as data:
    data = json.load(data)

print(data)