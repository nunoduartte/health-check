import subprocess


def ping(ip):
    result = subprocess.run(
        ['ping', '-c', '30', ip],
        text=True,
        capture_output=True,
        check=True
    )

    for line in result.stdout.splitlines():
        if "icmp_seq" in line:
            timing = line.split('tempo=')[-1]
            print(ip, timing)

if __name__ == '__main__':
    ping("8.8.8.8")


