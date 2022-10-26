from delete import *
from notify import *
from check import *
from mark import *

def main(test_number, delete = delete_default, notify = notify_default, check = check_default, mark = mark_default):
    delete.main(test_number = test_number, notify=notify)
    result_check = check.main(test_number = test_number)
    mark.main(test_number = test_number, resources = result_check, notify=notify)

# Default test #1
main(test_number = 1)