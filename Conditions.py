import psutil
import subprocess
import re

Memory = 0
Disk = 1
PERCENTAGE_REG_EX = '\d{1,3}%'


def minimum_ram_required(memory_required, unit):
    return space_required(memory_required, unit, Memory)


def minimum_free_disk_space(disk_size, unit):
    return space_required(disk_size, unit, Disk)


def space_required(min_val, unit, type):
    unit_val = 1
    if unit == "KB":
        unit_val = 1024
    elif unit == "MB":
        unit_val = 1024 * 1024
    elif unit == "GB":
        unit_val = 1024 * 1024 * 1024

    if type == Memory:
        memory = psutil.virtual_memory().total
    elif type == Disk:
        # primaryPartitionName = psutil.disk_partitions()[0].device
        memory = psutil.disk_usage('/').free

    return (memory / unit_val) >= min_val


def is_power_on_adapter():
    power_info = subprocess.check_output(["pmset", "-g", "batt"])
    return "AC Power" in power_info


def is_power_on_battery():
    # powerInfo = subprocess.check_output('pmset -g batt')
    power_info = subprocess.check_output(["pmset", "-g", "batt"])
    return "Battery Power" in power_info


def check_min_battery_required(minimum_percentage):
    if is_power_on_adapter():
        return True

    power_info = subprocess.check_output(["pmset", "-g", "batt"])
    current_battery_percent = re.search(PERCENTAGE_REG_EX, power_info).group(0)
    current_battery_percent = int(current_battery_percent[:-1])
    return current_battery_percent >= minimum_percentage


def execute_script(script_file):
    return_val = 0
    if script_file.endswith("py"):
        return_val = subprocess.check_output(["python", "./conditions/download/" + script_file])
    if script_file.endswith("sh"):
        return_val = subprocess.check_output(["sh", "./conditions/download/" + script_file])
    return return_val == 1


def execute_command(cmd_args):
    subprocess.check_output(cmd_args)


print minimum_ram_required(16, "GB")
