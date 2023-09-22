#! /usr/bin/python3

EC_IO_FILE = '/sys/kernel/debug/ec/ec0/io'
EC_FILE_1 = '/etc/modprobe.d/ec_sys.conf'
EC_FILE_2 = '/etc/modules-load.d/ec_sys.conf'

# Adding EC_SYS support to the OS 

def check():
    FLAG = 0
    try:
        FILE = open(EC_FILE_1, 'r')
    except FileNotFoundError:
        FILE = open(EC_FILE_1, 'w')
        FILE.write("options ec_sys write_support=1")
        FILE.close()
        FLAG = 1
        
    try:
        FILE = open(EC_FILE_2, 'r')
    except FileNotFoundError:
        FILE = open(EC_FILE_2, 'w')
        FILE.write("ec_sys")
        FILE.close()
        FLAG = 1

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

def fan_profile(PROFILE, VALUES):
    
    # Setting up fan profiles
    ADDRESS = VALUES[2] + VALUES[3]
    if PROFILE == "auto":
        write(VALUES[0][0], VALUES[0][1])
        write(VALUES[1][0], VALUES[1][1])
        SPEED = VALUES[4]
        speed_writer(ADDRESS, SPEED)
    elif PROFILE == "advanced":
        write(VALUES[0][0], VALUES[0][2])
        write(VALUES[1][0], VALUES[1][1])
        SPEED = VALUES[5]
        speed_writer(ADDRESS, SPEED)
    elif PROFILE == "cooler booster":
        VALUE = read(VALUES[1][0], 1)
        if VALUE == VALUES[1][1]:
            write(VALUES[1][0], VALUES[1][2])
        else:
            write(VALUES[1][0], VALUES[1][1])
            
def speed_writer(ADDRESS, SPEED):
    # Setting up indivisual CPU FAN SPEED bytes
    write(ADDRESS[0], SPEED[0])
    write(ADDRESS[1], SPEED[1])
    write(ADDRESS[2], SPEED[2])
    write(ADDRESS[3], SPEED[3])
    write(ADDRESS[4], SPEED[4])
    write(ADDRESS[5], SPEED[5])
    write(ADDRESS[6], SPEED[6])
    # Setting up indivisual GPU FAN SPEED bytes
    write(ADDRESS[7], SPEED[7])
    write(ADDRESS[8], SPEED[8])
    write(ADDRESS[9], SPEED[9])
    write(ADDRESS[10], SPEED[10])
    write(ADDRESS[11], SPEED[11])
    write(ADDRESS[12], SPEED[12])
    write(ADDRESS[13], SPEED[13])