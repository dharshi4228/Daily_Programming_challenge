def bars(height):
    l,r = 0,len(height)-1
    maxL,maxR = height[l],height[r]
    water = 0
    while l<r:
        if maxL < maxR :
            l+=1
            maxL = max(height[l],maxL)
            water+= maxL - height[l]
        else:
            r-=1
            maxR = max(height[r],maxR)
            water += maxR - height[r]
    return water

def main():
    height_input=input("Enter the array")
    height=list(map(int,height_input.split(',')))
    output = bars(height)
    print(output)
if __name__=="__main__":
    main()
   