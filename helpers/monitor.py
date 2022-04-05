import psutil
from datetime import datetime
from termcolor import colored
from tabulate import tabulate
import os

pid = os.getpid()
main_process = object
create_time = None
executive_cores = 0
cpu_usage = 0
memory_usage = None
status = None
priority = None
io_counters = 0
total_read_bytes = None
total_write_bytes = None


def get_size_form_bytes(_bytes):
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if _bytes < 1024:
            return f"{_bytes:.2f}{unit}B"
        _bytes /= 1024


def process_monitor():
    global pid
    global main_process
    global create_time
    global executive_cores
    global cpu_usage
    global memory_usage
    global status
    global priority
    global io_counters
    global total_read_bytes
    global total_write_bytes

    for process in psutil.process_iter():
        with process.oneshot():
            if process.pid == pid:
                main_process = process

    try:
        print(colored("Info> Start to monitoring the process(not supported on OSX)", "blue"))
        create_time = datetime.fromtimestamp(main_process.create_time())
    except OSError:
        print(colored("Error> Can't make time stamp for monitoring process", "red"))

    try:
        executive_cores = len(main_process.cpu_affinity())
    except psutil.AccessDenied:
        executive_cores = 0

    try:
        memory_usage = get_size_form_bytes(main_process.memory_full_info().uss)
    except psutil.AccessDenied:
        memory_usage = 0

    try:
        priority = int(main_process.nice())
    except psutil.AccessDenied:
        priority = 0

    cpu_usage = main_process.cpu_percent()
    status = main_process.status()
    io_counters = main_process.io_counters()
    total_read_bytes = get_size_form_bytes(io_counters.read_bytes)
    total_write_bytes = get_size_form_bytes(io_counters.write_bytes)

    _table = tabulate({
        "Name": [
            "pid", "Executive cores", "Create time", "CPU usage", "Memory usage", "Status", "Total read bytes",
            "Total write bytes"
        ],
        "Values": [
            pid, executive_cores, create_time, cpu_usage, memory_usage, status, total_read_bytes, total_write_bytes
        ]
    }, headers="keys", showindex="always", tablefmt="simple")

    print(_table)
