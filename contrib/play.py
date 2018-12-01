from pprint import pprint
from collections import defaultdict
import csv

from pantomime import parse_mimetype


data = defaultdict(int)
with open('occrp.csv', 'r') as fh:
    reader = csv.reader(fh, delimiter=';')
    for row in reader:
        original, count = row
        parsed = parse_mimetype(original)
        print(parsed.label)
        # data[parsed.normalized] += int(count)
        # if parsed.normalized != original:
        #     pprint((original, parsed.label))


print(len(data))
