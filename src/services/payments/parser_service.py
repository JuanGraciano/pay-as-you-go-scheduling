# -*- coding: utf-8 -*-

# External libraries
from os import sys

def parser_payments(string_data):
    """
    Receives as input the raw data from the text file and divides it into sections
    
    Parameters
    ----------
    string_data: string
        Represents a line (case) of the text file
    
    Returns
    ----------
    data: dict
        Returns the case data in dict format
    """
    try:
        string_data = string_data.replace("\n", "")
        split_name_hours = string_data.split("=")
        
        if len(split_name_hours) > 1:
            name_employee = string_data.split("=")[0]
            hours_worked = string_data.split("=")[1]
        else:
            raise Exception("""The expected structure is not found. The structure should be '{employee name}={hours worked}'""")

        hours_per_day = hours_worked.split(",")

        return {
            "name": name_employee,
            "hours": hours_per_day
        }
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(str(e) + ", payments: parser_payments - LINE: " + str(exc_tb.tb_lineno))
        return {}

