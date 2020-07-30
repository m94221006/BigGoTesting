"""
Created on Jul 29 2020

@author: ricky
"""


if __name__ == "__main__":
    center_size = 20
    tree = "\ /".center(center_size)+"\n"
    tree += "-->*<--".center(center_size)+"\n"
    for i in range (6):
        word = '/_\\'
        if i == 1:
            word = '/_\_\\'
        elif i>=2:
            word = ("/"+"_/"*i+('_\\')).center(center_size)+"\n"+("/"+"_\\"*i+('_\\')).center(center_size)
        tree+= word.center(center_size)+"\n"
    tree += "|__|".center(center_size)
    print(tree)