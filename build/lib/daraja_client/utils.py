import base64
import requests
from datetime import datetime


def format_phone_number(phone_number: str) -> str:
    """
    Formats a phone number by removing the '+' prefix if present and validating the result.

    Args:
        phone_number (str): The phone number to format.

    Returns:
        str: The formatted phone number without the '+' prefix.

    Raises:
        ValueError: If the phone number contains invalid characters.
    """
    
    
    # Remove '+' prefix if present
    formatted_phone = phone_number.lstrip('+')

    # Check if the formatted phone number contains only digits
    if not formatted_phone.isdigit():
        raise ValueError("Invalid phone number format. Phone number must contain only digits.")
    
    return formatted_phone



def generate_access_token(consumer_key: str, consumer_secret: str, url: str) -> str:
    try:
        # Encode the credentials
        encoded_credentials = base64.b64encode(f"{consumer_key}:{consumer_secret}".encode()).decode()

        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/json"
        }

        # Send the request and parse the response
        response = requests.get(url, headers=headers).json()

        # Check for errors and return the access token
        if "access_token" in response:
            return response["access_token"]
        else:
            raise Exception("Failed to get access token: " + response["error_description"])
    except Exception as e:
        raise Exception("Failed to get access token: " + str(e)) 


def generate_stk_password(shortcode: str, passkey: str) -> str:
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    # Create the STK password
    stk_password = base64.b64encode((shortcode + passkey + timestamp).encode('utf-8')).decode('utf-8')
    return stk_password
