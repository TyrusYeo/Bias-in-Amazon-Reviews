# Amazon Review Analysis README

## Overview

This Python script analyzes Amazon review data from different categories such as "Movies and TV". We got our data from https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/. It performs various analyses to understand how review ratings, sentiment, and word usage differ between male and female reviewers.

## Code Explanation

### Imports

- The script starts by importing necessary libraries:
  - `json`: For handling JSON data
  - `string`: For string manipulation
  - `statistics`, `math`: For statistical calculations
  - `gender_guesser.detector`: For gender detection based on names
  - `matplotlib.pyplot`: For data visualization
  - `collections.Counter`: For counting occurrences of items
  - `scipy.stats`: For statistical tests
  - `stop_words.get_stop_words`: For obtaining stop words
  - `nltk`: For natural language processing tasks
  - `nltk.sentiment.SentimentIntensityAnalyzer`: For sentiment analysis
  - `pandas`, `seaborn`: For data manipulation and visualization

## Usage

To use the script, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the script with `python final_project.py`.

### Data Loading and Preprocessing

- The script loads review data from a JSON file, one example is (`Movies_and_TV_5.json`).
- It preprocesses reviewer names to extract first names and detects gender using the `gender_guesser.detector` library.
- Review data is stored in the `data` list, containing tuples of (rating, gender, reviewText).
- Additional data is stored in the `alt_data` dictionary, mapping ASINs to lists of (rating, gender) tuples.

### Data Analysis

#### Rating Analysis

- Ratings and genders are extracted from the data.
- Average ratings for males, females, and androgynous individuals are calculated.
- The distribution of review ratings by gender is visualized using bar plots.

#### T-test

- A two-sample independent t-test is performed to quantify the significance of gender differences in review ratings.
- T-statistic and p-value are calculated.
- The results are visualized using histograms and vertical lines representing mean ratings for males and females.

#### Difference in Ratings per Product

- The script calculates the difference between male and female ratings per product.
- The average difference between male and female ratings per product is computed.

#### Word Frequency Analysis

- Word frequency analysis is performed separately for male and female reviewers.
- Stop words are removed, and words are counted using the `Counter` class.
- The top 25 most frequent words for males and females are printed.

#### Sentiment Analysis

- Sentiment analysis is performed using the VADER sentiment analyzer.
- Positive and negative reviews are categorized based on sentiment scores and gender.
- The number of positive and negative reviews for males and females is printed.

#### Review Word Length Analysis

- The average word length of reviews is calculated for males and females.
- The distribution of average review word length by gender is visualized using boxplots.
- The correlation between review star rating and average review word length by gender is visualized using scatter plots.

### Utility Functions

- Several utility functions are defined to perform specific tasks like calculating average review length and visualizing data.

### Main Function

- The `__main__` block executes the data analysis pipeline by calling various functions defined above.

## Conclusion

This script provides insights into how review ratings, sentiment, and word usage vary between male and female reviewers on Amazon. 
