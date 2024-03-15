from datetime import datetime
import pytz
from cat.mad_hatter.decorators import tool, hook

@tool
def get_the_time(tool_input, cat):
    """Che ore sono in Italia", "che ore sono", "dimmi l'orario"""

    return str(datetime.now(pytz.timezone('Europe/Rome')))
