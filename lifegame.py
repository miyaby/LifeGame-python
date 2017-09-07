# import sys, time
# for num, i in enumerate(range(100)):
#     sys.stdout.write("\r%d" % num)
#     sys.stdout.flush()
#     time.sleep(0.01)

first_live = [11,36,66,93]
square = "";

for num in range(100):

    cell = "X"
    for live_num in first_live:
        if (num+1)==live_num:
            cell = "O"
            break

    square += cell
    if (num+1)%10==0:
        square += "\n"

print(square)