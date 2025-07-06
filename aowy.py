# Install library jika belum ada:
# pip install speedtest-cli psutil platform

import speedtest
import psutil
import platform
import os

def cek_speed():
    print("\n=== 🌐 CEK SPEED INTERNET ===")
    st = speedtest.Speedtest()
    st.get_best_server()
    download = st.download() / 1_000_000  # Mbps
    upload = st.upload() / 1_000_000      # Mbps
    ping = st.results.ping

    print(f"↓ Download : {download:.2f} Mbps")
    print(f"↑ Upload   : {upload:.2f} Mbps")
    print(f"↔ Ping     : {ping:.2f} ms")


def cek_spek():
    print("\n=== 🖥️ CEK SPEK VPS ===")
    uname = platform.uname()
    print(f"OS         : {uname.system} {uname.release}")
    print(f"Node Name  : {uname.node}")
    print(f"Processor  : {uname.processor}")
    print(f"CPU Cores  : {psutil.cpu_count(logical=False)} (Physical)")
    print(f"Threads    : {psutil.cpu_count(logical=True)} (Logical)")
    print(f"RAM Total  : {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
    disk_usage = psutil.disk_usage("/")
    print(f"Disk Total : {round(disk_usage.total / (1024**3), 2)} GB")
    print(f"Disk Free  : {round(disk_usage.free / (1024**3), 2)} GB")


if __name__ == "__main__":
    cek_spek()
    cek_speed()
