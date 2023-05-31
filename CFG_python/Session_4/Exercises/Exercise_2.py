### EXERCISE 2 ###
"""
Make a list of game scores. Using list functions write code to output information of the scores in the following format:

    Number of scores: 10
    Highest score: 200
    Lowest score: 3

Extension: Output all of the scores in descending order
"""

scores = [45, 120, 80, 3, 200, 75, 90, 60, 150, 30]

num_scores = len(scores)
highest_score = max(scores)
lowest_score = min(scores)
descending_scores = sorted(scores, reverse=True)

print("Number of scores:", num_scores)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)
print("Scores in descending order:", descending_scores)
