#! /usr/bin/python3

EC_IO_FILE = '/sys/kernel/debug/ec/ec0/io'
EC_FILE_1 = '/etc/modprobe.d/ec_sys.conf'
EC_FILE_2 = '/etc/modules-load.d/ec_sys.conf'

# Adding EC_SYS support to the OS 

def check():
    FLAG = 1
    try:
        FILE = open(EC_FILE_1, 'r')
    except FileNotFoundError:
        FILE = open(EC_FILE_1, 'w')
        FILE.write("options ec_sys write_support=1")
        FILE.close()
        FLAG = 0
        
    try:
        FILE = open(EC_FILE_2, 'r')
    except FileNotFoundError:
        FILE = open(EC_FILE_2, 'w')
        FILE.write("ec_sys")
        FILE.close()
        FLAG = 0

    return FLAG

# Universal EC Byte writing

def write(BYTE, VALUE):
    with open(EC_IO_FILE,'w+b') as file:
        file.seek(BYTE)
        file.write(bytes((VALUE,)))

# Universal EC Byte reading

def read(BYTE, SIZE):
    with open(EC_IO_FILE,'r+b') as file:
        file.seek(BYTE)
        if SIZE == 1:
            VALUE = int(file.read(1).hex(),16)
        elif SIZE == 2:
            VALUE = int(file.read(2).hex(),16)
    return int(VALUE)

def fan_profile(PROFILE, VALUES, CPU):
    
    # Setting up fan profiles
    
    if PROFILE == "auto":
        write(VALUES[0][0], VALUES[0][1])
        write(VALUES[1][0], VALUES[1][1])
        speed_writer(VALUES)
    elif PROFILE == "basic" and CPU == 0:
        write(VALUES[0][0], VALUES[0][2])
        write(VALUES[1][0], VALUES[1][1])
        speed_writer(VALUES)
    elif PROFILE == "advanced":
        write(VALUES[0][0], VALUES[0][3])
        write(VALUES[1][0], VALUES[1][1])
        speed_writer(VALUES)
    elif PROFILE == "cooler booster":
        VALUE = read(VALUES[1][0], 1)
        if VALUE == VALUES[1][1]:
            write(VALUES[1][0], VALUES[1][2])
        else:
            write(VALUES[1][0], VALUES[1][1])
            
def speed_writer(VALUES):
    # Setting up indivisual CPU FAN SPEED bytes
    write(VALUES[2][0], VALUES[4][0])
    write(VALUES[2][1], VALUES[4][1])
    write(VALUES[2][2], VALUES[4][2])
    write(VALUES[2][3], VALUES[4][3])
    write(VALUES[2][4], VALUES[4][4])
    write(VALUES[2][5], VALUES[4][5])
    write(VALUES[2][6], VALUES[4][6])
    # Setting up indivisual GPU FAN SPEED bytes
    write(VALUES[3][0], VALUES[4][7])
    write(VALUES[3][1], VALUES[4][8])
    write(VALUES[3][2], VALUES[4][9])
    write(VALUES[3][3], VALUES[4][10])
    write(VALUES[3][4], VALUES[4][11])
    write(VALUES[3][5], VALUES[4][12])
    write(VALUES[3][6], VALUES[4][13])

