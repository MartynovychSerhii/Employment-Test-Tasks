# Project Objective
Match companies between two datasets based on company names and locations, and produce a merged output.

## Datasets: DATAFOREST - DE TEST TASK
You are provided with two datasets, both containing company information including:
* Company name 
* Location (street, city, province / state, country, postal code)

## Requirements
Match companies between Dataset 1 and Dataset 2 based on **company name** and **location information**.

### The merged dataset must:
* Contain all unique companies from **Dataset 1**.
* Include corresponding company matches from **Dataset 2** where they exist.
* Contain a column with a **list of locations** for companies from Dataset 1.
* Contain a column with a **list of locations** for companies from Dataset 2.
* Contain a column with **overlapping locations** between two companies.
* *Note: If no locations overlap, keep the company name match and leave the overlapping locations column empty.*

### Calculated Metrics:
1. **Match rate:** % of Dataset 1 companies that have a match in Dataset 2.
2. **Unmatched records:** % of companies with no match in either dataset.
3. **One-to-many matches:** % of companies with multiple matched entries.
4. **Additional metrics:** Any other useful insights (e.g., Location Overlap Rate).

## Constraints
* **Time limit:** 3 hours.
* **Tools:** Python, Pandas.

## Deliverables
1. **Merged dataset:** Final output in CSV format.
2. **Code scripts:** Python/Jupyter Notebook.
3. **Documentation:** * Matching approach.
    * Data quality issues found.
    * Normalization / transformations applied.
    * Calculated metrics.
