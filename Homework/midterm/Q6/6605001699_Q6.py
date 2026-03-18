# Get filename 
filename = input("Enter filename: ").strip()

total = 0.0
count = 0

with open(filename, "r", encoding="utf-8") as file:
	for line in file:
		line = line.strip().split(",")	
    
	high = int(line[0])
	low = int(line[1])
	total += abs(high - low)
	count += 1

average = total / count
print(f"Average temparature difference: {average}")