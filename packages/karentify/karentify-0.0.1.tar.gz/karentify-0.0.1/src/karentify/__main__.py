import sys
import argparse

from random import choice
from karentify import karentify


REACTIONS = ['inaudible', 'incomprehensible', 'enraged hairflip',
             'angry fingerpointing', 'attention seeking room scan']


def main(args):
    cmdline = argparse.ArgumentParser(description='Unleash your inner Karen on `s`')
    cmdline.add_argument('--dEmAnD-MaNaGeR', '-D', action='store_true',
                         help='Demand to speak to somebody with actual authority')
    cmdline.add_argument('entitlement', type=str, nargs='*', help='Your important message')
    opts = cmdline.parse_args(args)

    if len(opts.entitlement) > 1:
        print(karentify(' '.join(opts.entitlement)) + '!!!')
    else:
        if sys.stdin.isatty():
            print('Hello, how can I help you?')

        for s in [_.strip() for _ in sys.stdin]:
            if len(s):
                demand = karentify(s)
            else:
                demand = f'[{choice(REACTIONS)}]'

            if s != demand:
                print(f'{demand}!!!')
            else:
                print(s)

    if opts.dEmAnD_MaNaGeR:
        print(karentify('and I would like to talk to your manager') + '!!!')


def run():
    # if this is not split up, the cli can't be tested by injecting args
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    run()
