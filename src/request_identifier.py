class RequestIdentifier:
    paths_and_requirements = {
        'login': {
            'source': str,
        },
        'confirm': {
            'source': str,
            'paymentnumber': int,
        },
        'sign': {
            'source': str,
            'documentid': str,
        },
    }

    def __init__(self, uri) -> None:
        self.uri = uri
        parsed_uri = self.parse_and_validate_uri(uri)
        self.path = parsed_uri['path']
        self.parameters = parsed_uri['parameters']
    
    def parse_parameters(self, input:str):
        parts = input.split('&')
        if len(parts) == 1 and parts[0] == '':
            raise ValueError('Parameters missing')
        result = {}
        for parameter in parts:
            parameter_parts = parameter.split('=')
            if len(parameter_parts) == 1 or parameter_parts[0] == '' or parameter_parts[1] == '':
                raise ValueError(f'Invalid parameter: {parameter}')
            key, value = parameter_parts
            result[key] = value
        return result

    def parse_and_validate_uri(self, uri:str) -> dict:
        parts = uri.split('://')
        scheme = parts[0]
        if not scheme == 'visma-identity':
            raise ValueError(f'Invalid URI scheme: {scheme}')
        parts = parts[1].split('?')
        path_name = parts[0]
        if not path_name in self.paths_and_requirements:
            raise ValueError(f'Invalid path: {path_name}')
        parameters_string = parts[1]
        parsed_parameters = self.parse_parameters(parameters_string)
        path_requirements = self.paths_and_requirements[path_name]

        if len(parsed_parameters.keys()) > len(path_requirements.keys()):
            raise ValueError(f'Too many parameters: {parameters_string}')
        parameters = {}
        for key in path_requirements:
            if key not in parsed_parameters:
                raise ValueError(f'Missing parameter: {key}')
            valid_type = path_requirements[key]
            try:
                parameter_value = valid_type(parsed_parameters[key])
                parameters[key] = parameter_value
            except ValueError:
                raise ValueError(f'Invalid parameter type: value for {key} is not {valid_type}')
        return {
            'path': path_name,
            'parameters': parameters
        }
