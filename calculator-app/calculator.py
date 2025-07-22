def add (a,b):
    return a+b
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        a = int(sys.argv[2])
        b = int(sys.argv[3])
        result = add(a,b)
        print(f'test result: {result}')