# coding:utf-8

import sys
args = sys.argv

# import sys, time
# for num, i in enumerate(range(100)):
#     sys.stdout.write("\r%d" % num)
#     sys.stdout.flush()
#     time.sleep(0.01)

# 初回に生存しているセル
first_live = [11,36,66,93]
square = ""
print_square = ""

# 1辺の長さ
edge = 10
# 全てのセル数
all_cell_count = edge*edge

# ８方向計算用
directions = [-edge-1,-edge,-edge+1,-1,1,edge-1,edge,edge+1]

# 特定のセルに対して、隣接する生存セルの数を返す
def count_O_side(cell):
	count = 0
	print('対象セル：'+square[cell])

	for direct in directions:
		checkcell = cell + direct
		# print(checkcell)
		if checkcell>=0 and checkcell<all_cell_count:
			# print('列：{0}'.format(cell % edge))
			# 左辺は左隣をスキップ
			if cell % edge == 0 and (direct == - 1 or direct == -edge -1 or direct == edge -1):
				print("left skip!")
				continue
			# 右辺は右隣をスキップ
			if cell % edge == edge-1 and (direct == 1 or direct == -edge +1 or direct == edge +1):
				print("right skip!")
				continue

			# print(square[checkcell])
			if square[checkcell] == "O":
				count += 1
				print("O")
			else:
				print("X")


		else:
			print("out range!")

	return count

# メイン処理開始
for num in range(all_cell_count):

    cell = "X"
    for live_num in first_live:
        if (num)==live_num:
            cell = "O"
            break

    square += cell
    print_square += cell

    if (num+1)%10==0:
        print_square += "\n"

print(print_square)
print(count_O_side(int(args[1])))


