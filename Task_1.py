import heapq

def min_cost_to_connect_cables(cables):
    # Створюємо мін-купу з довжин кабелів
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки в купі більше одного кабелю
    while len(cables) > 1:
        # Вибираємо два найменших кабелі
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)
        
        # З'єднуємо їх, додаємо вартість з'єднання
        cost = cable1 + cable2
        total_cost += cost
        
        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад
cables = [4, 3, 2, 6]
result = min_cost_to_connect_cables(cables)
print(f"Мінімальні витрати на з'єднання: {result}")
