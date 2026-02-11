# Company Data Matching Project

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]([https://colab.research.google.com/github/ВАШ_ЮЗЕРНЕЙМ/НАЗВА_РЕПО/blob/main/ВАШ_ФАЙЛ.ipynb](https://colab.research.google.com/github/MartynovychSerhii/Employment-Test-Tasks/blob/main/Dataforest/DataForest_test_Martynovych.ipynb))

This project provides a robust solution for entity resolution and data matching between two disparate company datasets using fuzzy logic and address validation.

## 1. Matching Approach
A multi-staged approach was implemented to merge the datasets effectively:
* **Aggregation:** To handle clients with multiple locations, data was grouped by company name. All addresses were collected into Python lists to maintain a "one company — one row" structure and prevent row duplication.
* **Fuzzy Matching:** The `rapidfuzz` library, specifically the `token_sort_ratio` algorithm, was utilized. This method effectively identifies matches despite word reordering or spelling errors.
* **Similarity Threshold:** A threshold of **85%** was established. This provides an optimal balance, filtering out false positives while capturing companies with minor naming variations.
* **Address Validation:** Following the name-based match, the algorithm automatically compares address lists using **Set Intersection** to identify overlapping locations.

## 2. Normalization & Transformations
To enhance matching accuracy, the following transformations were applied to names and addresses:
* **Case Folding:** Converting all text to lowercase for uniformity.
* **Suffix Removal:** Stripping legal entity suffixes (e.g., Inc, Ltd, LLC, Corp), which do not contribute to brand identification.
* **Whitespace Trimming:** Eliminating leading/trailing spaces and excessive padding found within Dataset 2.
* **Standardization:** Explicitly converting all values to string types before comparison to prevent errors caused by missing values (NaN).

## 3. Data Quality Issues Found
Several data integrity issues were identified and addressed during analysis:
* **Trailing Spaces:** Numerous records in Dataset 2 contained significant trailing whitespace, which initially hindered direct string comparison.
* **Inconsistent Naming Conventions:** The same entity often appeared with inconsistent punctuation (e.g., a comma before "Inc." in one file but not the other).
* **Missing Values:** Null entries in address fields were successfully filtered using `.dropna()` to ensure clean list aggregation.
* **Duplicate Records:** Multiple location entries for single companies necessitated pre-matching aggregation to ensure a clean 1:1 company comparison.

## 4. Calculated Metrics

### Key Performance Indicators
| Metric | Value | Description |
| :--- | :--- | :--- |
| **Match Rate** | 49.33% | 518 out of 1050 unique entities matched |
| **Unmatched Records** | 50.67% | 532 entities with no confident match |
| **One-to-Many Ratio** | 6.38% | Companies with multiple locations in DS2 |

### Additional Insights
* **Location Overlap Rate:** **55.41%** *This metric represents high-confidence matches where both the company name and at least one physical address were identical in both datasets.*

---
