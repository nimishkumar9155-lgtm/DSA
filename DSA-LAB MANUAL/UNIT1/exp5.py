move_count = 0

def hanoi(n, src, aux, dst):
    global move_count
    
    if n == 1:
        print(f"Move disk 1 from {src} to {dst}")
        move_count += 1
        return
    
    # Step 1: Move n-1 disks to auxiliary
    hanoi(n-1, src, dst, aux)
    
    # Step 2: Move nth disk to destination
    print(f"Move disk {n} from {src} to {dst}")
    move_count += 1
    
    # Step 3: Move n-1 disks from auxiliary to destination
    hanoi(n-1, aux, src, dst)


# 🔹 Move sequence for n = 3
print("Move sequence for n = 3:")
move_count = 0
hanoi(3, "A", "B", "C")
print("Total moves for n=3:", move_count)


# 🔹 Move count for n = 4
move_count = 0
hanoi(4, "A", "B", "C")
print("\nTotal moves for n=4:", move_count) 