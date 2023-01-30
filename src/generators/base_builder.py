

class BuilderBaseClass:
    def __init__(self):
        self.result = {}

    def update_inner_value(self, keys, value):
        if not isinstance(keys, list):
            self.result[keys] = value
        else:
            current_json = self.result
            for item in keys[:-1]:
                if item not in current_json.keys():
                    current_json[item] = {}
                current_json = current_json[item]
            current_json[keys[-1]] = value
        return self

    def build(self):
        return self.result

