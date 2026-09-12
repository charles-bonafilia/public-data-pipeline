import csv

print("Exoplanet summary report")

with open("data/raw/exoplanets.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    count = 0
    counts = {}
    for row in reader:
        count = count + 1
        method = row[2]
        counts[method] = counts.get(method, 0) + 1

print(f"Columns: {header}")
print(f"Planets: {count}")

print("Discovery methods:")
sorted_methods = sorted(counts.items(), key=lambda x: x[1], reverse=True)
for method, number in sorted_methods:
    print(f"  {method}: {number}")
    

