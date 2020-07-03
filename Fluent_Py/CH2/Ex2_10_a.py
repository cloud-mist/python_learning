# E1:why slices and range exclude the last item
'''
    1.easy to see the length
    2.easy to compute the length
    3.easy to split a sequence in two parts
'''
l = [10, 20, 30, 40, 50, 60]
print(l[:2])            # [10, 20] 
print(l[2:])            # [30, 40, 50, 60]


# E2:s[a:b:c]的说明   以c为步，负值反向
s = 'bicycle'
print(s[::3])           # bye
print(s[::-1])          # elcycib
print(s[::-2])          # eccb


# E3:纯文本形式的收据 以一行字符串的的形式被解析
invoice = """  
        8                           36
1909    pimoroni pibrella           $17.50    3    $52.50
1489    6mm tactile switch x20      $4.95     2    $9.90
1510    panavise jr                 $28.00    1    $28.00
1601    pitft mini kit              $34.95    1    $34.95
"""

SKU = slice(0,8)
DESCRIPITION = slice(8, 36)
UNIT_PRICE = slice(36, 44)
QUANTITY = slice(44, 48)
ITEM_TOTAL = slice(48, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPITION])
'''     ***** Result *****
$17.50   pimoroni pibrella
$4.95    6mm tactile switch x20
$28.00   panavise jr
$34.95   pitft mini kit
'''
