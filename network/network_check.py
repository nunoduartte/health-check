import subprocess
import sys

class NetworkCheck:
    def __init__(self, ip):
        self.ip = ip
        self.data = dict()

    def run(self):
        result = subprocess.run(
            ['ping', '-c', '10', self.ip],
            text=True,
            capture_output=True,
            check=True
        )

        average = 0
        max = sys.float_info.min
        min = sys.float_info.max
        for line in result.stdout.splitlines():
            if "icmp_seq" in line:
                timing = float(line.split('tempo=')[-1].split( )[0])
                if timing > max:
                    max = timing
                if timing < min:
                    min = timing
                average = average + timing

        average = average / 30
        result = (min, max, average)
        return result
