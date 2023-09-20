import json
import requests
from support_toolbox.utils import select_resource, select_api_url


# Clear User/Edit Layer on entire resource
def clear_entire_user_layer(api_token, org, iris, resource_type, customer_url):
    url = f"{customer_url}/metadata/{org}/resources/clear"

    header = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_token}'
    }

    clear_resource_data = {
        "resources": iris,
        "resourceType": resource_type
    }

    body = json.dumps(clear_resource_data)
    response = requests.post(url, body, headers=header)

    # Verify the deletion
    if response.status_code == 200:
        print("Successfully cleared the User Layers for the following IRIs:")
        for iri in iris:
            print(iri)
    else:
        print(response.text)


# Clear User/Edit Layer on specific properties
def clear_property_user_layer(api_token, org, iri, resource_type, properties, customer_url):
    url = f"{customer_url}/metadata/{org}/resources/properties/clear"

    header = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_token}'
    }

    clear_resource_data = {
        "resource": iri,
        "resourceType": resource_type,
        "properties": properties
    }

    body = json.dumps(clear_resource_data)
    response = requests.put(url, body, headers=header)

    # Verify the deletion
    if response.status_code == 200:
        print("Successfully cleared the User Layer for the following IRI's Properties:")
        print(iri)
        for p in properties:
            print(p)
    else:
        print(response.text)


# Function to select the clear method
def clear_user_layer(api_token, org, iris, resource_type, customer_url):
    clear_method = input("Clear entire resource or specific properties? (e/p): ").strip().lower()

    if clear_method == "e":
        clear_entire_user_layer(api_token, org, iris, resource_type, customer_url)
    elif clear_method == "p":
        properties_input = input("Enter the properties to clear (comma-separated): ")
        properties = [prop.strip() for prop in properties_input.split(',')]

        for r in iris:
            clear_property_user_layer(api_token, org, r, resource_type, properties, customer_url)
    else:
        print("Invalid choice. Please enter 'e' or 'p'.")


def run():
    api_url = select_api_url("public")
    api_token = input("Enter your API Token for the selected customer: ")
    org = input("Enter the org ID where the resources are located: ")

    # Allow the user to input multiple IRIs as a comma-separated list
    iris_input = input("Enter the resource IRIs (comma-separated): ")
    iris = [iri.strip() for iri in iris_input.split(',')]

    resource_type = select_resource()
    clear_user_layer(api_token, org, iris, resource_type, api_url)
