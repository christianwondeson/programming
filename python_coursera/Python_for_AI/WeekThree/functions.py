if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)
    runner_up_score = next((score for score in scores if score < max(scores)), None)
    print(runner_up_score)
