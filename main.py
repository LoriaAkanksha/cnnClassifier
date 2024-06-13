from cnnClassifier.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline
#from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
#from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
#from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline
from cnnClassifier import logger



STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e