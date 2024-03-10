import requests
import json
import sys
import random


class Questions:
    def __init__(self, amount=5, difficulty='easy', type='multiple', category=None):
        self.parameters = {
            'amount': amount,
            'difficulty': difficulty,
            'type': type,
            'category': category
        }
        self.categories = self.get_categories()

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
        
    def shuffle_questions(self):
        pass

    def create_question_set(self):
        pass


easy_questions = Questions(category=None)
easy_questions.choose_category()
questions = easy_questions.raw_data()
for i in questions:
    print(i['question'])
    print(i['correct_answer'])
    print(i['incorrect_answers'])
    print()
