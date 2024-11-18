
# MPESA Daraja 2.0 API Python Client Module

This python module provides a simple way to integrate the Safaricom MPESA Daraja 2.0 API into your Python projects. It is designed to handle common operations like generating access tokens, formatting phone numbers, and sending STK Push requests.

## Features

- Generate access tokens securely.
- Format and validate phone numbers.
- Send STK Push requests for payments.
- Easily configurable with environment variables.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/anomalous254/daraja_client.git
   ```

2. Navigate to the project directory:
   ```bash
   cd daraja_client
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Add the following variables to your `.env` file in the root directory of your project:

```env
DARAJA_API_CONSUMER_KEY='your_consumer_key'
DARAJA_API_CONSUMER_SECRET='your_consumer_secret'
DARAJA_API_PASS_KEY='your_pass_key'
DARAJA_API_SHORT_CODE='your_shortcode'
```

## Usage

### Import the Library

```python
from core import DarajaClient
from decouple import config

# Configuration
auth_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
stk_push_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
call_back_url = 'https://your-callback-url.com' # 
phone_number = '+254769507699' # person to receive the prompt

# Initialize the client
cl = DarajaClient(
    auth_url=auth_url,
    consumer_key=config('DARAJA_API_CONSUMER_KEY'),
    consumer_secret=config('DARAJA_API_CONSUMER_SECRET'),
    pass_key=config('DARAJA_API_PASS_KEY'),
    shortcode=config('DARAJA_API_SHORT_CODE'),
    phone_number=phone_number,
    call_back_url=call_back_url
)

# Send STK Push
response = cl.send_stk_push(stk_push_url=stk_push_url)
print(response)
```

## Response Examples

### Success

```json
{
    "message": "success",
    "stkpushID": "ws_CO_blahblahblah",
    "info": "You can use and store this stkpushID in your db model to be used for payment confirm during callback from Safaricom"
}
```

### Failure

```json
{
    "message": "failed",
    "error": "Wrong credentials"
}
```

## Acknowledgment

This library was developed by [Peter Nyando](https://nyando-tech.vercel.app/), a passionate software engineer dedicated to creating scalable and efficient solutions. Check out more of my work on my [portfolio](https://nyando-tech.vercel.app/).


Ensure your `.env` file is properly configured.



## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push to your fork and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
