import abc
from typing import List
from ...domain.FundoImobiliario import FundoImobiliario


class FiiScrappingService(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def scrapFiis(self) -> List[FundoImobiliario]:
        raise NotImplementedError()