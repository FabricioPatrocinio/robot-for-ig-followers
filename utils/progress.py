# External module
import time
from alive_progress import alive_bar


def process_progress(number: int = 1, milliseconds: int = 50):
    '''It serves for the progress bar and to give a timeout to the page.'''

    milliseconds /= 1000

    with alive_bar(number, bar='blocks') as bar:
        for i in range(number):
            time.sleep(milliseconds)
            bar()

    print()
