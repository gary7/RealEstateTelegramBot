import logging
from .StateMetaClass import StateMetaClass


class BasicState(metaclass=StateMetaClass):
    tag = ''
    logger = logging.getLogger('State')
    logger.setLevel(logging.DEBUG)

    @staticmethod
    def create_transition(new_state_tag, **kwargs):
        return new_state_tag, kwargs

    def __init__(self, user):
        self.user = user

    def enter(self, **kwargs):
        pass

    def update(self, message):
        pass

    def exit(self):
        pass