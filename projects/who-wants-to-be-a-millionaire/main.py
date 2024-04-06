import requests
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

    def fetch_data(self):
        self.raw_data = self.raw_data()
        
    def raw_request(self):
        result = requests.get('https://opentdb.com/api.php', params=self.parameters)
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
            
            q_and_a_set['question'] = html.unescape(data['question'])
            q_and_a_set['answers'] = [html.unescape(answer) for answer in answers]
            q_and_a_set['correct_answer'] = html.unescape(data['correct_answer'])

            q_and_a_set_collection.append(q_and_a_set)

        return q_and_a_set_collection


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.total_questions = len(questions)
        self.question_number = 0
        self.incorrect_answers = 3
    
    def display_question(self):
        print(f"Question {self.question_number + 1}: {self.questions[self.question_number]['question']}")
        for i, answer in enumerate(self.questions[self.question_number]['answers']):
            print(f"{i + 1}. {answer}")
        user_answer = int(input('Enter the number of the correct answer: '))
        self.check_answer(user_answer)
        self.question_number += 1
        if self.question_number < self.total_questions:
            self.display_question()
        else:
            self.end_quiz()


    def check_answer(self, user_answer):
        if self.questions[self.question_number]['answers'][user_answer - 1] == self.questions[self.question_number]['correct_answer']:
            print('Correct!')
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {self.questions[self.question_number]['correct_answer']}")
            self.incorrect_answers -= 1
            if self.incorrect_answers == 0:
                self.end_quiz()
                sys.exit()
            else:
                print(f"You have {self.incorrect_answers} incorrect answers left\n")

    def end_quiz(self):
        print(f"Your final score is {self.score}/{self.total_questions}")


def main():
    questions = Questions()
    questions.choose_category()
    questions.fetch_data()
    quiz = Quiz(questions.create_question_set())
    quiz.display_question()


if __name__ == "__main__":
    main()
