class CountVectorizer:

    def __init__(self):
        self.feature_list = list()  # Список уникальных фич (токенов).
        self.document_term_matrix = list()  # Терм-документная матрица.

    def create_feature_list(self, corpus: list) -> object:
        '''
        Метод создает список уникальных фич (токенов). Отдельной задаче - отдельный метод.
        '''
        for document in corpus:
            document_tokens = document.lower().rstrip().split(' ')  # Превращаем документ в список токенов.

            for token in document_tokens:
                if token not in self.feature_list:
                    self.feature_list.append(token)

        return self.feature_list  # Функция не обязана возвращать список фич, но лучше если функция что-то возвращает.

    def fit_transform(self, corpus: list) -> object:
        self.create_feature_list(corpus)

        for document in corpus:
            document_vector = [document.lower().count(token) for token in self.feature_list]
            self.document_term_matrix.append(document_vector)

        return self.document_term_matrix

    def get_feature_names(self) -> object:
        return self.feature_list


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    # Out: ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
    #       'fresh', 'ingredients', 'parmesan', 'to', 'taste']

    print(count_matrix)
    # Out: [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]