# Global counters
naive_calls = 0
memo_calls = 0

# 1️⃣ Naive Fibonacci
def fib_naive(n):
    global naive_calls
    naive_calls += 1
    
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)


# 2️⃣ Memoized Fibonacci
def fib_memo(n, memo={}):
    global memo_calls
    memo_calls += 1
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    
    return memo[n]


# Test values
for n in [10, 20, 30]:
    naive_calls = 0
    memo_calls = 0
    
    naive_result = fib_naive(n)
    memo_result = fib_memo(n, {})
    
    print("\nFor n =", n)
    print("Fibonacci:", naive_result)
    print("Naive Calls:", naive_calls)
    print("Memo Calls:", memo_calls) 