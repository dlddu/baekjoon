current_temperature = int(input())
target_temperature = int(input())
melting_time = int(input())
defrost_time = int(input())

total_time = 0

if current_temperature < 0:
    total_time = abs(current_temperature) * melting_time + defrost_time
current_temperature = max(current_temperature, 0)
heating_time = int(input())

print(total_time + (target_temperature - current_temperature) * heating_time)
