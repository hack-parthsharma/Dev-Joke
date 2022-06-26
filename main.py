"""DevJoke is a cli program that returns programming jokes randomly. (Internet required)"""

import sys
import json
import random
import requests
import properties

class DevJoke:
    """DevJoke main class - DevJoke program starts from this class."""

    def __init__(self):
        """INIT"""

        self.joke = ""

        self.get_the_joke()

        print(self.joke)

    def get_the_joke(self):
        """This method sends GET request to API_URL defined in property.py"""

        try:

            response = requests.get(properties.API_URL).text
            data = json.loads(response)

            self.joke = data["joke"]

        except:

            print(random.choice(properties.MESSAGES))
            sys.exit(1)

if __name__ == "__main__":
    app = DevJoke()
