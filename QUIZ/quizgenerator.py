import configparser
import json
import os
import requests
from tqdm import tqdm
from datetime import datetime


class Quiz:
    def __init__(self, config_file):
        self.config_file = config_file
        self.data = None
        self.uri = ''
        self.json_file_name = 'data.json'
        self.load_config()
        self.answers_data = []
        self.initial_answers = []

    def load_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        self.uri = config['APP']['URL']
        self.json_file_name = config['APP']['JSON_FILE_NAME']

    def download_file(self):
        if os.path.isfile(self.json_file_name):
            return
        else:
            response = requests.get(self.uri, stream=True)
            with open(self.json_file_name, "wb") as handle:
                for data in tqdm(response.iter_content()):
                    handle.write(data)

    def parse_json_data(self):
        with open(self.json_file_name) as json_file:
            self.data = json.load(json_file)

    def initial_questions(self):
        questions = ["Name", "Lastname"]

        for i in range(len(questions)):
            self.initial_answers.append({questions[i]: input(questions[i] + "\t")})

    def __check_input(self, answer_key):

        dic = ['A', 'B', 'C', 'D', 'E']
        if answer_key not in dic:
            print("Invalid input. Please try again ex.( 'A' )")
            self.iter_questions()
        else:
            temp = dic.index(answer_key)
        return temp

    def iter_questions(self):
        dic = ['A', 'B', 'C', 'D', 'E']
        for item in self.data['exam_content']:
            line = ""
            for index, answer in enumerate(item['answers']):
                line += "\n" + dic[index] + "\t" + answer + ""
            question = item['question']
            answer_key = input(question + line)
            answer_index = self.__check_input(answer_key)
            selected_answer = line.replace(dic[answer_index], "*" + dic[answer_index])
            self.answers_data.append({question: selected_answer})

    def write_answers(self):
        name = self.initial_answers[0]['Name']
        lastname = self.initial_answers[1]['Lastname']
        date = datetime.now()
        with open(name + "_" + lastname + ".txt", 'w') as answer_file:
            answer_file.write(name)
            answer_file.write(lastname)
            answer_file.write(str(date))
            for i in range(len(self.answers_data)):
                line = ''.join(['%s ==> %s' % (key, value) for (key, value) in self.answers_data[i].items()])
                answer_file.write(line + "\n")


if __name__ == '__main__':
    quiz = Quiz("url.ini")
    quiz.download_file()
    quiz.parse_json_data()
    quiz.initial_questions()
    quiz.iter_questions()
    quiz.write_answers()
