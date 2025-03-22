# Stock Market Forecasting with LSTM Networks

![Stock Market Forecast](https://raw.githubusercontent.com/arjunthilak05/Project-1-Stock-Market-Prediction/9397c938d57ad146fcd6fbfdefce82936398adeb/output.png)

## Overview

This project implements a Long Short-Term Memory (LSTM) neural network model to forecast stock market movements. It analyzes historical stock data using technical indicators to predict future price movements, with customizable features for different tickers.

## Features

- **Multi-ticker Analysis**: Support for analyzing multiple stock tickers simultaneously
- **Technical Indicators**: Automatic calculation of RSI, EMAs (20, 100, 150) for each stock
- **Custom LSTM Architecture**: Configurable neural network with dropout layers and hyperparameter tuning
- **Visualization Suite**: Comprehensive set of evaluation plots (prediction vs. actual, residuals, error distribution)
- **Interactive Ticker Selection**: Ability to select specific stocks for analysis

## Requirements

- Python 3.7+
- TensorFlow 2.x
- Keras
- pandas
- pandas_ta
- numpy
- scikit-learn
- matplotlib
- seaborn

## Installation

```bash
# Clone the repository
git clone https://github.com/arjunthilak05/Project-1-Stock-Market-Prediction.git 
cd stock-market-lstm

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

1. Prepare your stock data CSV file with required columns
2. Update the file path in the script:
   ```python
   df = pd.read_csv("path/to/your/stock_data.csv")
   ```
3. Run the main script:
   ```python
   python stock_lstm.py
   ```
4. When prompted, enter the ticker symbol you want to analyze

## Model Architecture

The project implements two LSTM model variants:

### Basic LSTM Model
- Single LSTM layer (150 units)
- Dense output layer
- Adam optimizer
- Mean Squared Error loss function

### Enhanced LSTM Model
- Configurable LSTM units (default: 150)
- Dropout regularization
- Customizable optimizer
- Linear activation output

## Model Evaluation

The models are evaluated using multiple visualization techniques:

- Line plots comparing predicted vs actual values
- Scatter plots showing prediction accuracy
- Residual analysis plots
- Error distribution histograms
- Density plots of prediction errors

## Sample Results

![Prediction Comparison](https://raw.githubusercontent.com/username/stock-market-lstm/main/images/pred_vs_actual.png)

![Error Analysis](https://raw.githubusercontent.com/username/stock-market-lstm/main/images/error_distribution.png)

## Customization

The project allows for easy customization:
- Modify `backcandles` to adjust the sequence length (currently 30 days)
- Change LSTM units (150, 200, 250, 300) to capture more complex patterns
- Adjust batch size and epochs for different training characteristics
- Add additional technical indicators in the indicators DataFrame

## Future Improvements

- [ ] Implement feature importance analysis
- [ ] Add sentiment analysis from news and social media
- [ ] Create ensemble models combining multiple prediction approaches
- [ ] Develop backtesting framework for trading strategies
- [ ] Add support for cryptocurrency data

## License

MIT License - see [LICENSE](LICENSE) file for details

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgments

- Technical indicators provided by [pandas_ta](https://github.com/twopirllc/pandas-ta)
- Inspired by research in deep learning approaches for financial time series forecasting
