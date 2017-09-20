# original file: aux_print_py3.py
#   by blackjuice, LuHoTuner, accelcoil, saguahollic & Lucas S.J. Hong
#   created on: 151231
#
#   python 3.x
# - - -
# edit (170524): imported from pte-python project

def print_ddt(ddt):
    print ("\nprinting dictionary >> ")
    print ("----------------------")
    for key in ddt:
        print(key)
        print("  ", ddt[key])
    print("ddt size: ", len(ddt))
    print ()

def print_ddt_sorted_key(ddt):
    print ("\nprinting dictionary(sorted) >> ")
    print ("------------------------------")
    for key in sorted(ddt):
        print(key)
        print("  ", ddt[key])
    print ()

def print_ddt_keys_SCH(ddt):
    str_tmp = []
    for key in ddt:
        if  (not (key).startswith("filename")) and (not (key).startswith("info_")):
            str_tmp.append( key )
    return (str_tmp)

def print_file(datafileString):
    print ("\nprinting file >> ")
    print ("----------------")
    with open(datafileString) as infile:
        for line in infile:
            line = line.strip() #deleting breakline
            print (line)
    print ()