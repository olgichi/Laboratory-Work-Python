"""Поиск суммы произведений из списка словарей"""
import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)
    score_list= [item["score"] for item in json_data]
    weight_list = [item["weight"] for item in json_data]
    summa = sum(score_list[i]*weight_list[i] for i in range(len(score_list)))
    return (summa)



if __name__ == '__main__':
    res = task()
    print(f"{res:.3f}")
