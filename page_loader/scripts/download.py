import argparse
import sys

from page_loader.download import download


def main():
    parser = argparse.ArgumentParser(description='Page downloader')

    parser.add_argument('url')
    parser.add_argument('-o', '--output', default='')

    args = parser.parse_args()

    try:
        print(download(args.url, args.destination))
    except RuntimeError:
        print("ERROR, see logs")
        sys.exit(1)


if __name__ == '__main__':
    main()
