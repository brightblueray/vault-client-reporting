import os
import requests
import json
import datetime
import pprint
import csv
# import pandas

# Set Environment
os.environ['VAULT_ADDR'] =  'http://127.0.0.1:8200'
# os.environ['VAULT_TOKEN'] = 'hvs.4O3Nh0I75YUMdZZS99cJt8xk'
os.environ['VAULT_TOKEN'] = 'hvs.CAESIPA6tTKqzn_UiXnRRmstt7nuhJYadG_ed7itSZbBo-pyGh4KHGh2cy54MTlhZmt0cGFnOHF0bjBCQVRVdVhFcHE'

token = os.getenv('VAULT_TOKEN')
base_url = os.getenv('VAULT_ADDR')


# Build Auth-Lookup Table
auth_url = f"{base_url}/v1/sys/auth"
headers = {
    "X-Vault-Token": token,
    "accept": "*/*"
}

auth_lookup = {}
response = requests.get(auth_url, headers=headers)
data = response.json()
for path, auth_info in data.items():
    if isinstance(auth_info, dict) and 'accessor' in auth_info and 'type' in auth_info:
        accessor = auth_info['accessor']
        auth_type = auth_info['type']
        auth_lookup[accessor] = {"path": path, "type": auth_type}

# headers = {
#     "X-Vault-Token": token
# }

url = f'{base_url}/v1/sys/internal/counters/activity/export'
response = requests.get(url, headers=headers)
lines = response.text.strip().split("\n")

client_data= []
for line in lines:
    try: 
        data = json.loads(line)
        timestamp = data.get('timestamp', 0)
        human_ts = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        # print (human_ts)
        # data['timestamp'] = human_ts
        data['date'] = human_ts
        data['auth_type'] = auth_lookup[data.get('mount_accessor')]['type']
        data['auth_path'] = auth_lookup[data.get('mount_accessor')]['path']
        client_data.append(data)
    except json.JSONDecodeError as e:
        print (f"Error decoding JSON: {e}")

# Add Entity Details
entity_url_template = f"{base_url}/v1/identity/entity/id/{{client_id}}"

for client in client_data:
    print (client)
    client_id = client['client_id']
    mount_accessor = client['mount_accessor']
    entity_url = entity_url_template.format(client_id=client_id)
    isNonEntity = client.get('non_entity', False)
    
    if isNonEntity:
        print ("non-entity")
        client['name'] = "Non-Entity"
    else:
        print ("entity")
        entity_response = requests.get(entity_url, headers=headers)
        entity_data = entity_response.json()
        for alias in entity_data.get('data',{}).get('aliases',[]):
            if alias.get('mount_accessor') == mount_accessor:
                client['name'] = alias.get('name')
                break

pprint.pprint(client_data, indent=4)


# Rearrange columns order
reordered_fieldnames = [
    'timestamp', 'date', 'namespace_id', 'auth_type', 'auth_path', 'name', 'non_entity', 'mount_accessor', 'client_id'
]

# Output to CSV with reordered columns
csv_file = 'client_data.csv'

with open(csv_file, 'w', newline='') as f:
    csv_writer = csv.DictWriter(f, fieldnames=reordered_fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(client_data)

print(f"Data written to {csv_file}")