# Please write assert statements to verify that every number in the list [2,4,6,8] is even.
# Hints: Use “assert expression” to make assertion.


listofnum=[2,4,7,8]


try:
    for x in listofnum:
        assert x%2==0
except:
    print(f"some element is {x}not even ")