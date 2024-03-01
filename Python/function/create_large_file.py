with open('large_file.log', 'w') as f:
    for i in range(10000000): # 写入一千万行
        f.write(f"This is line {i}, used for testing.\n")