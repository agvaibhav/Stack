def span(price):

    n = len(price)
    S=[1]
    st=[0]
    print(st[-1])
    for i in range(1,n):
    
        while(len(st) > 0 and price[st[-1]]<=price[i]):
            st.pop()

        if(len(st) > 0 and price[st[-1]]>price[i]):
            S.append(i-st[-1])

        else:
            S.append(i)
            
        st.append(i)

    print(S)
    

price=[100, 80, 60,70,60,75,85]
span(price)

