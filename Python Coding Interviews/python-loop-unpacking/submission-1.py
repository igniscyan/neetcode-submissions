from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    highest_score, leader_name = 0, ''
    for name, score in scores:
        if score > highest_score:
            highest_score = score
            leader_name = name
    return leader_name



# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
