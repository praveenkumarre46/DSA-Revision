def carPooling(trips, capacity):
    timeline = [0] * 1001
    
    for num, start, end in trips:
        timeline[start] += num
        timeline[end] -= num
        
    current_passengers = 0
    for change in timeline:
        current_passengers += change
        if current_passengers > capacity:
            return False
            
    return True