# 🔥 PySpark Learning Journey – Data Engineering Track

This repository documents my hands-on journey to learn **Apache Spark** and its Python API **PySpark**, as part of my path to mastering **Data Engineering**.

---

## 🚀 Project: Job Listings Analyzer

A mini-project designed to explore and implement the **core concepts of Spark**, including:
- RDDs
- DataFrame API
- Spark SQL
- Structured Streaming (simulated)
- MLlib (Spark's machine learning library)

---

## 📁 Directory Structure
  ```plaintext
.
├── jobs.txt                 
├── notebooks/               
│   ├── 1_rdd_basics.ipynb
│   ├── 2_dataframe_api.ipynb
│   ├── 3_spark_sql.ipynb
│   ├── 4_structured_streaming.ipynb
│   └── 5_mllib_model.ipynb
├── stream_data/             
├── output/                  
└── README.md

```
---

## 📚 Concepts Covered

### 1. 🔧 Spark Core + RDD
- Loading data using `textFile()`
- Basic `map()` and `filter()` transformations
- Actions like `collect()` and `count()`

### 2. 📊 DataFrame API
- Creating and querying DataFrames
- Using `groupBy`, `agg`, and `select`
- Catalyst optimizer and lazy evaluation

### 3. 🧠 Spark SQL
- Creating temporary views
- Running SQL queries over Spark tables

### 4. ⚡ Structured Streaming (Simulated)
- Setting up `readStream` on CSV files
- Writing real-time output to console

### 5. 🤖 MLlib (Machine Learning)
- Using `StringIndexer`, `VectorAssembler`
- Training a logistic regression model
- Predicting high-salary jobs

---

## ⚙️ Requirements

- Python 3.8+
- PySpark (`pip install pyspark`)
- Jupyter Notebook (recommended)
- Optional: VS Code or Google Colab

---

## 📈 How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/pyspark-data-engineering](https://github.com/MutharasuArchunan13/Data-Engineering).git
   cd pyspark-data-engineering

