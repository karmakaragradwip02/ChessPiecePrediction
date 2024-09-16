import shutil
import os
import yaml
from CHESS_PIECE_DETECTION import logger

class DataPreparation:
    def __init__(self, config):
        self.config = config
    
    def copying_data(self, train_path, test_path, val_path):
        train_folder = self.config.train_dir
        test_folder = self.config.test_dir
        val_folder = self.config.val_dir
        try:
            os.makedirs(train_folder, exist_ok=True)
            os.makedirs(test_folder, exist_ok=True)
            os.makedirs(val_folder, exist_ok=True)
            logger.info("Created validation, test, and train folders")
        except Exception as e:
            raise e

        paths = [train_folder, test_folder, val_folder]
        source = [train_path, test_path, val_path]
        for path, src in zip(paths, source):
            try:
                if not os.path.exists(path):
                    os.makedirs(path)
                shutil.copytree(src, path, dirs_exist_ok=True)
                logger.info(f"Folder copied successfully from {src} to {path}")
            except Exception as e:
                logger.info(f"Error occurred while copying folder: {e}")
    def change_yaml(self):
        train_folder = self.config.train_dir
        test_folder = self.config.test_dir
        val_folder = self.config.val_dir
        data_yaml = 'artifacts/data_ingestion/data.yaml'

        try:
            with open(data_yaml, 'r') as file:
                config_data = yaml.safe_load(file)

            config_data['train'] = train_folder+f'/images'
            config_data['val'] = val_folder+f'/images'
            config_data['test'] = test_folder+f'/images'

            with open(data_yaml, 'w') as file:
                yaml.safe_dump(config_data, file)

            logger.info("YAML file updated successfully.")

            artifacts_dir = self.config.data_yaml
            os.makedirs(artifacts_dir, exist_ok=True)
            dest_path = os.path.join(artifacts_dir, os.path.basename(data_yaml))
            shutil.copy(data_yaml, dest_path)
            logger.info(f"YAML file copied to {dest_path}")

        except Exception as e:
            logger.info(f"Error while updating YAML file: {e}")