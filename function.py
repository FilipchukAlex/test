import requests
import simplejson


class CustomRequestError(Exception):
    pass


def get_json(api_endpoint: str):
    try:
        response = requests.get(api_endpoint)
        response.raise_for_status()
        return response.json()
    except (simplejson.JSONDecodeError, requests.exceptions.JSONDecodeError):
        raise CustomRequestError('Invalid json data')
    except requests.exceptions.RequestException:
        raise CustomRequestError('Invalid url, connection error, or http error')

