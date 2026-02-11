# Project Objective
Match companies between two datasets based on company names and locations, and produce a merged output.

## Datasets: DATAFOREST - DE TEST TASK
You are provided with two datasets, both containing company information including:
* Company name 
* Location (street, city, province / state, country, postal code)

## Requirements
Match companies between Dataset 1 and Dataset 2 based on 
*company name*
*location information*

### The merged dataset must:
* Contain all unique companies from Dataset 1.
* Include corresponding company matches from Dataset 2 where they exist.
* Contain a column with a list of locations for companies from Dataset 1.
* Contain a column with a list of locations for companies from Dataset 2.
* Contain a column with overlapping locations between two companies.
* If no locations overlap, keep the company name match and leave the overlapping locations column empty.*

### Calculated Metrics:
1. **Match rate:** % of Dataset 1 companies that have a match in Dataset 2.
2. **Unmatched records:** % of companies with no match in either dataset.
3. **One-to-many matches:** % of companies with multiple matched entries.
4. **Additional metrics:** other metrics you consider useful.

## Constraints
* **Time limit:** 3 hours.
* **Tools:** Python, Pandas.

## Deliverables
1. **Merged dataset:** (CSV)
2. **Code scripts:** 
3. **Documentation:**
4.  * Matching approach.
    * Data quality issues found.
    * Normalization / transformations applied.
    * Calculated metrics.
