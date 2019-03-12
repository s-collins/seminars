from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import socket
import urllib

# set timeout in seconds
socket.setdefaulttimeout(20)


def get_soup(url):
    """
    Sends a request to the given URL and creates BeautifulSoup tree from
    response HTML.

    Raises:
        http.client.HTTPException
    """
    response = urllib.request.urlopen(url)
    return BeautifulSoup(response.read(), 'html.parser')


class ScraperBase(ABC):

    def ping(self):
        """
        Pings the scraper's URL in order to confirm that it is valid.

        Returns:
            True if a connection could be made with URL. False otherwise.
        """
        try:
            urllib2.urlopen(self.get_url())
        except:
            return False
        else:
            return True

    @abstractmethod
    def get_url(self):
        """
        Returns:
            String containing the principle URL for the data source.
        """
        pass

    @abstractmethod
    def extract_events(self):
        """
        Scrapes the associated URL in order to extract event details.

        Returns:
            List of Event objects.
        """
        pass

