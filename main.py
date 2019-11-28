import math

def mod(base, exp, divider):
    cnt = 0  # counter
    result = 1  # plaintext
    temp = base
    for i in range(0, 64):
        j = 1 & exp
        if (j == 0):
            # print('i is: ', i)
            cnt = cnt + 1
        else:
            temp = (temp ** (2 ** cnt)) % divider
            result = (result * temp) % divider
            # print('i is: ', i, '\t', c,'^',2**i,'mod',n,'is:\t',temp_m,'\tm is:',m)
            cnt = 1
        exp = exp >> 1
    print('result is: ', result)
    return result

if __name__ == '__main__':
    q = 2934201397
    a = 37
    Ya = 2174919958     # Ya = a ^ Xa   mod
    Xa = 83
    C1 = 2909170161
    C2 = 2565161545
    K = 1

    '''
    Xa의 값을 구하는 코드
    temp = 1
    for i in range (1, q-1):
        print("i is: ", i)
        temp = temp*a
        if(temp % q == Ya):
            Xa = i
            break
    '''

    #K = mod(a, 83, q)
    #print('K is: ',K)


    K = mod(11,23,187)

    '''
    cnt = 0  # counter
    K = 1  # plaintext
    temp_k = C1
    for i in range(0, 64):
        j = 1 & Xa
        if (j == 0):
            # print('i is: ', i)
            cnt = cnt + 1
        else:
            temp_m = (temp_k ** (2 ** cnt)) % q
            K = (K * temp_k) % q
            # print('i is: ', i, '\t', c,'^',2**i,'mod',n,'is:\t',temp_m,'\tm is:',m)
            cnt = 1
        Xa = Xa >> 1
    print('K is: ',K)
    '''

    '''
    #C1 = a^k mod q
    temp_c1 = 1
    cnt = 0  # counter
    temp_k = C1
    for i in range(0, 64):
        j = 1 & K
        if (j == 0):
            # print('i is: ', i)
            cnt = cnt + 1
        else:
            temp_c1 = (temp_c1 ** (2 ** cnt)) % q
            C1 = (C1 * temp_c1) % q
            # print('i is: ', i, '\t', c,'^',2**i,'mod',n,'is:\t',temp_m,'\tm is:',m)
            cnt = 1
        K = K >> 1
    print('C1 is: ', C1)
    '''

    '''
    a1 = 1
    a2 = 0
    a3 = q
    b1 = 0
    b2 = 1
    b3 = K
    gcd = 0;

    while (1):
        if (b3 == 0):
            gcd = a3;
            break
        elif (b3 == 1):
            gcd = b3;
            d = b2;
            if (d < 0):
                d += PI_n;
            break;
        else:
            q = math.floor(a3 / b3);
            t1 = a1 - q * b1;
            t2 = a2 - q * b2;
            t3 = a3 - q * b3;
            a1 = b1;
            a2 = b2;
            a3 = b3;
            b1 = t1;
            b2 = t2;
            b3 = t3;
    '''


    print('M is: ',C2/K % q)















