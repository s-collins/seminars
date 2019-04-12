from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import socket
import urllib.request


# set timeout in seconds
socket.setdefaulttimeout(20)


class WrapperBase(ABC):

    def ping(self, url):
        """
        Pings the scraper's URL in order to confirm that it is valid.

        Returns:
            True if a connection could be made with URL. False otherwise.
        """
        try:
            urllib.request.urlopen(self.get_url())
            return True
        except:
            return False
        
    @abstractmethod
    def get_source_name(self):
        """
        Returns:
            String with the name of the data source
        """

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

