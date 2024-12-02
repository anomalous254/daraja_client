from daraja_client.core  import DarajaClient
from decouple import config

url= "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
stk_push_url ='https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
call_back_url = 'https://amdeveloper-dpbzakb7gmg0ftgg.canadacentral-01.azurewebsites.net'
phone_number = '++254769507699'
amount=1
      
cl =  DarajaClient(
            auth_url=url, 
            consumer_key= config('DARAJA_API_CONSUMER_KEY') , 
            consumer_secret=config('DARAJA_API_CONSUMER_SECRET'), 
            pass_key=config('DARAJA_API_PASS_KEY'),
            shortcode=config('DARAJA_API_SHORT_CODE'),
            phone_number=phone_number,
            call_back_url=call_back_url,
            amount=amount
)


if __name__ == '__main__':
    response = cl.send_stk_push(stk_push_url=stk_push_url)
    print(response)
