from pydantic import BaseModel
from enum import Enum
from datetime import date, time
from cat.mad_hatter.decorators import plugin


# select box
#   (will be used in class DemoSettings below to give a multiple choice setting)
class NameSelect(Enum):
    a: str = 'Rome'
    b: str = 'UTC'


# settings
class DemoSettings(BaseModel):

    # Select
    time_zone: NameSelect = NameSelect.a


# Give your settings model to the Cat.
@plugin
def settings_model():
    return DemoSettings