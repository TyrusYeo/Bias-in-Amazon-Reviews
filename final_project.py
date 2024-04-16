import json
import string
import statistics
import math
import gender_guesser.detector as gender
d = gender.Detector(case_sensitive=False)
translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))

# print(d.get_gender("None"))
# print(d.get_gender(u"William"))
# file = 'AMAZON_FASHION_5.json'
file = 'Movies_and_TV_5.json'

# data format: (rating, gender)
data = []

# alt_data formate: asin : [(rating, gender), ...]
alt_data = {}

with open(file, 'r') as fp:
    for line in fp:
        # Pre process names, remove punc and get first name
        review_dict = json.loads(line.strip())
        name = review_dict.get('reviewerName', "None")
        first_name = name.translate(translator).partition(" ")[0]
        # Remove all data with unknown gender
        reveiwer_gender = d.get_gender(first_name)
        if reveiwer_gender == 'mostly_male' or reveiwer_gender == 'male':
            reveiwer_gender = 'M'
        elif reveiwer_gender == 'mostly_female' or reveiwer_gender == 'female':
            reveiwer_gender = 'F'
        elif reveiwer_gender == 'andy':
            reveiwer_gender = 'A'
        if reveiwer_gender != 'unknown':
            data.append([float(review_dict['overall']), reveiwer_gender])
            if review_dict['asin'] not in alt_data:
                alt_data[review_dict['asin']] = []
            alt_data[review_dict['asin']].append([float(review_dict['overall']), reveiwer_gender])

print(f"Size of data collected: {len(data)}")
print(f"Number of males: {sum(1 for row in data if row[1] == 'M')}")
print(f"Number of females: {sum(1 for row in data if row[1] == 'F')}")
print(f"Number of androgynous: {sum(1 for row in data if row[1] == 'A')}")

print(f"Average rating of males: {statistics.fmean(row[0] for row in data if row[1] == 'M')}")
print(f"Average rating of females: {statistics.fmean(row[0] for row in data if row[1] == 'F')}")
print(f"Average rating of androgynous: {statistics.fmean(row[0] for row in data if row[1] == 'A')}")

# Diff between male and female ratings per product
alt_data_diff = []

for key in alt_data:
    total_male_rating = sum(pair[0] for pair in alt_data[key] if pair[1] == 'M')
    total_male_count = sum(1 for pair in alt_data[key] if pair[1] == 'M')
    total_female_rating = sum(pair[0] for pair in alt_data[key] if pair[1] == 'F')
    total_female_count = sum(1 for pair in alt_data[key] if pair[1] == 'F')
    avg_male_rating = total_male_rating / (total_male_count or 1)
    avg_female_rating = total_female_rating / (total_female_count or 1)

    if total_male_count == 0 or total_female_count == 0:
        # alt_data_diff.append(0.0)
        pass
    else:
        alt_data_diff.append(abs(avg_female_rating - avg_male_rating))

print(f"Average diff between M and F ratings per product is: {statistics.fmean(alt_data_diff)}")
# print(alt_data_diff)