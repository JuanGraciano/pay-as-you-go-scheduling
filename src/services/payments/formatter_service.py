# -*- coding: utf-8 -*-

# External libraries
from os import sys

# Local libraries
from src.config import CALENDAR_2, DAY_ABBR

def format_date_hours(hours_worked):
    """
    Create the query to obtain information from users
    Parameters
    ----------
    gads_client: obj
        Google Ads client instance
    Returns
    ----------
    results: dataframe
        Dataframe with customer search results
    """
    # hours_worked = {
    #         "name": "RENE",
    #         "hours": ["MO10:00-12:00", "TU10:00-12:00", "TH01:00-03:00", "SA14:00-18:00", "SU20:00-21:00"]
    #     }
    try:
        if len(hours_worked) <= 0:
            raise Exception("A full dictionary is expected")

        hours_worked_formated = hours_worked.copy()
        hours_worked_formated["formatted_hours"] = {}
        for x in hours_worked["hours"]:
            day = str(x[:2]).lower()
            if day.isalpha() and day in DAY_ABBR:
                hours_split = x[2:].split("-")
                if len(hours_split) > 1: # TODO: hacer funcion para validar splits
                    # TODO: if start > end :
                        # print(la hora de comienso debe de ser menor a la hora de salida)
                    start = int(hours_split[0].replace(":", "")) + 10000
                    end = int(hours_split[1].replace(":", "")) + 10000
                    hours_worked_formated["formatted_hours"][DAY_ABBR[day]] = {
                        "start": start,
                        "end": end,
                        "hours_worked": int((end - start) / 100)
                        }
                else:
                    raise Exception("""The expected structure is not found. The structure should be '{hour start}-{hour end}'""")
            else:
                raise Exception("""The expected structure is not found. 
                    The structure should be '{day abbreviation}={hour start}-{hour end}'""")
                
        return hours_worked_formated
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(str(e) + ", payments: format_date_hours - LINE: " + str(exc_tb.tb_lineno))
        return {}

def format_payments():
    """
    Create the query to obtain information from users
    Parameters
    ----------
    gads_client: obj
        Google Ads client instance
    Returns
    ----------
    results: dataframe
        Dataframe with customer search results
    """
    try:
        payment_formated = {}
        for day in CALENDAR_2:
            payment_formated[day] = []
            for hour in CALENDAR_2[day]:
                split_hours = hour.split('-')
                if len(split_hours) > 1:
                    payment_formated[day].append({
                        "start": int(split_hours[0].replace(":", "")) + 10000,
                        "end": int(split_hours[1].replace(":", "")) + 10000,
                        "pay": CALENDAR_2[day][hour]
                    })
                else:
                    raise Exception("""The expected structure is not found. The structure should be '{hour start}-{hour end}'""")
                
        return payment_formated
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(str(e) + ", payments: format_date_hours - LINE: " + str(exc_tb.tb_lineno))
        return {}


