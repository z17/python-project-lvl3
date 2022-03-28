import argparse
import sys

from progress.bar import Bar

from page_loader.download import download


def main():
    parser = argparse.ArgumentParser(description='Download page')

    parser.add_argument('url')
    parser.add_argument('destination')

    args = parser.parse_args()

    bar1 = Bar('Load Url', max=1)
    bar2 = Bar('Process resources', max=100)
    bar3 = Bar('Saving results', max=1)

    bar1.next()
    bar1.finish()
    bar2.next()
    bar2.next()

    def load_url():
        bar1.next()
        bar1.finish()

    def process_resources(step):
        bar2.next(step)
        if step == 100:
            bar2.finish()

    def save_results():
        bar3.next()
        bar3.finish()

    try:
        print(download(args.url, args.destination, load_url, process_resources, save_results))
    except RuntimeError:
        print("ERROR, see logs")
        sys.exit(1)


if __name__ == '__main__':
    main()
