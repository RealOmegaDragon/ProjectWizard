import dns.resolver
import dns.reversename
import dns.zone
import dns.query
from datetime import datetime

from core.output import save_to_file

def get_input_schema():
  return [
    ["Enter domain(s) (comma-separated for multiple): ", str, False, [True,","]]
  ]

def resolve_record(domain, record_type):
  try:
    answers = dns.resolver.resolve(domain, record_type)
    return [str(answer) for answer in answers]
  except dns.resolver.NoAnswer:
    return f"No {record_type} records found."
  except dns.resolver.NXDOMAIN:
    return f"Domain {domain} does not exist."
  except dns.exception.Timeout:
    return f"DNS query for {record_type} timed out."
  except Exception as e:
    return f"Error querying {record_type}: {str(e)}"

def reverse_lookup(ip):
  try:
    reversed_name = dns.reversename.from_address(ip)
    return str(dns.resolver.resolve(reversed_name, "PTR")[0])
  except dns.resolver.NoAnswer:
    return "No PTR records found."
  except dns.resolver.NXDOMAIN:
    return "No reverse DNS entry exists."
  except dns.exception.Timeout:
    return "Reverse DNS query timed out."
  except Exception as e:
    return f"Error during reverse lookup: {str(e)}"

def attempt_zone_transfer(domain):
  try:
    ns_records = resolve_record(domain, "NS")
    if isinstance(ns_records, list):
      for ns in ns_records:
        ns_server = str(ns).split()[-1]
        try:
          zone = dns.zone.from_xfr(dns.query.xfr(ns_server, domain))
          return {f"{domain} zone records": {name.to_text(): zone[name].to_text() for name in zone.nodes}}
        except Exception:
          continue
    return "Zone transfer unsuccessful or not allowed."
  except Exception as e:
    return f"Error during zone transfer: {str(e)}"

def dns_enum(domain):
  results = {}

  print(f"Starting DNS enumeration for {domain}...")
  record_types = ["A", "AAAA", "MX", "TXT", "CNAME", "NS"]

  for record_type in record_types:
    print(f"Querying {record_type} records...")
    results[record_type] = resolve_record(domain, record_type)

  if isinstance(results.get("A"), list):
    results["Reverse Lookup"] = {}
    for ip in results["A"]:
      print(f"Performing reverse lookup for {ip}...")
      results["Reverse Lookup"][ip] = reverse_lookup(ip)

  print("Attempting DNS zone transfer...")
  results["Zone Transfer"] = attempt_zone_transfer(domain)

  return results

def run(inputs):
  domains = inputs

  domain_list = []

  if not type(domains) is list:
    domain_list = [domains]
  else:
    domain_list = domains

  all_results = {"results": []}

  for domain in domain_list:
    print(f"\n=== Enumerating {domain} ===")
    results = dns_enum(domain)
    all_results["results"].append({"domain": domain, "scanresults": results})

  now = datetime.now()
  timestamp = now.strftime("%Y%m%d_%H%M%S")

  result_file = ".\\results\\dns_enum\\" + timestamp + ".json"
  save_to_file(all_results, result_file)

  return all_results
    