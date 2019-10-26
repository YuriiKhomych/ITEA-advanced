#condition 1
a=[1,True,'hello']
if 'hello' in a:
    a.append('world')
    if len(a[3])<2:
        a[1]='wonderful'
        print(a)
    elif 'world' in a:
        a.remove(a[0])
        print(a)
    else:
        a.clear()
        print(a)
else:
    print("we don't have it there")

