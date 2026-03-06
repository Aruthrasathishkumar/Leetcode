import subprocess
from concurrent.futures import ThreadPoolExecutor

servers = ["server1.com", "server2.com", "server3.com"]
max_jobs = 10


def remote_task(server):
    """Run commands on remote server"""
    cmd = ["ssh", server, "uptime; df -h"]
    result = subprocess.run(cmd, capture_output=True, text=True)

    print(f"----- {server} -----")
    print(result.stdout)


def main():
    with ThreadPoolExecutor(max_workers=max_jobs) as executor:
        executor.map(remote_task, servers)


if __name__ == "__main__":
    main()