# open() w, r, a, wb, rb
# w = write
# r = read
# a = append
# wb = write binarry fayl

# rb = read binarry fayl

# file = open("text.txt", "w")
# file.write("Asslomu alaykum!!!")
# file = open("text.txt", "w", encoding = "utf-8")
# file.write("уаывкмпуккрваи!!!")
# file.close()



old = open("text.txt", "r", encoding="utf-8")
print(old.read())
old.close()