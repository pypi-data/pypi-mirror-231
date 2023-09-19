import json
import requests
from support_toolbox.utils import select_resource, select_api_url


# Clear User/Edit Layer on entire resource
def clear_user_layer(api_token, org, iri, resource_type, customer_url):
    url = f"{customer_url}/metadata/{org}/resources/clear"

    header = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_token}'
    }

    clear_resource_data = {
        "resources": [iri],
        "resourceType": resource_type
    }

    body = json.dumps(clear_resource_data)
    response = requests.post(url, body, headers=header)

    # Verify the deletion
    if response.status_code == 200:
        print(f"Successfully cleared the User Layer for: {iri}")
    else:
        print(response.text)


def run():
    api_url = select_api_url("public")
    api_token = input("Enter your API Token for the site you are looking to clear the user layer of a resource on: ")
    org = input("Enter the org_id the resource is in: ")
    iri = input("Enter the resource iri: ")
    resource_type = select_resource()
    clear_user_layer(api_token, org, iri, resource_type, api_url)
