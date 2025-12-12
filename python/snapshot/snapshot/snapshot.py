"""
Make snapshot

{"Tasks": {"total": 440, "running": 1, "sleeping": 354, "stopped": 1, "zombie": 0},
"%CPU": {"user": 14.4, "system": 2.2, "idle": 82.7},
"KiB Mem": {"total": 16280636, "free": 335140, "used": 11621308},
"KiB Swap": {"total": 16280636, "free": 335140, "used": 11621308},
"Timestamp": 1624400255}
"""

import argparse
from collections import Counter
import datetime
import json
import time
import psutil


class Monitor:
    def __init__(self, interval=30):
        self.interval = interval
        self.snapshots_taken = 0

    def get_tasks(self):
        processes = list(psutil.process_iter(["status"]))
        status_counts = Counter(p.info["status"] for p in processes)

        return {
            "total": len(processes),
            "running": status_counts.get(psutil.STATUS_RUNNING, 0),
            "sleeping": status_counts.get(psutil.STATUS_SLEEPING, 0),
            "stopped": status_counts.get(psutil.STATUS_STOPPED, 0),
            "zombie": status_counts.get(psutil.STATUS_ZOMBIE, 0),
        }

    def get_cpu_percentage(self):
        cpu_times = psutil.cpu_times_percent()
        return {
            "user": cpu_times.user,
            "system": cpu_times.system,
            "idle": cpu_times.idle,
        }

    def get_memory(self):
        memory = psutil.virtual_memory()
        return {
            "total": memory.total // 1024,
            "free": memory.free // 1024,
            "used": memory.used // 1024,
        }

    def get_swap(self):
        swap = psutil.swap_memory()
        return {
            "total": swap.total // 1024,
            "free": swap.free // 1024,
            "used": swap.used // 1024,
        }

    def create_snapshot(self):
        snapshot = {}

        snapshot["Tasks"] = self.get_tasks()
        snapshot["%CPU"] = self.get_cpu_percentage()
        snapshot["KiB Mem"] = self.get_memory()
        snapshot["KiB Swap"] = self.get_swap()

        timestamp = int(datetime.datetime.now().timestamp())
        snapshot["Timestamp"] = timestamp

        return snapshot


def main():
    """Snapshot tool."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        help="Interval between snapshots in seconds",
        type=int,
        default=30,
    )
    parser.add_argument("-f", help="Output file name", default="snapshot.json")
    parser.add_argument(
        "-n", help="Quantity of snapshot to output", default=20
    )
    args = parser.parse_args()

    monitor = Monitor(interval=args.i)

    count = int(args.n)
    open(args.f, "w").close()
    with open(args.f, "a") as file:
        while monitor.snapshots_taken < count:
            snapshot = monitor.create_snapshot()
            json.dump(snapshot, file)
            file.write("\n")

            print(snapshot, end="\r")
            monitor.snapshots_taken += 1

            if monitor.snapshots_taken < count:
                time.sleep(args.i)


if __name__ == "__main__":
    main()
