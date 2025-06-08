from event import subscribe
from person_utils.creation import print_creation_of_obj
from person_utils.my_details import normal_print, capital_print

def setup_log_creation():
    subscribe("print-details-on-creation", print_creation_of_obj)

def setup_capital_print():
    subscribe("capital-print", capital_print)



def setup_normal_print():
    subscribe("normal-print", normal_print)



def setup_all_print():
    subscribe("normal-print", normal_print)
    subscribe("capital-print", capital_print)
