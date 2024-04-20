import json
import requests
from flask import Blueprint

product = Blueprint('product', __name__)


@product.route('/products/')
def get_product_details():
    urls = [
        'https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json',
        'https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json'
    ]
    headers = {}
    payload = {}
    result = {}
    for url in urls:
        response = requests.get(url, headers=headers, data=payload)
        json_response = response.json()
        records = json_response['contents'][0]['mainContent'][0]['contents'][0]['records']
        result[url] = []
        for each in records:
            result[url] += each['attributes']['product.displayName']

        # result[url] = [each['attributes']['product.displayName'] for each in records]

    # pretty_result = json.dumps(result, indent=4)

    return result
