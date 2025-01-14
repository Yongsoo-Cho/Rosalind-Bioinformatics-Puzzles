k,m,n = map(int, input().split())

total = k+m+n
total_pairs = total * (total-1)

prob_dom = (
    k*(k-1) +
    2*k*m +
    2*k*n +
    m*(m-1)*0.75 +
    2*m*n*0.5
)

print(prob_dom/total_pairs)