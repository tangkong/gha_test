import argparse
from pathlib import Path


def main(args):
    source_dir = Path(args.csv_dir)
    xml_dir = Path(args.xml_dir)

    for item in source_dir.glob('*'):
        print(item)

    print(xml_dir)

if __name__ == "__main__":
    print('convert script run')
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_dir')
    parser.add_argument('xml_dir')
    main(parser.parse_args())