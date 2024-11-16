import json



# TODO решите задачу
def task() -> float:
    path_f = 'input.json'
    with open(path_f) as f:
        data = json.load(f)

    s = 0
    for q in data:
        s += q['score'] * q['weight']
    return s

print(f'{task():.3f}')
