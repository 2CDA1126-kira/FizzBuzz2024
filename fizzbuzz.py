while True:
    try:
        x = int(input('いくつまで数えますか？: ')) + 1
        break
    except ValueError:
        print("無効な入力です。整数を入力してください。")
for i in range(1,x):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)