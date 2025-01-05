def counting_sort(arr, max_val):
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output

tasks_priority = [3, 1, 4, 1, 2, 4, 3]
sorted_tasks = counting_sort(tasks_priority, max(tasks_priority))
print(sorted_tasks)
