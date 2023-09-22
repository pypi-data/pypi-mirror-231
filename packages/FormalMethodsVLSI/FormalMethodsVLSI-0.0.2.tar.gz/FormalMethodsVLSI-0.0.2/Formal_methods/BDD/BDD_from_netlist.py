from functools import cached_property,reduce,lru_cache
import networkx as nx
from .netlist import *
from dd import BDD
import operator as op
from tqdm import tqdm

__all__ = ["BDD_from_netlist"]

class BDD_from_netlist(Netlist):
    def __init__(self,file):
        super().__init__(file)
        self._bdd = BDD() 
        self.prob = dict()   # signal probabilities
        self.table = dict()  # to save all the computed nets

    def __str__(self):
        return f"BDD for {repr(self.dag)}"

    def __repr__(self):
        return f"BDD_from_netlist({self.file})"

    @lru_cache(maxsize = 128)
    def probability(self,u):
        if not u.low : return 1 # leaf node?
        low, high = u.low, u.high 
        p = self.prob[u.var]
        if low.negated: # if low edge is complemented
            return ((1 - self.probability(low))*(1 - p) +
                    self.probability(high)*p)
        return (self.probability(low)*(1 - p) +
                self.probability(high)*p)

    def __len__(self):
        if len(self._bdd) == 1:
            raise AssertionError(
                    "No BDD is built,call "
                    "`bdd.find_probabilities` first")
        return len(self._bdd)

    @cached_property
    def cutnodes(self):
        G = self.dag
        return G.all_cutnodes(self.outputs)

    def find_probabilities(self,input_probabilities = {},
                           useCutnodes = False, ordering = None):
        G = self.dag
        nodes_list = G.nodes
        And,Or,Xor = op.and_,op.or_,op.xor
        table = self.table
        bdd = self._bdd
        bdd.declare(*self.inputs) # declare primary inputs as variables
        cutnodes = set()
        if useCutnodes:
            cutnodes = self.cutnodes
            bdd.declare(*cutnodes)
        if ordering:
            bdd.configure(reordering = False)
            bdd.reorder(var_order = ordering)

        table.update({primary_input : bdd.var(primary_input)
                      for primary_input in self.inputs})
        self.prob.update(input_probabilities)

        if not input_probabilities :
            self.prob = {primary_input : 0.5 for primary_input in self.inputs}
        progress_bar = tqdm(nx.topological_sort(G),total = len(nodes_list))

        for node in progress_bar:
            gate_type = nodes_list[node].get("type")
            if gate_type:
                inputs = [table[net] for net in G.pred[node]]
                output = list(G.succ[node])[0]
                description = italic_text(f"Finding probability of {output}")
                progress_bar.set_description(description)
                if gate_type == "nand":
                    expr = reduce(And,inputs)
                    expr = ~expr
                elif gate_type == "nor":
                    expr = reduce(Or,inputs)
                    expr = ~expr
                elif gate_type == "and":
                    expr = reduce(And,inputs)
                elif gate_type == "or":
                    expr = reduce(Or,inputs)
                elif gate_type == "inv":
                    expr = ~inputs[0]
                elif gate_type == "buf":
                    expr = inputs[0]
                elif gate_type == "xor":
                    expr = reduce(Xor,inputs)
                elif gate_type == "xnor":
                    expr = reduce(Xor,inputs)
                    expr = ~expr
                else:
                    raise TypeError(f"Invalid gate_type {gate_type} in netlist") 
                u = table[output] = expr
                # for `cudd` garbage collection is automatic
                # bdd.collect_garbage()
                if not ordering: 
                    bdd.reorder()
                po = self.probability(u)
                self.prob[output] = (1 - po) if u.negated else po
                if output in cutnodes:
                    del u
                    table[output] = bdd.var(output)
                """
                # for checking whether probabilities are calculated correctly
                n = len(u.support) 
                SATcount = u.count()
                assert isclose(self.prob[output], SATcount/2**n)
                """
            else:
                continue
        print(green_text("done"))

    @property
    def ordering(self):
        return self._bdd.var_levels
