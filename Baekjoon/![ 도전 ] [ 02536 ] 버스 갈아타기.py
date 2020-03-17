# https://www.acmicpc.net/problem/2536

import sys
I = sys.stdin.readline


def check(srr1, scc1, err1, ecc1, srr2, scc2, err2, ecc2):
    sr1 = srr1 <= srr2 and srr1 or srr2
    sr2 = srr1 <= srr2 and srr2 or srr1
    er1 = err1 <= err2 and err1 or err2
    er2 = err1 <= err2 and err2 or err1
    
    sc1 = scc1 <= scc2 and scc1 or scc2
    sc2 = scc1 <= scc2 and scc2 or scc1
    ec1 = ecc1 <= ecc2 and ecc1 or ecc2
    ec2 = ecc1 <= ecc2 and ecc2 or ecc1

    if sr1 == sr2 == er1 == er2:
        if \
            check_include(sr1, sc1, er1, ec1, sr2, sc2, er2, ec2) or\
            check_include(sr2, sc2, er2, ec2, sr1, sc1, er1, ec1) or\
            check_part(sr1, sc1, er1, ec1, sr2, sc2, er2, ec2) or\
            check_part(sr2, sc2, er2, ec2, sr1, sc1, er1, ec1):
            return True
    if sc1 == sc2 == ec1 == ec2:
        if \
            check_include(sc1, sr1, ec1, er1, sc2, sr2, ec2, er2) or\
            check_include(sc2, sr2, ec2, er2, sc1, sr1, ec1, er1) or\
            check_part(sc1, sr1, ec1, er1, sc2, sr2, ec2, er2) or\
            check_part(sc2, sr2, ec2, er2, sc1, sr1, ec1, er1):
            return True

    if sc1 <= sc2 == ec2 <= ec1:
        
    if sc2 <= sc1 == ec1 <= ec2:

    
    

def check_include(sr1, sc1, er1, ec1, sr2, sc2, er2, ec2):
    if sr1 <= sr2 <= er2 <= er1:
        return True
    return False

def check_part(sr1, sc1, er1, ec1, sr2, sc2, er2, ec2):
    if sr1 <= sr2 <= er1 <= ec2:
        return True
    return False

C, R = map(int, I().split())
B = int(I())
arr = [list(map(int, I().split())) for _ in range(B)]
sc, sr, ec, er = list(map(int, I().split()))

adj = [[] for _ in range(B)]
for b1, scc1, srr1, ecc1, err1 in arr:
    for b2, scc2, srr2, ecc2, err2 in arr:
        if b1 == b2:
            continue

        