import whois
import time

from datetime import datetime

from core.output import save_to_file

def get_input_schema():
  return [
    ["Enter target(s) (comma-separated for multiple): ", str, False, [True,","]]
  ]

def whois_lookup(target, retries=3):
  for attempt in range(retries):
    try:
      # Perform WHOIS lookup
      return whois.whois(target)
    except whois.parser.PywhoisError as e:
      print(f"WHOIS server error for {target}: {e}. Retrying... ({attempt + 1}/{retries})")
    except Exception as e:
      print(f"General error for {target}: {e}. Retrying... ({attempt + 1}/{retries})")
      
    # Wait before retrying
    time.sleep(2)
  
  print(f"Failed to fetch WHOIS data for {target} after {retries} attempts.")
  return None

def run(inputs):
  targets = inputs

  target_list = []

  if not type(targets) is list:
    target_list = [targets]
  else:
    target_list = targets

  print(f"Running WHOIS lookup for targets: {target_list}")
  results = {"results": []}
  
  for target in target_list:
    print(f"\nFetching WHOIS data for: {target}")
    whois_data = whois_lookup(target)

    if whois_data:
      # Collect WHOIS information
      data = {
          "Domain Name": whois_data.domain_name,
          "Registrar": whois_data.registrar,
          "Creation Date": str(whois_data.creation_date),
          "Expiration Date": str(whois_data.expiration_date),
          "Nameservers": whois_data.name_servers,
          "Status": whois_data.status,
          "Admin Contact": whois_data.emails,
      }

      results["results"].append({"ip": target, "scanresults": data})

      # Display WHOIS data
      for key, value in data.items():
          print(f"{key}: {value}")
    else:
      results[target] = {"Error": "Failed to fetch WHOIS data"}

  now = datetime.now()
  timestamp = now.strftime("%Y%m%d_%H%M%S")

  result_file = ".\\results\\whois_lookup\\" + timestamp + ".json"
  save_to_file(results, result_file)

  return results