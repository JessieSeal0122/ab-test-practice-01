# A/B Test Practice 01 - Marketing Campaign Analysis

This repository is part of my A/B testing self-practice series.  
The goal of this project is to analyze and compare the conversion performance of two marketing campaigns (Control vs Test) using Python.

> 📌 This is a personal exercise project focused on A/B test logic, t-tests, and data visualization.

---

## 📊 Project Overview

This analysis examines whether the "Test Campaign" performs significantly better than the "Control Campaign" in terms of:

- Click-through rate (CTR)
- Add-to-cart rate
- Purchase conversion rate

A two-sample t-test is applied to evaluate whether the differences in conversion rates are statistically significant.

---

## 🗂️ Dataset

- **Source**: [Kaggle Open Dataset - A/B Testing Data](https://www.kaggle.com/datasets/amirmotefaker/ab-testing-dataset/data)
- The dataset contains daily metrics from two marketing campaigns.
- Columns include impressions, clicks, add to cart, purchases, and more.

> 📌 *Data files are not uploaded to this repository. Please download from Kaggle manually and place them in the `/data/` folder.*

---

## 🧰 Requirements

Install required packages with:

```bash
pip install -r requirements.txt
```
Required packages:  
pandas  
scipy  
matplotlib  
seaborn  

---

## ▶️ How to Run
Execute the script with:

```bash
python ab_test_analysis.py
```
It will:  
1.Load and clean the dataset  
2.Calculate conversion metrics  
3.Perform t-tests on CTR, cart rate, and purchase rate  
4.Generate a grouped bar chart  
5.Save a summary image and log file  

---

| File Name                            | Description                                    |
| ------------------------------------ | ---------------------------------------------- |
| `conversion_rate_comparison_all.png` | Grouped bar chart comparing conversion metrics |
| `ab_test_summary_table.png`          | Summary table of t-test results (as image)     |
| `ab_test_run_log.txt`                | Run log including timestamp and t-test output  |

## 📌 License
This is a practice project using open data and free libraries.  
No commercial use intended.  
