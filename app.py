# -*- coding: utf-8 -*-

from os import sys, path

if sys.version_info.major == 3:
    print('Python3')
else:
    print('Python2')
    reload(sys)
    sys.setdefaultencoding("utf-8")

root_files = path.dirname(path.abspath(__file__))
sys.path.append(root_files)

# External libraries

# Local libraries
from src.utils.read_file import read
from src.services.payments import formatter_service, parser_service, payments_service


def pipeline():
    """
    Runs the main thread of the script
    """
    try:
        data = read(root_files, "test_cases.txt")

        for i, case in enumerate(data):
            print("Case {}:".format(i+1))
            print("Input:\n\t{}".format(case))
            
            data_case = parser_service.parser_payments(case)
            data_case_formatted = formatter_service.format_date_hours(data_case)
            payments = payments_service.get_payments(data_case_formatted)
            
            print("Output:\n\tThe amount to pay {} is: {} USD\n".format(payments["employee"], payments["pay"]))

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(str(e) + " App: pipeline - LINE: " + str(exc_tb.tb_lineno))

if __name__ == "__main__":
    pipeline()

