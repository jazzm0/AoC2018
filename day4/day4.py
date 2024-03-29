from collections import defaultdict
from operator import itemgetter
import re


totals = defaultdict(int)
minutes = defaultdict(lambda: defaultdict(int))

with open('input') as ifile:
    for line in sorted(ifile):
        minute = int(re.search(r':(\d+)', line).group(1))
        if '#' in line:
            guard = int(re.search(r'#(\d+)', line).group(1))
        elif 'asleep' in line:
            m0 = minute  # starting minute (inclusive)
        elif 'wakes' in line:
            m1 = minute  # ending minute (non-inclusive)
            # guard, m0, and m1 are known here; increment the data structures
            for m in range(m0, m1):
                totals[guard] += 1
                minutes[guard][m] += 1

# part 1
key = itemgetter(1)  # compare the value in the (key, value) pairs
guard = max(totals.items(), key=key)[0]
minute = max(minutes[guard].items(), key=key)[0]
print(guard * minute)

# part 2
items = []
for guard in minutes:
    minute, count = max(minutes[guard].items(), key=key)
    items.append((count, guard * minute))
print(sorted(items)[-1][-1])
