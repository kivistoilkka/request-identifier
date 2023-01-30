from request_identifier import RequestIdentifier


class IdentifierClient:
    def __init__(self):
        pass

    def run(self):
        print('***  Request Identifier Client  ***\n')
        while True:
            user_input = input('Write your request URI, empty input stops the program:\n')
            if user_input == '':
                break
            print()
            try:
                result = RequestIdentifier(user_input)
                print(f'Path: {result.path}')
                print(f'Parameters: {result.parameters}')
            except ValueError as error:
                print('Error:')
                print(error)
            print('\n----------\n')
