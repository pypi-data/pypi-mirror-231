import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.login import Login
from openapi_client.apis.paths.events import Events

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.LOGIN: Login,
        PathValues.EVENTS: Events,
    }
)

path_to_api = PathToApi(
    {
        PathValues.LOGIN: Login,
        PathValues.EVENTS: Events,
    }
)
