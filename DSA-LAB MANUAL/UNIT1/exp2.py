n = int(input("Enter value of n: "))

# 1️⃣ Single Loop
count1 = 0
for i in range(n):
    count1 += 1

print("\nSingle Loop")
print("Estimated Operations:", count1)
print("Complexity: O(n)")
print("Justification: Loop runs n times.")
print("Operations grow linearly with n.\n")


# 2️⃣ Nested Loop
count2 = 0
for i in range(n):
    for j in range(n):
        count2 += 1

print("Nested Loop")
print("Estimated Operations:", count2)
print("Complexity: O(n^2)")
print("Justification: Inner loop runs n times for each outer loop.")
print("Total operations ≈ n × n.\n")


# 3️⃣ Triangular Loop
count3 = 0
for i in range(n):
    for j in range(i + 1):
        count3 += 1

print("Triangular Loop")
print("Estimated Operations:", count3)
print("Complexity: O(n^2)")
print("Justification: Total operations = 1+2+...+n = n(n+1)/2.")
print("Quadratic growth dominates.\n")


# 4️⃣ Halving Loop
count4 = 0
i = n
while i > 1:
    i = i // 2
    count4 += 1

print("Halving Loop")
print("Estimated Operations:", count4)
print("Complexity: O(log n)")
print("Justification: n reduces by half each step.")
print("Steps required ≈ log2(n).\n")