# Timeseries Pretrained Models Financial Benchmark

This repository contains an evaluation of various pretrained time series large models on a diverse set of assets, including stocks, commodities, cryptocurrencies, and stock indexes.
The models have been benchmarked on a test set with monthly granularity from 2020 to 2024.
All models were evaluated in a zero-shot setting, meaning no fine-tuning was performed. This allows for a comparison of the models' generalization ability on unseen data.

## Assets Data

The evaluation was conducted using a total of 40 financial assets.
Corresponding data can be found in the directory `benchmark_eval_data`.
The download script is `download_yahoo_data.py`.

## Models Evaluated

The following pretrained models were benchmarked:
- **Moirai (Small, Base, Large)**: [link](https://github.com/SalesforceAIResearch/uni2ts)
- **MoiraiMoE (Small, Base)**: [link](https://github.com/SalesforceAIResearch/uni2ts)

## Evaluation Metrics

The following metrics were used to evaluate the performance of each model on the test set:
 - **Mean Absolute Error (MAE)**: Lower MAE indicates better model accuracy. It is less sensitive to outliers than MSE.
 - **Mean Squared Error (MSE)**: Lower MSE indicates better model accuracy. Unlike MAE, MSE penalizes larger errors more heavily, making it sensitive to outliers.
 - **Mean Absolute Percentage Error (MAPE)**: Indicates how far off the predictions are from the actual values on average. A lower MAPE indicates better prediction accuracy.
 - **Directional Accuracy (DA)**: Higher directional accuracy indicates that the model can correctly predict the trend or direction of change in the data, regardless of the magnitude of the error.

## Evaluation Results

The results of the evaluation, including performance for each metric, can be found in the [visualize_results.ipynb](visualize_results.ipynb) notebook.

## Support
If you found this project interesting please support me by giving it a ⭐, I would really appreciate it 😀
