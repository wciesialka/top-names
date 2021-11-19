'''Module containing the list of top names.'''
import logging
from time import sleep
from top_names.name_scraper import NameScraper

_GLOBAL_CONTAINER = []

class NameList:
    '''Wrapper class for the list of top names.'''

    TIME_BETWEEN_REQUESTS: int = 200

    # Site URLs follow a pattern, https://www.ssa.gov/oact/babynames/decades/names[decade].html
    # Since each decade starts at 2010 and decreases by 10 until 1880,
    # we can use list comprehension here.
    SITES = [f"https://www.ssa.gov/oact/babynames/decades/names{x}s.html"\
        for x in range(2010, 1880, -10)]

    def __init__(self):
        self.__container = _GLOBAL_CONTAINER


    def __populate(self):
        '''Populate the list.'''
        logging.debug("Begin population of list.")
        for site in NameList.SITES:
            logging.debug("Scraping from site \"%s\"", site)
            scalper = NameScraper(site)
            for name in scalper:
                if not name in self.__container:
                    logging.debug("Appending name \"%s\" to list.", name)
                    self.__container.append(name)
            sleep(NameList.TIME_BETWEEN_REQUESTS/1000)
        logging.debug("Finished populating list.")

    def __getitem__(self, index: int):
        if not self.__container:
            self.__populate()
        return self.__container[index]

    def __len__(self):
        if not self.__container:
            self.__populate()
        return len(self.__container)
