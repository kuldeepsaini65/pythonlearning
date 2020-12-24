import argparse
import sys


def calc(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'div':
        return args.x / args.y
    elif args.o == 'sub':
        return args.x - args.y
    else:
        return 'Wrong Operation! Please Check Your Option'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help='Enter your First Number')
    parser.add_argument('--y', type=float, default=1.0, help= 'Enter your Second Number')
    parser.add_argument('--o', type=str, default='add', help='Select Operation +-/*')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
