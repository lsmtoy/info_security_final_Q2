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
            # result = (result * temp) % divider
            # print('i is: ', i, '\t', c,'^',2**i,'mod',n,'is:\t',temp_m,'\tm is:',m)
            cnt = 1
        exp = exp >> 1
    print('result is: ', result)
    return result


def find_disc_log(base, divider, result):
    for i in range(1,divider):
        if mod(base, i, divider) == result:
            print(base,'^',i,'mod',divider,'is: ',result)
            return i
    print('no answer')


if __name__ == '__main__':
    '''
    q = 2934201397
    a = 37
    Ya = 2174919958     # Ya = a ^ Xa   mod
    Xa = 83
    #C1 = 2909170161; C2 = 2565161545
    C1 = 2909170161; C2 = 1004005362       # M = 189465461
    #C1 = 2909170161; C2 = 2081016632       # M = 848963461
    '''

    q = 19
    a = 10
    Ya = 3  # Ya = a ^ Xa   mod
    Xa = 1  # Xa = 5
    C1 = 11 ; C2 = 5

    Xa = find_disc_log(a, q, Ya)
    K = mod(C1, Xa, q)
    inverse_K = 1

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

    K = mod(a,Xa,q)
    print('K:',K)

    '''
    Euclidean algorithm to find inverse_K
    '''
    temp_q = q
    a1 = 1; a2 = 0; a3 = temp_q
    b1 = 0; b2 = 1; b3 = K;
    Q = 1
    gcd = 0;

    while (1):
        if (b3 == 0):
            gcd = a3;
            break
        elif (b3 == 1):
            gcd = b3;
            inverse_K = b2;
            if (inverse_K < 0):
                inverse_K += temp_q;
            break;
        else:
            Q = math.floor(a3 / b3);
            t1 = a1 - Q * b1; t2 = a2 - Q * b2;  t3 = a3 - Q * b3;
            a1 = b1; a2 = b2; a3 = b3;
            b1 = t1; b2 = t2; b3 = t3;

    print('inverse_K is: ', inverse_K)
    #print( K*(inverse_K + q) % q)
    print('M is: ', C2*inverse_K % q)















