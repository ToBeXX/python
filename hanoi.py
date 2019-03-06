def hanoi(n, a, buffer, c):
    if n == 1:
        print(a, '--->', c) # 定义从a柱移动到c柱的操作
    else:
        hanoi(n-1, a, c, buffer) # 把(n-1)个a柱上的圆块移动到缓冲区buffer柱
        hanoi(1, a, buffer, c) # 把最底部的最大的圆块移动到c柱
        hanoi(n-1, buffer, a, c) # 把(n-1)个缓冲区buffer柱上的圆块移动到c柱

hanoi(3, 'A', 'B', 'C')
