import argparse
import sys

from page_loader.download import download


def main():
    parser = argparse.ArgumentParser(description='Download page')

    parser.add_argument('url')
    parser.add_argument('destination')

    args = parser.parse_args()
    try:
        print(download(args.url, args.destination))
    except RuntimeError:
        print("ERROR, see logs")
        sys.exit(1)


if __name__ == '__main__':
    main()
