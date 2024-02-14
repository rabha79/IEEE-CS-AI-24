n = int(input())
scores = list(map(int, input().split()))
unique_scores = sorted(set(scores), reverse=True)
if len(unique_scores) > 1:
    runner_up_score = unique_scores[1]
    print(runner_up_score)
else:
    print()





