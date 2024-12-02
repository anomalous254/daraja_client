import requests
from datetime import datetime
from .utils import format_phone_number, generate_access_token, generate_stk_password

class DarajaClient:
    def __init__(self, auth_url: str, consumer_key: str, consumer_secret: str, pass_key: str, shortcode: str, phone_number: str, call_back_url: str, amount:str):
        """
        Initialize the MPESA Daraja 2.0 API client with required credentials and phone number.

        Args:
            url (str): The API base URL.
            consumer_key (str): Your consumer key for the API.
            consumer_secret (str): Your consumer secret for the API.
            pass_key (str): Security pass key for transactions.
            shortcode (str): Shortcode for transactions.
            phone_number (str): The phone number to format and validate.

        Raises:
            ValueError: If any required parameter is missing or invalid.
        """

        # Validate required parameters
        if not auth_url: raise ValueError("url cannot be empty!")
        if not consumer_key: raise ValueError("consumer_key cannot be empty!")
        if not consumer_secret: raise ValueError("consumer_secret cannot be empty!")
        if not pass_key: raise ValueError("pass_key cannot be empty!")
        if not shortcode: raise ValueError("shortcode cannot be empty!")
        if not phone_number: raise ValueError("phone_number cannot be empty!")
        if not call_back_url: raise ValueError("call_back_url cannot be empty!")
        if not amount: raise ValueError("amount cannot be empty!")


        # Initialize instance attributes
        self.auth_url = auth_url
        self.__consumer_key = consumer_key
        self.__consumer_secret = consumer_secret
        self.__pass_key = pass_key
        self.shortcode = shortcode
        self.phone_number = format_phone_number(phone_number)
        self.call_back_url = call_back_url
        self.amount = amount

    @property
    def consumer_key(self):
        """Get the consumer key (read-only)."""
        return self.__consumer_key

    @property
    def consumer_secret(self):
        """Get the consumer secret (read-only)."""
        return self.__consumer_secret

    @property
    def pass_key(self):
        """Get the pass key (read-only)."""
        return self.__pass_key
    

    def send_stk_push(self, stk_push_url: str):
        # Get the access token using the utility function
        token = generate_access_token(self.consumer_key, self.consumer_secret, self.auth_url)
        
        # Generate the STK password using the utility function
        stk_password = generate_stk_password(self.shortcode, self.pass_key)
        
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

        requestBody = {
            "BusinessShortCode": self.shortcode,
            "Password": stk_password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline", # "CustomerBuyGoodsOnline"
            "Amount": self.amount,
            "PartyA": self.phone_number,
            "PartyB": self.shortcode,
            "PhoneNumber": self.phone_number,
            "CallBackURL": self.call_back_url,
            "AccountReference": self.shortcode,
            "TransactionDesc": "MPESA ONLINE PAYMENT"
        }

        try:
            response = requests.post(stk_push_url, json=requestBody, headers=headers).json()
            response_code = response.get('ResponseCode')

            # Success
            if response_code == '0':
                return {
                    "message" : "success",
                    "stkpushID" : response.get("CheckoutRequestID"),
                    "info" : 'You can use and store this stkpushID in your db model to be used for payment confirm during callback from safaricom'
                }
            # failed
            if response_code != '0':
                return {
                    "message" : "failed",
                    "error" : response.get("errorMessage")
                }
            
            return {"message" : "request failed"}

        except Exception as e:
            print('Error:', str(e))
