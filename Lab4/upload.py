from pycti import OpenCTIApiClient
from stix2 import TLP_GREEN
from datetime import datetime
from os import environ
from dotenv import load_dotenv

load_dotenv()
date = datetime.today().strftime("%Y-%m-%dT%H:%M:%SZ")

api_url = 'http://localhost:8080'
api_token = environ.get('OPENCTI_ADMIN_TOKEN')
client = OpenCTIApiClient(api_url, api_token)

TLP_GREEN_CTI = client.marking_definition.read(id=TLP_GREEN["id"])
with open('hosts', 'r') as f:
    domains = f.read().splitlines()
count = 1
for domain in domains:
    indicator = client.indicator.create(
    name="Malicious domain {}".format(count),
    description="domains",
    indicator_types=["malicious-activity"],
    pattern_type="stix",
    pattern="[domain-name:value = '{}']".format(domain),
    x_opencti_main_observable_type="IPv4-Addr",
    valid_from=date,
    update=True,
    markingDefinitions=[TLP_GREEN_CTI["id"]]
    )
    print("Created indicator with ID:", indicator["id"])
    count += 1 