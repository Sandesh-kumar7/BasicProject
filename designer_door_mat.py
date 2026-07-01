height,width=map(int,input().split())
index_number=1
for i in range(1,height+1):
    
    if i<(height//2)+1:
        print((index_number*'.|.').center(width,'-'))
        index_number+=2
    elif i==(height//2)+1:
        print('WELCOME'.center(width,'-'))
        index_number-=2
    
    else:
        print((index_number*'.|.').center(width,'-'))
        index_number-=2