'''
Title: Treasure Map
Description: The program creates a list resembling a map. The user can then choose where to mark an X on the map. 
Utilized: random module, lists & nested lists, if/elif/else statements
'''

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

'''
Map visualization:
    1    2    3
1 "⬜️" "️⬜️" "️⬜️"
2 "⬜️" "️⬜️" "️⬜️"
3 "⬜️" "️⬜️" "️⬜️"
'''
#Split string so that the positions are seen individually as columns and rows.
column = 0
column += int(position)

if column == 11:
    row1[0] = "X"
    print(f"{row1}\n{row2}\n{row3}")
elif column == 21:
    row1[1] = "X"
    print(f"{row1}\n{row2}\n{row3}")
elif column == 31:
    row1[2] = "X"
    print(f"{row1}\n{row2}\n{row3}")


elif column == 12:
    row2[0] = "X"
    print(f"{row1}\n{row2}\n{row3}")
elif column == 22:
    row2[1] = "X"
    print(f"{row1}\n{row2}\n{row3}")
elif column == 32:
    row2[2] = "X"
    print(f"{row1}\n{row2}\n{row3}")

elif column == 13:
    row3[0] = "X"
    print(f"{row1}\n{row2}\n{row3}")
elif column == 23:
    row3[1] = "X"
    print(f"{row1}\n{row2}\n{row3}")
elif column == 33:
    row3[2] = "X"
    print(f"{row1}\n{row2}\n{row3}")