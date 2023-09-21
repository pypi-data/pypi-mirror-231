from typing import List, Optional
from openapi_client.configuration import Configuration
from openapi_client.api_client import ApiClient
from openapi_client.models import EventInput, LoginRequestSchema
from openapi_client.apis.tags import events_api, auth_api
from openapi_client.model.send_events_request_schema import SendEventsRequestSchema

class WeftClient:
    def __init__(self, host: str):
        self.__access_token = None
        self.__host = host

    def __build_auth_api(self):
        configuration = Configuration(self.__host)
        client = ApiClient(configuration)
        
        return auth_api.AuthApi(client)

    def __build_events_api(self, host: str):
        configuration = Configuration(host=host)

        if self.__access_token is None:
            raise Exception('No Weft access token set. Please login first by using the login function.')

        client = ApiClient(configuration, header_name='Authorization', header_value=f'Bearer {self.__access_token}')
        
        return events_api.EventsApi(client)

    def login(self, access_key_id: str):
        """
        Get new access token from refresh token (access token expires after 1 hour)

        Args:
            refresh_token (str): refresh token
        
        Returns:
        str: access token
        """
        

        auth_api = self.__build_auth_api()
        refresh_token_input = LoginRequestSchema(refreshToken=access_key_id)

        refresh_response = auth_api.login(refresh_token_input)

        self.__access_token = refresh_response.body.get('token')        
    
    def send_events(self, events: List[EventInput]):
        """
        Send events to Weft

        Args:
            events ([EventInput]): events to send
        """

        events_api = self.__build_events_api(self.__host)
        send_events_request = SendEventsRequestSchema(events=events)

        return events_api.send_events(send_events_request)
