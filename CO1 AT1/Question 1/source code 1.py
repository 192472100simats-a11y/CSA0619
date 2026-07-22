def image_merge(size, level=0):
    if size <= 1:
        return

    print("Level", level, ": Processing", size, "images")

    image_merge(size // 2, level + 1)

    work = size

    print("Level", level, ": Merge Cost =", work)


n = int(input("Enter number of images: "))
image_merge(n)
