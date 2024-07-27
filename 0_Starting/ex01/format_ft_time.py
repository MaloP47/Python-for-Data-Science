import time
from datetime import datetime

now = time.time()

sec = f"{now:,.4f}"

sci = f"{now:.2e}"

nowFormat = datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {sec} or {sci} in scientific notation")
print(f"{nowFormat}")
