def ryerson_letter_grade(pct):
    grade=''
    if pct>89:
        grade='A+'
    elif pct>84:
        grade='A'
    elif pct>79:
        grade='A-'
    elif pct>76:
        grade='B+'
    elif pct>72:
        grade='B'
    elif pct>69:
        grade='B-'
    elif pct>66:
        grade='C+'
    elif pct>62:
        grade='C'
    elif pct>59:
        grade='C-'
    elif pct>56:
        grade='D+'
    elif pct>52:
        grade='D'
    elif pct>49:
        grade='D-' 
    else:
        grade='F'    
    return(grade)





def is_ascending(items):
    flag=0
    for x in range(1,len(items),1):
        if items[x-1]>=items[x]:
            flag+=1
    if flag>0:
        return(False)
    else:
        return(True)





def riffle(items, out = True):
    result=[]
    half1=items[:len(items)//2]
    half2=items[(len(items)//2):]
    if out:
        for x in range(len(items)//2):
            result.append(half1[x])
            result.append(half2[x])
    else:
        for x in range(len(items)//2):
            result.append(half2[x])
            result.append(half1[x])
    return(result)





def only_odd_digits(n):
    result=True
    wList=list(str(n))
    for x in range(len(wList)):
        if int(wList[x])%2==0:
            result=False
    return(result)





def pyramid_blocks(n,m,h):
    total=0
    for x in range(h):
        total+=(n+x)*(m+x)
    return(total)





def is_cyclops(n):
    numz=0
    result=False
    wList=list(str(n))
    for x in range(len(wList)):
            if int(wList[x])==0:
                numz+=1
    if numz!=1 or len(wList)%2==0:
        result=False
    elif numz==1 and int(wList[len(wList)//2])==0:
        result=True
    return(result)





def domino_cycle(tiles):
    flag=0
    if tiles==[]:
        result=True
    else:
        for x in range(len(tiles)):
            if tiles[x][0]!=tiles[x-1][1]:
                flag+=1
        if flag==0 and tiles[0][0]==tiles[-1][1]:
            result=True
        else:
            result=False
    return(result)


        
        
        
        
        
def count_distinct_sums_and_products(items):
    distinct={''}
    distinct.remove('')
    for x in range(len(items)):#root num
        
        for y in range(len(items)):#other number
            distinct.add(items[x]+items[y])
            distinct.add(items[x]*items[y])
            
    return(len(distinct))









def pancake_scramble(text):
    wList=list(text)
    word=[]
    
    for x in range(len(text)):
        
        for y in range(x,-1,-1):
            word.append(wList[y])
        
        for y in range(x+1,len(text)):
            word.append(wList[y])
        wList=word
        word=[]
            
    result=''.join(wList)
    
    return(result)





def first_missing_positive(items):
    a=items
    count=1
    missingNum=0
    for y in range(len(a)):
        for x in range(len(a)): 
            if a[x]==count:
                count+=1
                break
        if count!=y+2:
            missingNum=count
            break

    return(missingNum)





def is_permutation(items, n):
    if sorted(items)==sorted(list(range(1,n+1))):
        return(True)
    else:
        return(False)

    
def double_until_all_digits(n, giveup = 1000):
      
    num=n
    counter=0
    numList=list(str(num))
    result=-1
    
    for z in range(giveup):
        numList=list(str(num))
        for x in range(10):
            for y in range(len(numList)):
           
                if int(numList[y])==counter:
                    counter+=1
                    break      
        if counter==10:
            result=z
            break
            
        else:
            num*=2
            counter=0
    
    return(result)





def remove_after_kth(items, k = 1):
    
    seen={}
    results=[]
    flag=0
    
    for x in range(len(items)):
        
        for key in seen:
            if items[x]==key:#if in dict
                if seen[key]<k: #if not at k iterations yet
                    seen[key]+=1
                    results.append(items[x])
            else: #if the word is not in dict
                flag+=1
                
        if flag==len(seen): #adding completly new word
            seen[items[x]]=1
            results.append(items[x])
        flag=0
            
    return(results)





def first_preceded_by_smaller(items, k = 1):
    count=0
    
    for x in range(len(items)): #running all values in items

        for y in range(x,-1,-1): #running backwards from k
            if items[y]<items[x]:
                count+=1
            
        if count>=k:
            return(items[x])
        count=0
        
    return(None)





def maximum_difference_sublist(items, k = 2):
    subSetValues={}
    results=[]    
    for first in range(len(items)-k+1):
        max,min=items[first],items[first]        
        for x in range(k): #Find max and min                
            if items[x+first]>max:
                max=items[x+first]          
            if items[x+first]<min:
                min=items[x+first]                         
        subSetValues[first]=max-min
        max,min=0,0    
    for best in subSetValues:#finding highest difference
        if subSetValues[best]>max:
            max=subSetValues[best]  
    for x in subSetValues.keys(): #where to start to get best/first substring
        if subSetValues[x]==max:
            startVal=x
            break
    for x in range(k): #appending the best substring to results
        results.append(items[x+startVal])
    return(results)   
  
    
    
    
def count_and_say(digits):
    numList=list(digits)
    results=[]
    numCount=0
    reading=numList[0]
    
    for x in range(len(digits)):
        
        if reading==numList[x]:
            numCount+=1
        else:
            results.append(str(numCount))
            results.append(reading)
            reading=numList[x]
            numCount=1
    
    results.append(str(numCount))
    results.append(reading)         
    final=''.join(results)
    return(int(final))
    
    
def safe_squares_rooks(n, rooks):
    area=n*n
    rowsTaken=[]
    colTaken=[]
    for x in range(len(rooks)):
        #removing rows
        if rooks[x][0] not in rowsTaken:
            area-=n
            rowsTaken.append(rooks[x][0])
    for x in range(len(rooks)):
        #removing colums
        look=rooks[x]
        if look[1] not in colTaken:
            for x in range(n):
                if x not in rowsTaken:
                    area-=1
            colTaken.append(look[1])
    return(area)
    
    
    
def squares_intersect(s1, s2):
    result=False
    if s2[0]<=s1[0]+s1[2] and s1[0]<=s2[0]+s2[2]:#do they intersect in the x direction?
    
        if s2[1]<=s1[1]+s1[2] and s1[1]<=s2[1]+s2[2]: #do they intersect in the y direction?
        
            result=True
    return(result)
    
    
    
def group_equal(items):
    final,run=[],[]
    for x in range(len(items)):
        current=items[x]
        
        if current in run or run==[]:
            run.append(current)
        else:
            final.append(run)
            run=[]
            run.append(current)
    final.append(run)
    return(final)
    
    
    
def all_cyclic_shifts(text): #THIS ONE FAILED
    wList=list(text)
    newWord,final=[],[]
    for x in range(len(wList)):
        
        for y in range(1,len(wList)):
            newWord.append(wList[y])
        newWord.append(wList[0])
        wList=newWord
        if (''.join(newWord)) not in final:
            final.append(''.join(newWord))
        newWord=[]
    final.sort()
    return(final)
    
    
    
def give_change(amount, coins):
    result=[]
    currency=coins
    pos=0
    money=amount
    while True:
        if (money//currency[pos])>0:
            result.append(currency[pos])
            money-=currency[pos]
        else:
            pos+=1
            if pos>len(currency)-1:
                break
    return(result)
    
    

    
    
    
    
def scrabble_value(word, multipliers = None):
    wList=list(word)
    score=0
    points={'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10 }
    for x in range(len(wList)):
        if multipliers==None:  
            score+=points[wList[x]]
        else:
            score+=points[wList[x]]*multipliers[x]
    return(score)
    
    
    
    
def detab(text, n = 8, sub = ' '):
    wList=list(text)
    result=[]
    count=0
    for x in range(len(wList)):
        if wList[x]!='\t':
            result.append(wList[x])
            
        elif (x+count)%n!=0:
            result.append(sub)
            count+=1
            while (count+x)%n!=0:
                result.append(sub)
                count+=1
        else:
            result.append(wList[x])
    return(''.join(result))



def create_zigzag(rows, cols, start = 1):
    sides,final=[],[]
    count=start
    
    for x in range(rows):
        
        if x%2==0:
            for y in range(cols):
                sides.append(count)
                count+=1
        else:
            for y in range(count+cols-1,count-1,-1):
                sides.append(y)
                count+=1
    
        final.append(sides)
        sides=[]
        
    return(final)




def bridge_hand_shape(hand):
    spade,dia,club,heart=0,0,0,0
    for x in range(len(hand)):
        if hand[x][1]=='spades':
            spade+=1
        elif hand[x][1]=='clubs':
            club+=1
        elif hand[x][1]=='diamonds':
            dia+=1
        elif hand[x][1]=='hearts':
            heart+=1
    final=[spade,heart,dia,club]

    return(final)




def count_consecutive_summers(n):
    
    final=1
    for x in range(1,n+1):
        sum=x
        pointer=1
        
        while sum<=n:
            sum+=(x+pointer)
            pointer+=1
            
            if sum==n:
                final+=1
            
    return(final)




def iterated_remove_pairs(items):
    fail=0
    
    while fail!=1:
        fail=1
        for x in range(len(items)):
            if items[x-1]==items[x] and x<len(items) and x!=0:
                del(items[x])
                del(items[x-1])
                fail=0
                break
    return(items)




def expand_intervals(intervals):
    wList=intervals.split(',')
    final=[]
    for x in range(len(wList)):
        
        if '-' in wList[x]:
            test=wList[x].split('-')
            for y in range(int(test[0]),int(test[1])+1):
                final.append(y)
        else:
            final.append(int(wList[x]))

    return(final)




def reverse_reversed(items):
    
    items=items[::-1]
    for x in range(len(items)):
        if type(items[x])==list:
            items[x]=reverse_reversed(items[x])
            
    return(items)


def winning_card(cards, trump = None):
    
    
    ranks = {'deuce' : 2, 'trey' : 3 , 'four' : 4, 'five' : 5,
         'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9,
         'ten' : 10, 'jack' : 11, 'queen' : 12, 'king' : 13,
         'ace' : 14 }
    
    finalVal=0
    final=''
    
    #is trump in the hand?
    nope=0
    for x in range(4):
        if cards[x][1]==trump:
            nope+=1
    
    if trump==None or nope==0:
        for x in range(len(cards)):
            if cards[x][1]==cards[0][1]:
                if ranks[cards[x][0]]>finalVal:
                    finalVal=ranks[cards[x][0]]
                    final=cards[x][0]
        final=(final,cards[0][1])
        
        
        
    elif trump!=None:
        for x in range(len(cards)):
            if cards[x][1]==trump:
                if ranks[cards[x][0]]>finalVal:
                    finalVal=ranks[cards[x][0]]
                    final=cards[x][0]
        final=(final,trump)
    
    return(final)




def sort_by_typing_handedness(words):
    wList=list(words)
    scores={}
    mid=[]
    final=[]
    leftLetters=('q','w','e','r','t','y','a','s','d','f','g','h','z','x','c','v','b')
    leftscore=0
    rightscore=0
    val=-100   
    for x in range(len(wList)):
        letters=list(wList[x])
        for y in range(len(letters)):
            if letters[y].lower() in leftLetters:
                leftscore+=1
            else:
                rightscore+=1
        
        scores[wList[x]]=leftscore-rightscore
        leftscore=0
        rightscore=0
        
    # find lowest value
    for keys in scores:
        if scores[keys]>val:
            val=scores[keys]
    
    while val>-50:
        for x in scores:
            if scores[x]==val:
                mid.append(x)
        if mid!=[]:
            final+=sorted(mid)
        val-=1
        mid=[]

    return(final)
