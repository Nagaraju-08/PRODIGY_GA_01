# PRODIGY_GA_01

Fine-Tuned GPT-2 Text Generator | Prodigy InfoTech Generative AI Internship Task-01

# 🤖 GPT-2 Text Generator

A Streamlit web application that generates coherent text using a fine-tuned GPT-2 language model. The model was fine-tuned on a movie dialogues dataset to produce contextually relevant text based on user prompts.

---

## 📌 Project Overview

This project was developed as part of the **Prodigy InfoTech Generative AI Internship – Task 01**.

The objective is to fine-tune OpenAI's GPT-2 model on a custom dataset and build an interactive web application for generating human-like text.

---

## ✨ Features

- Fine-tuned GPT-2 model
- Interactive Streamlit web interface
- Custom text prompt input
- Adjustable Temperature parameter
- Adjustable Maximum Length parameter
- Context-aware text generation
- Fast model loading with caching

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- Datasets Library

---

## 📂 Dataset

The GPT-2 model was fine-tuned using a **Movie Dialogues Dataset** containing conversational text.

---

## 📁 Project Structure

```
PRODIGY_GA_01/
│
├── app.py
├── train.py
├── test.py
├── create_dataset.py
├── requirements.txt
├── README.md
│
├── data/
│   └── movie_dialogues.txt
│
├── models/
│   └── final_model/
│
└── screenshots/
    ├── home.png
    └── output.png
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/PRODIGY_GA_01.git
```

### 2. Navigate to the project

```bash
cd PRODIGY_GA_01
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 🚀 Usage

1. Enter a text prompt.
2. Adjust the Temperature.
3. Select the Maximum Length.
4. Click **Generate Text**.
5. View the generated output.

---

## 📸 Screenshots

### Home Page

> Add `screenshots/home.png`

### Generated Output

> Add `screenshots/output.png`

---

## 📚 Learning Outcomes

- Fine-tuned GPT-2 on a custom dataset
- Worked with Hugging Face Transformers
- Built an interactive Streamlit application
- Implemented text generation using sampling techniques
- Learned model loading and inference

---

## 👨‍💻 Author

**Kartheek Lagisetti**

---

## 🏢 Internship

**Prodigy InfoTech**

**Generative AI Internship**

**Task-01: Fine-Tune GPT-2 for Text Generation**

---

## 📄 License

This project is developed for educational and internship purposes.
