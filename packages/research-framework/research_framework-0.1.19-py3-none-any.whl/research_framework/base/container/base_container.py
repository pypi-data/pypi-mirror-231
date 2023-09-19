from abc import ABC, abstractmethod
from typing import Optional, Any, Dict
from research_framework.base.wrappers.filter_wrapper import BaseFilterWrapper

class BaseContainer(ABC):
    
    @staticmethod
    @abstractmethod
    def register_dao(collection):...
    
    @staticmethod
    @abstractmethod
    def bind(wrapper:Optional[BaseFilterWrapper]=None):...
    
    @staticmethod
    @abstractmethod
    def get_filter(clazz:str, params:Dict[str, Any]) -> BaseFilterWrapper:...
    
    @staticmethod
    @abstractmethod
    def get_metric(clazz:str) -> BaseFilterWrapper:...

    @staticmethod
    @abstractmethod
    def init_wandb_logger(project:str, name:Dict[str, Any]): ...

    @staticmethod
    @abstractmethod
    def send_to_logger(message:Dict[str, Any], step:Optional[int] = None):...