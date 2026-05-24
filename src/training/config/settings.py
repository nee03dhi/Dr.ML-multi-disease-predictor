from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_config = {"env_file": ".env", "extra": "ignore"}

    # Shared
    log_path: str = "logs/training.log"
    hyper_params_yaml_path: str = "src/training/config/best_hyperparams.yaml"
    test_size: float = 0.15
    random_state: int = 42

    # Diabetes
    diabetes_dataset_path: str = "data/diabetes.csv"
    diabetes_model_path: str = "models/diabetes_model.joblib"
    diabetes_target_col: str = "Outcome"

    # Heart Disease
    heart_disease_dataset_path: str = "data/heart_disease.csv"
    heart_disease_model_path: str = "models/heart_disease_model.joblib"
    heart_disease_target_col: str = "target"
