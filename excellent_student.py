def get_excellent_scores(scores):
    excellent_scores = []

    for score in scores:
        if score >= 80:
            excellent_scores.append(score)

    return excellent_scores


scores = [65, 85, 72, 95, 40, 88]
result = get_excellent_scores(scores)

print(result)
