
class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_json_data = response.json().get('data')
        self.response_status = response.status_code

    def validate_by_schema(self, schema):
        if isinstance(self.response_json_data, list):
            for item in self.response_json_data:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json_data)
        return self

    def validate_field(self, key, value):
        if isinstance(self.response_json_data, list):
            for item in self.response_json_data:
                assert item[key] == value
        else:
            assert self.response_json_data[key] == value
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    def __str__(self):
        return \
            f"\nStatus code: {self.response_status}\n" \
            f"Requested URL: {self.response.url}\n" \
            f"Response body: {self.response_json}"
