
#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

from logzero import logger


def chunker(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def squisher(numbers=11):
    logger.info(f"""{numbers}""")
    logger.info(f"""length of numbers == {len(str(numbers))}""")
    if len(str(numbers)) > 1:
        ch = chunker(str(numbers), 2)
        logger.info(type(ch))
        for chunk in ch:
            logger.info(chunk)



def main():
    """ Main entry point of the app """
    squisher(2)
    logger.info(f"""=====""")
    squisher(1234111)
    logger.info(f"""=====""")
    squisher(12341113484980823980823798)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

