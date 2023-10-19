import os
import sys 
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    # IF WE CREATE A MODEL AND WE WANT TO SAVE IT INTO A PICKEL FILE THEN THIS PATH WILL BE USED 
    preprocessing_obj_file_path = os.path.join("artifact","processor.pkl") 

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for transformation
        '''
        try:
            num_features = ["reading score",
                            "writing score"]

            cat_feature  = ["gender",
                            "race/ethnicity",
                            "parental level of education",
                            "lunch",
                            "test preparation course"]
            
            num_pipeline = Pipeline(
                steps = [
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )
            logging.info("The numerical pipeline has been created")

            cat_pipeline = Pipeline(
                steps = [
                    ("imputer",SimpleImputer(strategy='most_frequent')),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )
            logging.info("The categorical pipeline has been created")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,num_features),
                ("cat_pipelines",cat_pipeline,cat_feature)
                ]
            )

            logging.info("data has been preprocessed")
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_transformation(self,training_path,testing_path):
        try:
            train_df = pd.read_csv(training_path)
            test_df  = pd.read_csv(testing_path)

            logging.info("Reading of train and test data has been completed")

            preprocessing_obj = self.get_data_transformer_object()

            target_column = "math score"
            numerical_column = ["writing score",
                                "reading score"]
            
            # DROPPING THE TARGET FEATURE FROM THE TRAIN DF 
            training_input_features = train_df.drop(columns=[target_column],axis=1)

            # STORING THR TARGET FEATURE IN A VARIABLE FOR TRAINING
            training_target_input_feature = train_df[target_column]

            # DROPPING THE TARGET FEATURES FROM THE TEST DF
            test_input_feature = test_df.drop(columns=[target_column],axis=1)

            # STORING THE TARGET FEATURE IN A VARIABLE FOR TESTING
            test_target_input_feature = test_df[target_column]

            logging.info("train and target data split is completed")

            processed_input_training_feature = preprocessing_obj.fit_transform(training_input_features)
            processed_input_testing_feature = preprocessing_obj.transform(test_input_feature)

            logging.info("The data preprocessing stage has been completed")

            train_arr = np.c_[
                processed_input_training_feature,np.array(training_target_input_feature)
            ]
            logging.info("training data created")

            test_arr = np.c_[
                processed_input_testing_feature,np.array(test_target_input_feature)
            ]
            logging.info("testing data created")

            # THIS IS A METHOD WE CALLED FROM THE UTILS FILE AND WE ARE PASSING THE 2 PARAMETERS
            save_object (
                        file_path = self.data_transformation_config.preprocessing_obj_file_path,
                        obj = preprocessing_obj)
            logging.info("The object has been saved to the specific path")

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessing_obj_file_path
            )

        except Exception as e:
            CustomException(e,sys)