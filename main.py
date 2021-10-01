from requests.models import default_hooks
from TopNames import NameScalper
import argparse
from os import linesep
from sys import stdout
from typing import TextIO
from time import sleep

#DEFAULT_OUTFILE = os.path.join(os.path.split(os.path.abspath(__file__))[0],"output.txt")

def main(*, output:TextIO = stdout, verbose:bool = False, time_between_requests:int = 200) -> None:
    """
    Create scrapers for the top names of the last thirteen decades and output them to the given output.

    :param output: TextIO stream to write to. Default is stdout.
    :param verbose: Boolean that, when true, will include verbose output. Default is false.
    :param time_between_requests: Time in millis between requests. Defaults to 200 to be nice.
    :returns: None
    :raises RuntimeError: Can raise RuntimeError from scalper if a 200 Response is not given by the website.
    """

    if(verbose):
        print("Starting.")

    # Site URLs follow a pattern, https://www.ssa.gov/oact/babynames/decades/names[decade].html
    # Since each decade starts at 2010 and decreases by 10 until 1880, we can use list comprehension here.
    sites = [f"https://www.ssa.gov/oact/babynames/decades/names{x}s.html" for x in range(2010,1880,-10)]

    unique_names = []
    for site in sites:
        # create our scalper
        scalper = NameScalper.NameScalper(site)

        for name in scalper:
            # if the name is unique, we output it and also append it to the array.
            if not name in unique_names:
                unique_names.append(name)
                output.write(f"{name}{linesep}")
                if(verbose):
                    print(f"\tWrote name \"{name}\"")

        # Sleep to be nice.
        sleep(time_between_requests//1000)

    if(verbose):
        print("Done.")


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Scrape a list of the top baby names from the last thirteen decades.")
    parser.add_argument('--output', '-o', help="Output file.", required=False, type=argparse.FileType('w'), default=stdout)
    parser.add_argument('--verbose','-v', help="Verbose output.", required=False, action='store_true' )
    args = parser.parse_args()
    outfile = args.output
    try:
        main(output=outfile,verbose=args.verbose)
    finally:
        outfile.close()