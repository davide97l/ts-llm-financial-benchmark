import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error
import os
import pandas as pd
from gluonts.dataset.pandas import PandasDataset
from gluonts.dataset.split import split


def plot_real_vs_predicted(real_value_series, pred_series):
    plt.figure(figsize=(12, 6))

    # Plot the real values
    plt.plot(real_value_series.index, real_value_series, color='blue', label='Real Values', linewidth=2)

    # Plot the predicted values
    plt.plot(pred_series.index, pred_series, color='orange', label='Predicted Values', linestyle='--', linewidth=2)

    # Adding titles and labels
    plt.title('Real Values vs Predicted Values')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid()
    plt.tight_layout()  # Adjust layout to prevent overlap

    # Show the plot
    plt.show()


def compute_metrics(pred, actual):
    def compute_directional_accuracy(pred, actual, only_sign=False):
        actual = actual.values if not isinstance(actual, np.ndarray) else actual
        pred = pred.values if not isinstance(pred, np.ndarray) else pred
        last_actual = actual[:-1]
        diff_pred = pred[1:] - last_actual
        diff_actual = actual[1:] - last_actual
        if only_sign:
            return np.mean(np.sign(pred) == np.sign(actual))
        else:
            return np.mean(np.sign(diff_pred) == np.sign(diff_actual))

    # Calculate directional accuracy
    directional_accuracy = compute_directional_accuracy(pred, actual)

    # Compute MSE, MAE, and MAPE
    mse = mean_squared_error(actual, pred)
    mae = mean_absolute_error(actual, pred)
    mape = np.mean(np.abs((actual - pred) / actual)) * 100  # Convert to percentage

    return mse, mae, mape, directional_accuracy


def load_datasets_from_folder(folder_path):
    datasets = {}
    
    # Iterate through all files in the specified folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv') or filename.endswith('.xlsx'):
            # Create the full file path
            file_path = os.path.join(folder_path, filename)
            # Load the dataset
            if filename.endswith('.csv'):
                df = pd.read_csv(file_path, index_col=0, parse_dates=True)
            else:
                df = pd.read_excel(file_path, index_col=0, parse_dates=True)
            # Use the filename without extension as the key
            dataset_name = os.path.splitext(filename)[0]
            datasets[dataset_name] = df
            
    return datasets


def prepare_ds_dataset(df, covariates, target_col, offset, prediction_length, windows, dist):
    # Create the PandasDataset
    ds = PandasDataset(
        df,
        feat_dynamic_real=covariates,
        target=target_col
    )

    # Split the dataset
    train, test_template = split(ds, offset=offset)

    # Generate test data instances
    test_data = test_template.generate_instances(
        prediction_length=prediction_length,  # number of time steps for each prediction
        windows=windows,  # number of windows in rolling window evaluation
        distance=dist,  # number of time steps between each window - distance=prediction_length for non-overlapping windows
    )
    
    return train, test_data, ds