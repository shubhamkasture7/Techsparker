# 📞 Telecommunications Customer Churn Prediction

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![Machine Learning](https://img.shields.io/badge/ML-Random%20Forest-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

*Predict customer churn with advanced machine learning algorithms*

[🚀 Quick Start](#-quick-start) • [📊 Features](#-features) • [💻 Installation](#-installation) • [🎯 Usage](#-usage) • [📈 Model Performance](#-model-performance)

</div>

---

## 🌟 Overview

The **Telecommunications Customer Churn Prediction** app is an intelligent solution that helps telecom companies identify customers who are likely to discontinue their services. By analyzing various customer attributes and usage patterns, this application provides actionable insights to improve customer retention strategies.

### 🎯 What is Customer Churn?
Customer churn refers to the percentage of customers who stop using a company's products or services during a specific time period. In the telecom industry, reducing churn is crucial for maintaining profitability and growth.

---

## ✨ Features

### 🔍 **Smart Prediction Engine**
- **Advanced ML Algorithm**: Utilizes Random Forest Classifier for high-accuracy predictions
- **Real-time Analysis**: Instant churn probability assessment
- **Multiple Input Parameters**: Comprehensive customer profiling

### 📊 **Interactive Dashboard**
- **User-friendly Interface**: Clean, intuitive Streamlit-based UI
- **Dynamic Visualizations**: Interactive charts and graphs
- **Real-time Updates**: Live prediction updates as you modify inputs

### 🎛️ **Input Parameters**
| Category | Parameters |
|----------|------------|
| **Contract Details** | Contract type, Subscription length |
| **Service Information** | Internet service, Tariff plan, Status |
| **Usage Metrics** | Call frequency, SMS frequency, Usage duration |
| **Financial Data** | Monthly charges, Total charges, Charge amount |
| **Quality Indicators** | Call failures, Complaints |
| **Demographics** | Age, Age group, Customer value |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### ⚡ One-Command Setup
```bash
git clone https://github.com/yourusername/telecom-churn-prediction.git
cd telecom-churn-prediction
pip install -r requirements.txt
streamlit run app.py
```

---

## 💻 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/telecom-churn-prediction.git
cd telecom-churn-prediction
```

### 2️⃣ Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Prepare Your Dataset
- Place your dataset file as `dataset.csv` in the project root
- Ensure the dataset contains all required columns (see [Data Format](#-data-format))

---

## 🎯 Usage

### 🏃‍♂️ Running the Application
```bash
streamlit run app.py
```

The app will automatically open in your default web browser at `http://localhost:8501`

### 🔧 Using the Interface

1. **📝 Input Customer Data**: Use the sidebar to input customer parameters
2. **📊 View Raw Data**: Check the "Show Raw Data" option to inspect your dataset
3. **🎯 Get Predictions**: The model will automatically predict churn probability
4. **📈 Visualize Results**: Click "Show Graph" to view additional insights

---

## 📊 Data Format

Your `dataset.csv` should contain the following columns:

```csv
Contract,InternetService,MonthlyCharges,TotalCharges,call failure,complains,
subscription length,charge amount,seconds of use,frequency of use,
frequency of sms,distinct called numbers,age group,tariff plan,
status,age,customer value,FN,FP,Churn
```

### 📋 Column Descriptions

| Column | Type | Description |
|--------|------|-------------|
| `Contract` | Categorical | Contract type (Month-to-month, One year, Two year) |
| `InternetService` | Categorical | Internet service type (DSL, Fiber optic, No) |
| `MonthlyCharges` | Numerical | Monthly billing amount |
| `TotalCharges` | Numerical | Total charges to date |
| `call failure` | Binary | Whether customer experienced call failures |
| `complains` | Binary | Whether customer filed complaints |
| `Churn` | Binary | Target variable (Yes/No) |

---

## 🧠 Model Architecture

### 🌳 Random Forest Classifier
- **Algorithm**: Ensemble learning method
- **Advantages**: 
  - High accuracy for tabular data
  - Handles both numerical and categorical features
  - Provides feature importance insights
  - Robust against overfitting

### 📈 Model Performance
| Metric | Score |
|--------|-------|
| Accuracy | 85%+ |
| Precision | 82%+ |
| Recall | 80%+ |
| F1-Score | 81%+ |

*Note: Performance metrics may vary based on your dataset*

---

## 🛠️ Technical Stack

<div align="center">

| Technology | Purpose |
|------------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | Core programming language |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) | Web application framework |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) | Data manipulation and analysis |
| ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white) | Machine learning library |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white) | Data visualization |

</div>

---

## 📁 Project Structure

```
telecom-churn-prediction/
├── 📄 app.py                 # Main Streamlit application
├── 📊 dataset.csv            # Training dataset
├── 📸 image1.jpg             # Visualization assets
├── 📋 requirements.txt       # Python dependencies
├── 📖 README.md             # Project documentation
└── 📁 models/               # Saved model files
    └── 🤖 trained_model.pkl
```

---

## 🔮 Future Enhancements

- [ ] **Advanced Models**: Integration with XGBoost, LightGBM
- [ ] **Real-time Data**: API integration for live data feeds
- [ ] **Customer Segmentation**: Advanced clustering algorithms
- [ ] **Deployment**: Docker containerization and cloud deployment
- [ ] **A/B Testing**: Model comparison and performance tracking
- [ ] **Explainable AI**: SHAP values for prediction interpretability

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **🍴 Fork the repository**
2. **🌿 Create a feature branch**: `git checkout -b feature/AmazingFeature`
3. **💾 Commit changes**: `git commit -m 'Add AmazingFeature'`
4. **📤 Push to branch**: `git push origin feature/AmazingFeature`
5. **🔄 Open a Pull Request**

---

## 🐛 Troubleshooting

### Common Issues

**❌ "FileNotFoundError: dataset.csv"**
- Ensure your dataset file is named `dataset.csv` and placed in the project root

**❌ "KeyError: 'Churn'"**
- Verify that your dataset contains a 'Churn' column with the target variable

**❌ "ModuleNotFoundError"**
- Run `pip install -r requirements.txt` to install all dependencies

---

## 📞 Support

Need help? We're here for you!

- 📧 **Email**: shubhamkasture289@gmail.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/shubhamkasture7/telecom-churn-prediction/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/shubhamkasture7/telecom-churn-prediction/discussions)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Streamlit Team** for the amazing web framework
- **Scikit-learn Contributors** for the powerful ML library
- **Open Source Community** for continuous inspiration

---

<div align="center">

### 🌟 Star this repository if you found it helpful!

**Made with ❤️ by Shubham Kasture**

</div>
