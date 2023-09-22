import requests

BASE_URL = "https://app.chipp.ai/api/public"

class User:
    def __init__(self, user_id: str, api_key: str):
        self.user_id = user_id
        self.api_key = api_key
        self.token_balance = None

        self.token_balance = self.get_chipps()

    def get_chipps(self) -> int:
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.get(f'{BASE_URL}/user/{self.user_id}', headers=headers)

        response.raise_for_status()
        
        return response.json()['tokenBalance']

    def deduct_chipps(self, quantity: int):
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        data = {
            'tokenQty': quantity,
            'consumerIdentifier': self.user_id
        }
        response = requests.post(f'{BASE_URL}/transactions', headers=headers, json=data)
        
        if self.token_balance is None:
            self.token_balance = self.get_chipps()
        self.token_balance -= quantity

    def get_payment_url(self, return_to_url: str = None) -> str:
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        url = f'{BASE_URL}/user/{self.user_id}/payment-url'
        if return_to_url:
            url += f'?returnToUrl={return_to_url}'
        response = requests.get(url, headers=headers)
        
        return response.json()['url']

    def get_packages_url(self, return_to_url: str = None) -> str:
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        url = f'{BASE_URL}/packages-url/?consumerIdentifier={self.user_id}'
        if return_to_url:
            url += f'?returnToUrl={return_to_url}'
        response = requests.get(url, headers=headers)
        
        return response.text

class Chipp:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def create_user(self, user_id: str) -> User:
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        data = {
            'consumerIdentifier': user_id
        }
        response = requests.post(f'{BASE_URL}/user', headers=headers, json=data)
        
        return User(user_id, self.api_key)

    def get_user(self, user_id: str) -> User:
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.get(f'{BASE_URL}/user/{user_id}', headers=headers)
        
        return User(user_id, self.api_key)
