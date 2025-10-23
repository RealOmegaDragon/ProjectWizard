import nmap
import ipaddress
from datetime import datetime

from utilities import subnet_map
from core.output import save_to_file

def get_input_schema():
  return [
    ["Would you like to scan the network? (y/n): "],
    ["Enter target(s) (comma-separated for multiple): ", str, False, [True,","]]
  ]

def run(inputs):
  network, targets = inputs

  target_list = []

  if network.lower() != "y":
    if not type(targets) is list:
      target_list = [targets]
    else:
      target_list = targets
  else:
    target_list = subnet_map.run()

  scanner = nmap.PortScanner()
  results = {"results": []}

  # Sort targets by ipv4 address
  target_list.sort(key=lambda x: ipaddress.IPv4Address(x))

  for target in target_list:
    print(f"Starting port scan on {target}")
    
    scanner.scan(target, arguments="-O -sS -sV -R")
    target_results = []
    
    for host in scanner.all_hosts():
      print("Host:", host)
      print("Device Status:", scanner[host].state())

      # Get hostname
      hostname = scanner[host].hostname()

      # Get MAC address
      mac = scanner[host]['addresses'].get('mac', 'N/A')

      # Get OS details (best match, if available)
      os = "Unknown"
      osmatches = scanner[host].get('osmatch', [])
      if osmatches:
        os = osmatches[0]['name']

      for proto in scanner[host].all_protocols():
        print("Protocol: ", proto)
        for port in scanner[host][proto].keys():
          port_data = {
            "port": port,
            "state": scanner[host][proto][port]['state'],
            "name": scanner[host][proto][port]['name'],
            "product": scanner[host][proto][port]['product'],
            "version": scanner[host][proto][port]['version'],
            "extrainfo": scanner[host][proto][port]['extrainfo']
          }
          target_results.append(port_data)
          print("Port: ", port, "State: ", scanner[host][proto][port]['state'])

      results["results"].append({
        "ip": target,
        "macaddress": mac,
        "hostname": hostname,
        "operatingsystem": os,
        "scanresults": target_results
      })

  now = datetime.now()
  timestamp = now.strftime("%Y%m%d_%H%M%S")

  result_file = ".\\results\\port_scanner\\" + timestamp + ".json"
    
  save_to_file(results, result_file)

  return results

  