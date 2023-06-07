import argparse
from pathlib import Path


def main(args):
    dir = Path(args.dir)

    print(list(dir.glob('*')))


if __name__ == "__main__":
    print('convert script run')
    parser = argparse.ArgumentParser()
    parser.add_argument('dir')
    main(parser.parse_args())