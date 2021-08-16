# Imports
import dateutil.parser
from datetime import datetime, timedelta

# A function that takes the war end time and subtracts by the current time to get the time remaining of the war.
def get_time(isoTime):

    # The last four characters of the string are unecessary.
    newISOTime = isoTime[:-4]
    now = dateutil.parser.isoparse(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    warTime = dateutil.parser.isoparse(newISOTime[:-5])

    # Adding two hours to the war time because it's in a different time zone.
    warTime = warTime + timedelta(hours=2)

    return str(warTime-now)