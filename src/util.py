# Imports
import dateutil.parser
from datetime import datetime, timedelta


# A function that takes the war end time and subtracts by the current time to get the time remaining of the war.
def get_time(iso_time) -> str:
    # The last four characters of the string are necessary.
    new_iso_time = iso_time[:-4]
    now = dateutil.parser.isoparse(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    war_time = dateutil.parser.isoparse(new_iso_time[:-5])

    # Adding two hours to the wartime because it's in a different time zone.
    war_time = war_time + timedelta(hours=2)

    return str(war_time - now)
