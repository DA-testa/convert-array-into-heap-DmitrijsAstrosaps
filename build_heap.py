# python3Arr


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n=len(data)
    for i in range(n//2-1,-1,-1):
        sort_Butt(data,i,swaps)

    return swaps

def sort_Butt(data, i, swaps):
    n=len(data)
    MI = i
    LCh = 2*i+1
    RCH = 2*i+2

    if(RCH<=n-1 and data[RCH]<data[MI]):
        MI = RCH
    if(LCh<=n-1 and data[LCh]<data[MI]):
        MI = LCh
    if(MI!=i):
        swaps.append((i,MI))
        data[i],data[MI]=data[MI],data[i]
        swap = sort_Butt(data,MI,swaps)

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    Che = input()
    if "F" in Che:
        FN = input()
        if "a" in FN:
            return
        else:
            with open("./tests/"+FN,'r') as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
                assert len(data) == n
                swaps = build_heap(data)
    elif "I" in Che:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
    else:
        return

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
