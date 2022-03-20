# -*- coding: utf-8 -*-

from os import sys

def read(file_path, file_name):
    """
    Reads text files
    
    Parameters
    ----------
    file_path: string
        path where the file is located
    file_name: string
        file name and extension
    
    Returns
    ----------
    data: list
        Listing with each line of the file
    """
    try:
        with open("{}/{}".format(file_path, file_name)) as f:
            lines = f.readlines()
            return lines
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(str(e) + " read_files: read - LINE: " + str(exc_tb.tb_lineno))
        return ""

