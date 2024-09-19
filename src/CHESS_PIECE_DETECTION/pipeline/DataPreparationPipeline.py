from CHESS_PIECE_DETECTION.components.DataPreparation import DataPreparation
from CHESS_PIECE_DETECTION.config.configuration import ConfigurationManager
from CHESS_PIECE_DETECTION import logger

STAGE_NAME = "DATA PREPARATION STAGE"

class DataPreparationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_preparation_config = config.get_data_preparation_config()
        data_preparation = DataPreparation(config=data_preparation_config)
        data_preparation.copying_data('datasets/artifacts/data_ingestion/train', 'datasets/artifacts/data_ingestion/test', 'datasets/artifacts/data_ingestion/valid')
        data_preparation.change_yaml('datasets/artifacts/data_ingestion/data.yaml')
    

if __name__ == '__main__':
    try: 
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataPreparationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e