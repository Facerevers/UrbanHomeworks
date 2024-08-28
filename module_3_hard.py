def calculate_structure_sum(data):
    sum = 0
    if isinstance(data, (list, tuple)):
        for i in data:
            sum += calculate_structure_sum(i)
    elif isinstance(data, dict):
        for key, value in data.items():
            sum += len(key)
            sum += calculate_structure_sum(value)
    elif isinstance(data, set):
        for i in data:
            sum += calculate_structure_sum(i)
    elif isinstance(data, str):
        sum += len(data)
    elif isinstance(data, (int, float)):
        sum += data
    return sum
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)