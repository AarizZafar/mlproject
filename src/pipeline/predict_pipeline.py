import sys 
import pandas as pd
from src.utils import load_object 
from src.exception import CustomException
from src.components.data_transformation import DataTransformation

transformation = DataTransformation().get_data_transformer_object()

class PredictPipeline:
    def __init__(self):
        pass

    def prediction(self,feature):
        try:
            model_path        = 'artifact\model.pkl'
            processing_path   = 'artifact\processor.pkl'

            model             = load_object(file_path = model_path)
            processor         = load_object(file_path = processing_path)

#           PRINTING THE FEATURES TO SEE IT AS A DATA FRAME
            print(feature)

            data_scaled       = processor.transform(feature)

            pred = model.predict(data_scaled)
            
            return pred

        except Exception as e:
            CustomException(e,sys)

# MAPPING ALL THE INPUTS THAT WE GET FROM THE HTML TO THE BACKEND
class CustomData:
    def __init__(self,
                gender:str,
                race_ethnicity:str,
                parental_level_of_education,
                lunch:str,
                test_preparation_course:str,
                reading_score: int,
                writing_score: int):
        
        self.gender                     = gender
        self.race_ethnicity             = race_ethnicity
        self.parental_level_education   = parental_level_of_education
        self.lunch                      = lunch
        self.test_preparation_course    = test_preparation_course
        self.reading_score              = reading_score
        self.writing_score              = writing_score

    # THE DATA THAT WE RECEIVE FROM THE HTML FILE WE SHOW IT IN THE FORM OF A DATA FRAME
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                'Gender'                      : [self.gender],
                'Race_ethnicity'              : [self.race_ethnicity],
                'Parental_level_of_education' : [self.parental_level_education],
                'Lunch'                       : [self.lunch],
                'Test_preparation_course'     : [self.test_preparation_course],
                'Reading_score'               : [self.reading_score],
                'Writing_score'               : [self.writing_score]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e,sys)
        

