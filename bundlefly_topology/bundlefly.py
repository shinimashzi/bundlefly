import networkx as nx
import configparser
from utils import get_xi_Xq_Xq_, get_a_bijection
import utils


def config_parse(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config


class Bundlefly:
    def __init__(self, config):
        self.k = config.getint('network', 'k')  # radix
        self.q = config.getint('network', 'q')  # MMS graph parameter

        self.a = config.getint('network', 'a')  # Paley graph parameter
        self.p = config.getint('network', 'p')  # one router connect p terminals
        self.save_path = config.get('network', 'output_path')

        self.Nr = -1  # the number of routers
        self.N = -1  # the number of all nodes in topology
        self.channels = -1

        self.compute_net_size()

        self.G = nx.Graph()
        for i in range(self.Nr):
            self.G.add_node(i)

        self.network()
        # self.output()

    def compute_net_size(self):
        k, q, a, p = self.k, self.q, self.a, self.p
        self.Nr = 2 * a * q * q
        self.N = 2 * a * q * q * p
        self.channels = self.Nr * k
        print("net size: ")
        print("Nr: ", self.Nr)
        print("N: ", self.N)
        # print("channels: ", self.channels)

    def connect_two_supernode(self, u_tripe, v_tripe, bijection_a):
        for b in range(self.a):
            b_node = [x for x in u_tripe]
            b_node.append(b)
            phi_b = bijection_a[b]
            a_node = [x for x in v_tripe]
            a_node.append(phi_b)
            self.G.add_edge(utils.convert_quad_id(b_node, self.a, self.q), utils.convert_quad_id(a_node, self.a, self.q))

    def network(self):
        axi, Xa, Xa_ = get_xi_Xq_Xq_(self.a)
        qxi, Xq, Xq_ = get_xi_Xq_Xq_(self.q)
        bijection_a = get_a_bijection(self.a)
        print(Xq)
        print(Xq_)
        # some router in supernode connections
        for i in range(0, self.Nr, self.a):
            one_a_ori = [node for node in range(i, i + self.a)]
            for index_u in range(self.a):
                for index_v in range(index_u + 1, self.a):
                    u = one_a_ori[index_u] - i * self.a
                    v = one_a_ori[index_v] - i * self.a
                    if (v - u) % self.a in Xa:
                        self.G.add_edge(one_a_ori[index_u], one_a_ori[index_v])

        # connections of columns of graph0 and graph1, if j-i%q in Xq/Xq', j and i are connected
        edge_0, edge_1 = 0, 0
        for col in range(self.q):
            for u in range(self.q):
                for v in range(u + 1, self.q):
                    if (v - u) % self.q in Xq:
                        self.connect_two_supernode([0, u, col], [0, v, col], bijection_a)
                        edge_0 += 1
                    if (v - u) % self.q in Xq_:
                        self.connect_two_supernode([1, u, col], [1, v, col], bijection_a)
                        edge_1 += 1

        # connections between two graphs
        # 0 - 1
        for r0 in range(self.q):
            for c0 in range(self.q):

                for r1 in range(self.q):
                    for c1 in range(self.q):
                        if ((c0*c1+r1)%self.q) == r0:
                            self.connect_two_supernode([0, r0, c0], [1, r1, c1], bijection_a)

        print(len(self.G.edges))
        print(len(self.G.nodes))

    def output(self):
        with open(self.save_path, "w", encoding='utf-8') as f:
            p_num = 0
            for router in range(self.Nr):
                one_data = "router " + str(router) + " "

                edges_router=0
                for connected_router in nx.all_neighbors(self.G, router):
                    edges_router +=1
                    one_data += "router " + str(connected_router) + " "

                for p in range(self.p):
                    one_data += "node " + str(p_num)
                    p_num += 1
                    if p != self.p-1:
                        one_data += " "
                one_data += "\n"
                f.write(one_data)


if __name__ == "__main__":
    config_file = "config.ini"
    config = config_parse(config_file)
    bundlefly = Bundlefly(config)
    bundlefly.output()




