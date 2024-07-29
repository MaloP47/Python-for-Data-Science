from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

print('###########################################')

for elem in ft_tqdm(range(99)):
    sleep(0.005)
print()
for elem in tqdm(range(99)):
    sleep(0.005)
print()

print('###########################################')

for elem in ft_tqdm(range(999)):
    sleep(0.005)
print()
for elem in tqdm(range(999)):
    sleep(0.005)
print()

print('###########################################')

for elem in ft_tqdm(range(9999)):
    sleep(0.005)
print()
for elem in tqdm(range(9999)):
    sleep(0.005)
print()

print('###########################################')

for elem in ft_tqdm(range(99999)):
    sleep(0.005)
print()
for elem in tqdm(range(99999)):
    sleep(0.005)
print()
