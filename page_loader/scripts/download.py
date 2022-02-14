import argparse

from page_loader.download import download


def main():
    parser = argparse.ArgumentParser(description='Download page')

    parser.add_argument('url')
    parser.add_argument('destination')
    parser.add_argument('-f', '--format', help='set format of output', default='stylish')

    args = parser.parse_args()
    print(download(args.url, args.destination))


if __name__ == '__main__':
    main()
