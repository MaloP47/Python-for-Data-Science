"""Try to copy original tqdm function"""

import time
import os


def toTime(seconds: int) -> str:
    """Convert time to a formatted 00:00 string"""
    minutes, seconds = divmod(seconds, 60)
    return f"{int(minutes):02d}:{int(seconds):02d}"


def ft_tqdm(lst: range) -> None:
    """The function"""
    spe = '█'
    rangeLen = len(lst)
    start = time.time()
    if rangeLen <= 99:
        barWidth = os.get_terminal_size().columns - 38
    elif rangeLen <= 999:
        barWidth = os.get_terminal_size().columns - 40
    elif rangeLen <= 9999:
        barWidth = os.get_terminal_size().columns - 42
    else:
        barWidth = os.get_terminal_size().columns - 44

    for i, elem in enumerate(lst, 1):
        percent = i * 100 // rangeLen
        elapse = int(time.time() - start)
        if elapse == 0:
            elapse = 1
        speed = int(i / elapse)
        speedd = i / (time.time() - start)
        remaining = toTime(int((rangeLen - i) / speed))
        progress = int(i * barWidth / rangeLen)
        progressBar = f"{spe * progress:<{barWidth}}"
        norm = f"\r{percent}%|{progressBar}| {i}/{rangeLen} [{toTime(elapse)}"
        print(f"{norm}<{remaining}, {speedd:.2f}it/s]", end='', flush=True)
        yield i
    print()
