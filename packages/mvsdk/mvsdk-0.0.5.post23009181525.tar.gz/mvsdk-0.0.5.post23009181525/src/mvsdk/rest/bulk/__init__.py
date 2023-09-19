class Bulk:

    def __init__(self, mv_sdk, base_url: str, domain: str):
        """
        Initialize the Asset Domain
        """
        super(Bulk, self)
        self.mv_sdk = mv_sdk
        self.base_url = base_url
        self.domain = domain

    def post(self, params=None, data=None, headers=None, auth=None, object_id=None,
             domain_id=None, domain_action=None):
        """

        """
        headers = headers or {}

        return self.mv_sdk.request(
            'post',
            self.base_url,
            self.domain,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            object_id=object_id,
            domain_id=domain_id,
            domain_action=domain_action
        )


class BulkContainer:
    def __init__(self):
        self.bulk_requests = []

    def add_request(self, request):
        self.bulk_requests.append(request)

    def get_all_requests(self):
        return self.bulk_requests

    def get_bulk_body(self):
        bulk_requests = {}

        boundary_string = 'c6c2ed020aadd284efd61a7c9d4dfe94'

        bulk_requests['headers'] = {
            'Content-Type': f'multipart/mixed; boundary={boundary_string}'
            }

        bulk_request_payloads = []

        for request in self.bulk_requests:
            bulk_request = '\r\n'.join(
                                    f'--{boundary_string}'
                                    'Content-Type: application/http; msgtype=request\r\n'
                                    f'{request["method"]} {request["uri"]} HTTP/1.1'
                                    f'host: {request["headers"]["Host"]}'
                                    f'Authorization: {request["headers"]["Authorization"]}'
                                    f'content-type: {request["headers"]["Content-Type"]}'
                                    )

            if request['data']:
                bulk_request += f'\r\n{request["data"]}\r\n'

            bulk_request_payloads.append(bulk_request)

        bulk_request_payloads.append(f'\r\n\r\n--{boundary_string}--')
        bulk_request_payload = '\n'.join(bulk_request_payloads)
        bulk_requests['payload'] = bulk_request_payload.encode(encoding='UTF-8', errors='strict')

        return bulk_requests
