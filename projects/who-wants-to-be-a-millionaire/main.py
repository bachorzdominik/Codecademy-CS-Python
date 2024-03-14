import requests
import json
import sys
import random
import html


class Questions:
    def __init__(self, amount=5, difficulty='easy', type='multiple', category=None):
        self.parameters = {
            'amount': amount,
            'difficulty': difficulty,
            'type': type,
            'category': category
        }
        self.categories = self.get_categories()
        self.raw_data = self.raw_data()

    def raw_request(self):
        result = requests.get('https://opentdb.com/api.php', params=self.parameters)
        print(result.url)
        if result.status_code == 200:
            return result
        else:
            raise Exception('Error: Unable to fetch data from the server')

    def raw_data(self):
        response = self.raw_request()
        return response.json()['results']
    
    def get_categories(self):
        result = requests.get('https://opentdb.com/api_category.php')
        if result.status_code == 200:
            return result.json()['trivia_categories']
        else:
            raise Exception('Error: Unable to fetch data from the server')
        
    def choose_category(self):
        print('Choose a category')
        for i in self.categories:
            print(f"{i['id']}. {i['name']}")
        category = int(input('Enter the category number: '))
        self.parameters['category'] = category

    def create_question_set(self):
        q_and_a_set_collection = []
        for data in self.raw_data:
            q_and_a_set = {}
            answers = data['incorrect_answers']
            correct_answer = data['correct_answer']

            answers.insert(random.randint(0, len(answers)), correct_answer)
            
            q_and_a_set['question'] = html.unescape(data['question']),
            q_and_a_set['answers'] = [html.unescape(answer) for answer in answers],
            q_and_a_set['correct_answer'] = html.unescape(data['correct_answer'])

            q_and_a_set_collection.append(q_and_a_set)

        return q_and_a_set_collection

easy_questions = Questions(category=18)
for q in easy_questions.create_question_set():
    print(q)