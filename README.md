📊 **Data Cleaning & Preprocessing Overview**

📌 **Project Goal**
The purpose of this task is to transform a raw, messy dataset into a structured, analysis-ready format by resolving missing entries, eliminating duplicate records, and standardizing data fields.

📂 **Dataset Details**

* **Source File:** Netflix Sample Dataset (`.csv`)
* **Overview:** Comprises metadata on various movies and television series, including attributes like title, director, country of origin, release year, and platform addition date.

🛠️ **Technologies & Libraries**

* **Programming Language:** Python
* **Data Manipulation:** Pandas

🔍 **Key Preprocessing Steps**

1. **Imputing Missing Values**
* Replaced null entries in the `director` field with `"Unknown"`.
* Replaced missing timestamps in the `date_added` field with `"Not Available"`.


2. **Eliminating Duplicate Entries**
* Detected and dropped repeated rows across the dataset using `df.drop_duplicates()` to ensure record uniqueness.
