import heapq

def merge_k_lists(lists):
    # Мінімальна купа
    min_heap = []
    
    # Додаємо перші елементи кожного списку до мін-купи
    for i in range(len(lists)):
        if lists[i]:  # перевіряємо, чи список не порожній
            heapq.heappush(min_heap, (lists[i][0], i, 0))
    
    merged_list = []
    
    # Поки мін-купа не порожня
    while min_heap:
        # Вибираємо мінімальний елемент з купи
        val, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(val)
        
        # Якщо в цьому списку є ще елементи, додаємо наступний до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))
    
    return merged_list

# Приклад
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
