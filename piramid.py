blocks = int(input("Enter the number of blocks: "))
blocks_used = 1
height = 1

while blocks >= blocks_used :
    blocks = blocks - blocks_used
    height += 1
    blocks_used = blocks_used + height

print("The height of the pyramid:", height)
