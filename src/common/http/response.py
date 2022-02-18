from src.common.http.rc import RC
from typing import List, Dict, Union, Any


class DataPackage:

    def __new__(cls, element: List, fields: Dict):
        if not element:
            element = []
        if not fields:
            fields = {}
        data = dict()
        data['element'] = element
        data['fields'] = fields
        return data


class JsonResponse:

    def __new__(cls, rc: int = RC.success.value, message: str = None, data: Union[DataPackage, Dict] = None,
                error: Any = None):
        response = dict()
        response['rc'] = rc
        response['message'] = message
        response['data'] = data
        response['error'] = error
        return response, rc
