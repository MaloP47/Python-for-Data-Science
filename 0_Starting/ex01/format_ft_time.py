import time
from datetime import datetime
from colorama import Fore, init, Style

init()

now = time.time()

inSec = f"{now:,.4f}"

sci = f"{now:.2e}"

nowFormat = datetime.now().strftime("%b %d %Y")

print(Fore.BLUE + f"Seconds since January 1, 1970:" + Style.RESET_ALL + f" {inSec} or {sci} in scientific notation")
print(f"{nowFormat}")
