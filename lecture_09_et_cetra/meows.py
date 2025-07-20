# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("usage: meows.py")







#/////////////////////////////////////////////////////////

import argparse
parser = argparse.ArgumentParser(description="Print 'meow' a specified number of times.")
parser.add_argument("-n", help="Number of times to print 'meow'", default = 1, type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")