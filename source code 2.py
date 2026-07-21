def image_processing(n):
    if n <= 1:
        return

    print("Processing Image Size:", n)

    for i in range(4):
        image_processing(n // 2)

    print("Linear Processing Work =", n)


n = int(input("Enter image size: "))
image_processing(n)
