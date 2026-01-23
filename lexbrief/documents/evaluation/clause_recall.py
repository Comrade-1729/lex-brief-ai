import json

def evaluate_clause_recall(predicted_clauses, gold_path):
    try:
        with open(gold_path, "r") as f:
            gold = json.load(f)
    except FileNotFoundError:
        return {
            "recall": None,
            "error": "Gold evaluation file not found"
        }

    gold_clauses = set(gold["clauses"])
    predicted = set(predicted_clauses)

    true_positives = gold_clauses & predicted
    recall = len(true_positives) / len(gold_clauses)

    return {
        "recall": round(recall, 3),
        "found": list(true_positives),
        "missing": list(gold_clauses - predicted),
    }
