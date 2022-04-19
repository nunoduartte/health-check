import subprocess

class NetworkCheck:
    def __init__(self, ip):
        self.ip = ip
        self.data = dict()
        self.data[ip] = []

    def run(self):
        result = subprocess.run(
            ['ping', '-c', '30', self.ip],
            text=True,
            capture_output=True,
            check=True
        )

        for line in result.stdout.splitlines():
            if "icmp_seq" in line:
                timing = line.split('tempo=')[-1]
                self.data[self.ip].append(timing)
        print(self.data[self.ip])
