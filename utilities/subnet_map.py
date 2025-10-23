import nmap
import socket
import ipaddress
import psutil

def get_local_subnet():
    try:
        # Connect to a public IP to determine default interface
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]

        for _, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family.name == 'AF_INET' and addr.address == local_ip:
                    network = ipaddress.IPv4Network(f"{addr.address}/{addr.netmask}", strict=False)
                    return str(network)
    except Exception as e:
        print(f"Error detecting subnet: {e}")
    return None

def run():
  nm = nmap.PortScanner()

  subnet = get_local_subnet()

  if not subnet:
    print("[-] Could not detect a local subnet")
  try:
    print(f"[+] Scanning subnet: {subnet}")
    nm.scan(hosts=subnet,arguments='-sn -PR -PS22,80,443 -PA21,23,80,3389')
    live_hosts = [host for host in nm.all_hosts() if nm[host].state() == 'up']

    return live_hosts
  except Exception as e:
    print(f"[-] Error scanning network: {e}")
    return []