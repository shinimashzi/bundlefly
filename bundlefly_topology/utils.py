import networkx as nx
from networkx.algorithms import isomorphism

"""
1. 求本原根、对应Xq，Xq'

2. 论文中定义的双射

3. 网络中的id和四元组相互转换
"""


def convert_id_quad(id, a, q):
    quad = [-1, -1, -1, -1]
    sum = id
    subgraph_num = a*q*q
    quad[0] = int(id // subgraph_num)
    sum -= subgraph_num if sum > subgraph_num else 0
    quad[1] = int(sum // (q*a))
    sum = sum%(q*a)
    quad[2] = int(sum // a)
    sum = sum%a
    quad[3] = sum
    return quad


def convert_quad_id(quad, a, q):
    sum = 0
    subgraph_num = a*q*q
    sum += quad[0]*subgraph_num
    sum += quad[1]*q*a
    sum += quad[2]*a
    sum += quad[3]
    return sum


# get one primitive element
def get_primitive_element(n):
    phi_n = n-1  # Fermat's little theorem, phi(x) = x-1, if x is a prime
    for xi in range(2, n-1):
        flag = 0
        x = 1
        while x <= phi_n:
            if xi**x % n == 1:
                flag = 1
                break
            x += 1
        if x == phi_n and flag:
            return xi
    return -1


# get Xq in paper
def get_X_q(q, xi):
    Xq_temp = []
    if q%4 == 0:
        for i in range(0, q-1, 2):
            Xq_temp.append(xi**i%q)
    elif q%4 == 1:
        for i in range(0, q-2, 2):
            Xq_temp.append(xi**i%q)
    else:
        wq = int((q+1)//4)
        for i in range(0, 2*wq-1, 2):
            Xq_temp.append(xi**i%q)
        for i in range(2*wq-1, 4*wq-2, 2):
            Xq_temp.append(xi**i%q)
        Xq__temp = []
        for i in range(1, 2*wq, 2):
            Xq__temp.append(xi**i%q)
        for i in range(2*wq, 4*wq-1, 2):
            Xq__temp.append(xi**i%q)

        Xq, Xq_ = [], []
        for x in range(1,q):
            if x in Xq_temp:
                Xq.append(x)
            if x in Xq__temp:
                Xq_.append(x)

    if q%4==0 or q%4==1:
        Xq, Xq_ = [], []
        for x in range(1, q):
            if x in Xq_temp:
                Xq.append(x)
            else:
                Xq_.append(x)
    else:
        pass
    return Xq, Xq_


def get_xi_Xq_Xq_(q):
    xi = get_primitive_element(q) # find one primitive element
    Xq, Xq_ = get_X_q(q, xi)
    return xi, Xq, Xq_


# define a bijection: ϕ(x) = x', x' is corresponding nodes in terms of isomorphism. x in Ga, x' in Ga'.
def get_a_bijection(a):
    a_xi, Xa, Xa_ = get_xi_Xq_Xq_(a)
    Ga = nx.Graph()
    Gb = nx.Graph()
    for i in range(a):
        Ga.add_node(i)
        Gb.add_node(i)

    for i in range(a):
        for j in range(i+1, a):
            if (j-i)%a in Xa:
                Ga.add_edge(i, j)
            if (j-i)%a in Xa_:
                Gb.add_edge(i, j)
    print(len(Ga.edges))
    print(len(Gb.edges))
    GM = isomorphism.GraphMatcher(Ga, Gb)
    print(GM.is_isomorphic())
    return GM.mapping


# 5:  2
# 7:  3
# 13: 2
# 17: 3
