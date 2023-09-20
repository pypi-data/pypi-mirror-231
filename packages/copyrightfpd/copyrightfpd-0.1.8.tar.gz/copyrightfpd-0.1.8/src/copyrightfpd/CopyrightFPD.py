from joblib import load
import pkg_resources
import spacy
import os
import re

class CopyrightFPD:
    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        fpd_path = pkg_resources.resource_filename(__name__, 'models/false_positive_detection_model.pkl')
        vectorizer_path = pkg_resources.resource_filename(__name__, 'models/false_positive_detection_vectorizer.pkl')
        ner_model_path = pkg_resources.resource_filename(__name__, 'models/ner_model')
        self.fpd = load(fpd_path)
        self.vectorizer = load(vectorizer_path)
        self.ner_model = spacy.load(ner_model_path)

    def preprocess_data(self, data):
        # Initial preprocessing
        if type(data) is not list:
            data = data.to_list()
        for i in range(len(data)):
            data[i] = str(data[i])

        # Replace entities with ENTITY
        data = [self.ner_model(sentence) for sentence in data]
        new_data = []
        for sentence in data:
            new_sentence = sentence.text
            for entity in sentence.ents:
                if entity.label_ == 'ENT':
                    new_sentence = re.sub(re.escape(entity.text), ' ENTITY ', new_sentence)
            new_data.append(new_sentence)
        data = new_data
        
        # replace dates (e.g. 2007) with DATE
        data = [re.sub(r'\d{4}', ' DATE ', sentence) for sentence in data]

        # remove numbers
        data = [re.sub(r'\d+', ' ', sentence) for sentence in data]

        # replace copyright symbols ( ©, (c), and (C) ) with 
        symbol_text = ' COPYRIGHTSYMBOL '
        data = [re.sub(r'©', symbol_text, sentence) for sentence in data]
        data = [re.sub(r'\(c\)', symbol_text, sentence) for sentence in data]
        data = [re.sub(r'\(C\)', symbol_text, sentence) for sentence in data]

        # replace emails with EMAIL
        email_text = ' EMAIL '
        data = [re.sub("""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""", email_text, sentence) for sentence in data]

        # remove any special characters not already replaced or removed
        data = [re.sub(r'[^a-zA-Z0-9]', ' ', sentence) for sentence in data]

        # Change any remaining text to lowercase
        data = [sentence.lower() for sentence in data]

        # Remove any extra whitespaces remaining in the text
        data = [re.sub(r' {2,}', ' ', sentence) for sentence in data]

        # vectorize the data using the pre trained TF-IDF vectorizer
        data = self.vectorizer.transform(data)
        
        # return the fully prerocessed and transformed data
        return data

    def predict(self, data, threshold=0.99):
        # preprocess the data
        data = self.preprocess_data(data)

        # predict the data
        if self.fpd.get_params()['estimator'].probability:
            predictions = self.fpd.predict_proba(data)
            predictions = ['f' if prediction[1] >= threshold else 't' for prediction in predictions]
        else:
            predictions = self.fpd.predict(data)
            predictions = ['f' if prediction == 1 else 't' for prediction in predictions]

        # return the predictions
        return predictions
