from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    highest_score, leader_name = 0, ''
    for name, score in scores:
        if score > highest_score:
            highest_score = score
            leader_name = name
    return leader_name

def best_student_sort(scores: List[Tuple[str, int]]) -> str:
    scores.sort(key = lambda tup: tup[1], reverse = True)
    return scores[0][0]

def best_student_max(scores: List[Tuple[str, int]]) -> str:
    return max(scores, key = lambda tup: tup[1])[0]



# do not modify below this line
print(best_student_max([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student_max([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student_max([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student_max([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
