import psutil
import socket

print(f"System Memory used: {psutil.virtual_memory().used // (1024 ** 3)} GB")
print(f"System Memory available: {psutil.virtual_memory().available // (1024 ** 3)} GB")
print(f"System Memory total: {psutil.virtual_memory().total // (1024 ** 3)} GB")


print(f"Hostname: {socket.gethostname()}")

partitions = psutil.disk_partitions()

for part in partitions:
    mnt = part.mountpoint
    if "snap" in mnt or "boot" in mnt:
        continue
    disk = psutil.disk_usage(mnt)
    print(f"Usage at {mnt} on {part.device}: {disk.used // (1024 ** 3)} GB")
    print(f"Free at {mnt} on {part.device}: {disk.free // (1024 ** 3)}GB")
    print(f"Total at {mnt} on {part.device}: {disk.total // (1024 ** 3)}GB")
