import requests
import json


class Questions:
    def raw_data(self):
        parameters = {
            'amount': 10,
            'type': 'multiple'
        }
        response = requests.get('https://opentdb.com/api.php', params=parameters)
        json_data = response.json()
        responce_code = json_data['response_code']
        questions_data = json_data['results']
        
        print(responce_code)
        print(json.dumps(questions_data, indent=4))
        
        return questions_data
    
    def shuffle_questions(self):
        pass

    def create_question_set(self):
        pass


class Quiz:
    pass



q = Questions()
q.raw_data()