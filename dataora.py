from datetime import datetime
import pytz
from cat.mad_hatter.decorators import tool, hook

@tool
def get_the_time(tool_input, cat):
    """Che ore sono in Italia", "che ore sono", "dimmi l'orario"""

    settings = cat.mad_hatter.get_plugin().load_settings()
    prefix = settings["time_zone"]

    if prefix == "Rome":
        timezona = "Europe/Rome"
    else:
        timezona = "UTC"  

    return str(datetime.now(pytz.timezone(timezona)))
