from abc import ABC


class ScraperBase(ABC):

    @abstractmethod
    def ping(self):
        """
        Pings the scraper's URL in order to confirm that it is valid.

        Returns:
            True if a connection could be made with URL. False otherwise.
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

