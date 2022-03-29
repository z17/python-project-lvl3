from typing import Optional

from progress.bar import Bar


class Progress:
    def __init__(self):
        self._resources_bar: Optional[Bar] = None

    def processing_resources_start(self, count):
        self._resources_bar = Bar('Processing resources', max=count)

    def processing_resources_next(self):
        self._resources_bar.next()

    def processing_resources_finish(self):
        self._resources_bar.finish()
