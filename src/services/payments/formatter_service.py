# -*- coding: utf-8 -*-

# External libraries
from os import sys

# Local libraries
from src.config import CALENDAR_2, DAY_ABBR

def format_date_hours(hours_worked):
    """
    Takes as input the data parsed by the parser to format dates and times
    
    Parameters
    ----------
    hours_worked: dict
        Employee data previously prepared by the parser
    
    Returns
    ----------
    data: dict
        Formatted employee data 
    """
    
    try:
        if len(hours_worked) <= 0:
            raise Exception("A full dictionary is expected")

        hours_worked_formated = hours_worked.copy()
        hours_worked_formated["formatted_hours"] = {}
        for x in hours_worked["hours"]:
            day = str(x[:2]).lower()
            if day.isalpha() and day in DAY_ABBR:
                hours_split = x[2:].split("-")
                if len(hours_split) > 1: 
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
                raise Exception("""The expected structure is not found. The structure should be '{day abbreviation}={hour start}-{hour end}'""")
                
        return hours_worked_formated
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(str(e) + ", payments: format_date_hours - LINE: " + str(exc_tb.tb_lineno))
        return {}

def format_payments():
    """
    Analyzes the configuration file where the data to be paid per hour is stored.
    
    Returns
    ----------
    data: dict
        Formatted payment schedules
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


