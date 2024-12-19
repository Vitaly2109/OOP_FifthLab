def main():
    n = int(input("кол-во элем массива: "))
    list = []
    print("элементы: ")
    for i in range(n):
        list.append(int(input()))
    print("массив:")
    for i in range(n):
        print(f"list[{i}] = {list[i]}")

    print(f"адрес начала: {id(list)}")

    print("расстояние каждого элемента от начала:")
    for i in range(n):
        print(f"{list[(i)]} находится на расстоянии {i}")

if __name__ == "__main__":
    main()