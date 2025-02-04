# 📌 Facebook Sentiment Analysis with Random Forest  

![Banner](images/banner.png)  

![GitHub repo size](https://img.shields.io/github/repo-size/yourusername/facebook-sentiment-analysis)  
![GitHub contributors](https://img.shields.io/github/contributors/yourusername/facebook-sentiment-analysis)  
![GitHub stars](https://img.shields.io/github/stars/yourusername/facebook-sentiment-analysis?style=social)  
![GitHub forks](https://img.shields.io/github/forks/yourusername/facebook-sentiment-analysis?style=social)  

## 🚀 Overview  

This project is a **Facebook Sentiment Analysis** tool built with **Streamlit** and **Random Forest**. It allows users to enter Facebook comments or posts and predicts their sentiment as **Positive 😊, Neutral 😐, or Negative 😡** using a trained **Random Forest model** 
---

## 🛠️ Features  

- ✅ **Pretrained Random Forest model** for sentiment classification  
- ✅ **Text preprocessing** (removal of URLs, special characters, and stopwords)  
- ✅ **TF-IDF vectorization** for text transformation  
- ✅ **Beautiful Streamlit UI** with emoji-based sentiment display  
- ✅ **Easy deployment** and lightweight execution  

---

## 📸 Screenshots  

### 🔹 **User Interface**  
![UI Screenshot](assets/naturak.png)  

### 🔹 **Sentiment Analysis in Action**  
![Sentiment Analysis](assets/positive.png)  

---

## 📦 Installation  

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/Bibekbb/Facebook-Sentiment-Analysis.git
cd facebook-sentiment-analysis
```  

2️⃣ **Create a virtual environment (optional but recommended)**  
```bash
python -m venv venv
source venv/bin/activate  
venv\Scripts\activate      
```  

3️⃣ **Install dependencies**  
```bash
pip install -r requirements.txt
```  

4️⃣ **Run the Streamlit app**  
```bash
streamlit run app.py
```  

---

## 📁 Project Structure  

```
facebook-sentiment-analysis/
│── assets/                    
│   ├── positive.png
│   ├── negative.png
│
│── model/                    
│   ├── sentiment_model.pkl 
│   ├── tfidf_vectorizer.pkl
│
│── data/                    
│   ├── Facebook Sentiment Analysis .ipynb
│   ├── fb_sentiment.csv
│
│── app.py                     
│── requirements.txt            
│── README.md            
```

---

## 🎯 Usage  

1️⃣ Open the **web interface**  
2️⃣ Enter a **Facebook comment/post**  
3️⃣ Click **Analyze Sentiment**  
4️⃣ View the **sentiment prediction**  

---

## ⚡ Example Inputs & Predictions  

| Input Text | Prediction |
|------------|------------|
| `"I love this product! It's amazing!"` | 😊 Positive |
| `"This is okay, nothing special."` | 😐 Neutral |
| `"Worst experience ever! Never buying again."` | 😡 Negative |

---

## 🌍 Deployment  

To deploy this project online, you can use **Streamlit Cloud, Heroku, or AWS**.  

Example for **Streamlit Cloud**:  
1️⃣ Push the repository to GitHub  
2️⃣ Go to [Streamlit Cloud](https://share.streamlit.io/)  
3️⃣ Connect your repository and deploy  

---

## 💡 Future Enhancements  

- 🔹 Improve model performance with **deep learning**  
- 🔹 Add **BERT-based sentiment analysis**  
- 🔹 Enable **real-time Facebook comment scraping**  

---

## 🤝 Contributing  

Contributions are **welcome**! Please follow these steps:  
1️⃣ Fork the repository  
2️⃣ Create a new branch: `git checkout -b feature-branch`  
3️⃣ Commit changes: `git commit -m "Add new feature"`  
4️⃣ Push the branch: `git push origin feature-branch`  
5️⃣ Open a **Pull Request**  

---

## 📜 License  

This project is **MIT licensed**. See the [LICENSE](LICENSE) file for details.  

---

## 📩 Contact  

📧 **Your Name** – [your.email@example.com](mailto:your.email@example.com)  
🔗 **GitHub** – [github.com/yourusername](https://github.com/yourusername)  
🚀 **Portfolio** – [yourwebsite.com](https://yourwebsite.com)  

Give a ⭐ if you found this useful! 😊  

---

### 🔹 **Note:**  
Make sure to upload `banner.png`, `ui_screenshot.png`, and `sentiment_example.png` inside an `images/` folder in your repository for proper display.  

Let me know if you need more modifications! 🚀🔥