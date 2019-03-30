# Copyright 2019 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Demo of Enlighten's features
"""

import random
import time

import enlighten

from multicolored import run_tests, load
from multiple_logging import process_files


def initialize(manager, initials=15):
    """
    Simple progress bar example
    """

    # Simulated preparation
    pbar = manager.counter(total=initials, desc='Initializing:', unit='initials')
    for num in range(initials):  # pylint: disable=unused-variable
        time.sleep(random.uniform(0.1, 0.5))  # Random processing time
        pbar.update()
    pbar.close()


def main():
    """
    Main function
    """

    manager = enlighten.get_manager()
    initialize(manager, 15)
    load(manager, 80)
    run_tests(manager, 40)
    process_files(manager)
    manager.stop()  # Clears all temporary counters and progress bars
    time.sleep(3)


if __name__ == '__main__':
    main()
