'''
3 bottles of beer on the wall.
3 bottles of beer.
Take one down.
Pass it around.
2 bottles of beer on the wall.

(...)
1 ...
(...)
No more bottles of beer on the wall.
'''
word = "bottles"

for bottle_count in range(99, 0, -1):
    print(bottle_count, word, "of beer on the wall.")
    print(bottle_count, word, "of beer.")
    print("Take on down.\nPass it around.")
    if bottle_count ==1:
        print("No more bottles of beer on the wall.\n")
    else:
        new_num = bottle_count -1
        if new_num ==1:
            word = "bottle"
            print(new_num, word, "of beer on the wall.\n")
        else:
            print(bottle_count -1, word, "of beer on the wall.\n")
        
    

          
