#!/usr/bin/env python3

import os
import tempfile
import subprocess
import re
from math import sqrt, ceil, prod
import itertools
import abc
from random import Random

__version__ = "1.2.0"

_MyRandom = Random()


def seed(seed=None):
    """
    @brief seed treedecomposition random number generator

    Seeds the a local random number generator.
    This does not seed Python's global RNG (functions of module random)

    Without argument or seed==None, use pythons built-in random.seed()
    to generate a seed.
    """
    _MyRandom.seed(seed)


# @brief Class to hold a tree decomposition
#
# contains
#
# * bags   a list of 0-based indexed lists of vertices of the decomposed
#          graph (or "variables")
#
# * edges  a list of edges; an edge is a list of bags (bag1, bag2)
#
# * adj    adjacency lists (as defined by edges)
#
# edges are directed, an edge from bag x to y is represented by (x,y)
class TreeDecomposition:
    # @brief construct from bags and edges
    #
    # @param bags lists of indices of the variables (vertices) in the
    # bag
    #
    # @param edges list of edges between the bags; edges are
    # specified as pairs (x,y), where x is the index of the parent
    # bag and y, of the child bag (0-based indices according to
    # bags).
    #
    # Edges must be directed from root(s) to leaves. Typically the
    # bags and edges result from calling a tree decomposition
    # algorithm. The supported algorithms return correctly oriented
    # edges.
    def __init__(self, bags, edges):
        # copy bags
        self._bags = list(bags)
        # ensure that all edges are tuples or lists of length 2
        assert all(len(x) == 2 for x in edges)
        # copy edges and convert all edges to pairs (even if they
        # have been lists)
        self._edges = list(map(lambda x: (x[0], x[1]), edges))

        self.update_adjacency_lists()

    # @brief list of bags
    def get_bags(self):
        return self._bags

    # @brief list of edges
    def get_edges(self):
        return self._edges

    @property
    def bags(self):
        return self._bags

    @property
    def edges(self):
        return self._edges

    # @brief Comute adjacency list representation
    ##
    # @param n number of nodes
    # @param edges list of edges
    @staticmethod
    def adjacency_lists(n, edges):
        adj = {i: [] for i in range(n)}
        for i, j in edges:
            adj[i].append(j)
        return adj

    # @brief Update the adjacency representation
    ##
    # Updates the adjacency representation in adj according to the
    # number of bags and edges
    def update_adjacency_lists(self):
        self.adj = self.adjacency_lists(len(self._bags), self._edges)

    # @brief Toppological sort of bags
    ##
    # @returns sorted list of bag indices
    def toposorted_bag_indices(self):
        n = len(self._bags)

        visited = set()
        sorted = list()

        def toposort_component(i):
            visited.add(i)
            for j in self.adj[i]:
                if j not in visited:
                    toposort_component(j)
            sorted.append(i)

        for i in range(n):
            if i not in visited:
                toposort_component(i)
        return sorted[::-1]

    # @brief Difference set
    ##
    # @param xs first list
    # @param ys second list
    ##
    # @return ys setminus xs
    ##
    # For bags xs and ys, this computes the introduced variable
    # indices when going from parent xs to child ys.
    @staticmethod
    def diff_set(xs, ys):
        return [y for y in ys if y not in xs]

    # @brief Separator set
    ##
    # @param xs first list
    # @param ys second list
    ##
    # @return overlap of xs and ys
    ##
    # For bags xs and ys, this computes the 'separator' of xs and ys,
    # i.e. the common variables.
    @staticmethod
    def sep_set(xs, ys):
        return [y for y in ys if y in xs]

    # @brief Get tree width
    def treewidth(self):
        return max([len(bag) for bag in self._bags]) - 1

    # @brief Write tree decomposition in dot format
    # @param out output file handle
    def writeTD(self, out):
        def baglabel(bag):
            if len(bag) == 0:
                return ""

            lwidth = ceil(sqrt(len(bag)))
            lnum = ceil(len(bag) / lwidth)
            xs = [str(i) for i in sorted(bag)]
            lines = list()
            for i in range(0, lnum):
                lines.append(" ".join(xs[i * lwidth : (i + 1) * lwidth]))
            return "\\n".join(lines)

        out.write("digraph G {\n\n")

        for bagid, bag in enumerate(self._bags):
            label = baglabel(bag)
            out.write('\tbag{} [label="{}"]\n'.format(bagid + 1, label))

        out.write("\n\n")

        for x, y in self._edges:
            edgelabel = " ".join(
                [str(x) for x in self.diff_set(self._bags[x], self._bags[y])]
            )
            out.write(
                '\tbag{} -> bag{}  [label="{}"]\n'.format(x + 1, y + 1, edgelabel)
            )

        out.write("\n}\n")

    # @brief Guarantee a certain maximal diff set size
    ##
    # @param maxdiffsize maximum size of diff sets after transformation
    ##
    # @see diff_set()
    ##
    # @pre the tree is connected
    ##
    # Expands the tree by inserting a minimum number of in-between
    # bags whereever the diff set size exceeds maxdiffsize. This can
    # limit the complexity of certain algorithm based on the tree (in
    # particular sampling in Infrared).
    ##
    def expand_treedecomposition(self, maxdiffsize=1):
        def chunks(lst, n):
            """Yield successive n-sized chunks from lst."""
            for i in range(0, len(lst), n):
                yield lst[i : i + n]

        def expand(u, v, ubags, vbags):
            new_edges = []
            # determine diff set
            diff = self.diff_set(ubags, vbags)
            if len(diff) > maxdiffsize:
                if (u, v) in self._edges:
                    self._edges.remove((u, v))

                if (v, u) in self._edges:
                    self._edges.remove((v, u))

                last_bag_idx = u

                sep = self.sep_set(ubags, vbags)
                newbag = sep

                for ext in chunks(diff[:-1], maxdiffsize):
                    newbag.extend(ext)
                    new_bag_idx = len(self._bags)
                    self._bags.append(newbag[:])
                    new_edges.append([last_bag_idx, new_bag_idx])
                    last_bag_idx = new_bag_idx

                new_edges.append([last_bag_idx, v])
            return new_edges

        root = self.toposorted_bag_indices()[0]

        # perform depth first traversal
        visited = set()
        stack = [(None, root)]  # parent idx, bag index
        while stack:
            # pop
            (u, v) = stack[-1]
            stack = stack[:-1]

            if v in visited:
                continue
            visited.add(v)

            # push children on stack
            for w in self.adj[v]:
                stack.append((v, w))

            new_edges = expand(
                u, v, self._bags[u] if u is not None else [], self._bags[v]
            )
            if u is None and len(new_edges) > 1:
                new_edges = new_edges[1:]
            self._edges.extend(new_edges)

        self.update_adjacency_lists()


# ##########################################################
# writing graphs to files in different formats
#


# @brief Plot graph
# @param graphfile file of graph in dot format
#
# The graph is plotted and written to a pdf file by calling
# graphviz's dot tool on th dot file.
def dotfile_to_tgt(graphfile, tgt, outfile=None):
    if outfile is None:
        outfile = re.sub(r".dot$", "", graphfile) + "." + tgt
    subprocess.check_output(["dot", f"-T{tgt}", "-o", outfile, graphfile])


def dotfile_to_pdf(graphfile, outfile=None):
    dotfile_to_tgt(graphfile, "pdf", outfile)


def dotfile_to_png(graphfile, outfile=None):
    dotfile_to_tgt(graphfile, "png", outfile)


# @brief Write graph in dgf format
#
# @param out output file handle
# @param num_nodes number of nodes
# @param edges the edges of the graph
def write_dgf(out, num_nodes, edges):
    edge_num = len(edges)

    out.write("p tw {} {}\n".format(num_nodes, edge_num))
    for u, v in sorted(edges):
        out.write("e {} {}\n".format(u + 1, v + 1))


# @brief Write graph in dot format
#
# @param out output file handle
# @param num_nodes number of nodes
# @param edges the edges of the graph
def write_dot(out, num_nodes, edges):
    out.write("graph G{\n\n")

    for v in range(num_nodes):
        out.write('\tnode{idx} [label="{idx}"]\n'.format(idx=v))

    for u, v in edges:
        out.write("\tnode{} -- node{}\n".format(u, v))

    out.write("\n}\n")


###########################################################
# Interface TDlib
#
# specific functions to call TDlib's tree decomposition tool
# and parse the result
#


# @brief Parse tree decomposition as written by TDlib
#
# @param tdfh file handle to tree decomposition in dot format
# @param num_nodes number of nodes
# @returns tree decomposition
#
# Assume file is in td format as written by the tool TDlib.
def parseTD_TDlib(tdfh, num_nodes):
    bags = list()
    edges = list()

    for line in tdfh:
        # catch bags "New_vertex"
        if re.search("New_Vertex", line):
            bags.append([])
            continue

        m = re.search(r"bag(\d+).+label=\"(.+)\"", line)
        if m:
            bagid = int(m.group(1))
            label = m.group(2)
            labels = re.findall(r"\d+", label)
            labels = [int(label) for label in labels]
            if bagid != len(bags) + 1:
                raise IOError(
                    "Bag indices in td file must be consecutive"
                    " (at bag {})!".format(bagid)
                )
            bags.append(labels)
        else:
            m = re.search(r"bag(\d+) -- bag(\d+)", line)
            if m:
                edges.append((int(m.group(1)), int(m.group(2))))
    # decrease bag labels

    def dec(xs):
        return [[x - 1 for x in ys] for ys in xs]

    bags = dec(bags)
    edges = dec(edges)

    # add missing bags
    present = set()
    for b in bags:
        for x in b:
            present.add(x)

    for i in range(num_nodes):
        if i not in present:
            bags.append([i])

    return TreeDecomposition(bags, edges)


# @brief Compute tree decomposition of a graph by TDlib
##
# Generates tree decomposition and writes the result to file.
##
# @param filename base name for input .dfg and output .td files
# @param num_nodes number of nodes
# @param edges specifies edges of a graph; nodes are indexed 0-based
# @param strategy integer code of decomposition strategy:
# 1) Permutation To Tree Decomposition with GreedyDegree
# 2) Permutation To Tree Decomposition with GreedyFillIn
# 3) Permutation To Tree Decomposition with Lex-BFS: Lexicographic Breadth
#    First Search
# 4) Permutation To Tree Decomposition with MCS; Maximum Cardinality Search
# 5) PermutationGuesser
def makeTDFile_TDlib(filename, num_nodes, edges, *, strategy=2):
    inname = filename + ".dgf"
    outname = filename + ".td"

    with open(inname, "w") as dgf:
        write_dgf(dgf, num_nodes, edges)
        dgf.close()

        cmd = [
            "java",  # "-cp", tdlib_home,
            "nl.uu.cs.treewidth.TreeDecomposer",
            str(strategy),
            inname,
            outname
            # , filename+".dot"
        ]
        try:
            subprocess.check_output(cmd)
        except subprocess.CalledProcessError:
            print(
                "ERROR: Could not call TDlib; please make sure that TDlib "
                "is installed in the Java class path"
            )
            print(
                "       Possibly, you just need to set the environment "
                "variable CLASSPATH, like"
            )
            print("       export CLASSPATH=$tdlib_home/treewidth-java")
            exit(-1)

        os.remove(inname)

        return outname


# ###########################################################
# Interface tree demposition libraries
#


# @brief Base class of tree decomposition factories
#
# A TD factory needs to provide a method create to produce a class
# TreeDecomposition given the number of variables and the list of dependencies;
# dependencies are lists of lists of 0-based indices of the
# variables that respectively depend on each other
#
class TreeDecompositionFactoryBase:
    def __init__(self):
        pass

    # @brief Create tree decomposition
    #
    # @param size number of nodes in the dependency graph
    # @param dependencies specifies edges of the dependency (hyper-)graph;
    # nodes are indexed 0-based
    #
    # @return tree decomposition (object of TreeDecomp)
    @abc.abstractmethod
    def create(self, size, dependencies):
        return

    # @brief Expand non-binary dependencies to cliques of binary deps
    # @param dependencies list of dependencies
    # @return list of binary dependencies
    @staticmethod
    def expand_to_cliques(dependencies):
        bindeps = list()
        for d in dependencies:
            bindeps.extend(itertools.combinations(d, 2))
        return bindeps


# @brief Tree decomposition factory using HTD
class HTDTreeDecompositionFactory(TreeDecompositionFactoryBase):
    def __init__(self, maxdiffsize=1):
        self.maxdiffsize = maxdiffsize
        pass

    # @brief Create tree decomposition
    def create(self, size, dependencies):
        bindependencies = self.expand_to_cliques(dependencies)

        from libhtdwrap import HTD

        myhtd = HTD(size, bindependencies)
        myhtd.decompose()

        td = TreeDecomposition(myhtd.bags(), myhtd.edges())
        td.expand_treedecomposition(self.maxdiffsize)

        return td


# @brief Tree decomposition factory using TDlib
class TDLibTreeDecompositionFactory(TreeDecompositionFactoryBase):

    ##
    # @brief construct
    # @param strategy TDlib's strategy (see help page of TDlib)
    # @param tmpfile file for tdlib's output
    # @todo automatically generate unique / thread-safe tmp name
    def __init__(self, strategy=2, tmpfile=None):
        self.strategy = strategy
        self.tmpfile = tmpfile

    ##
    # @brief Make tree decomposition using TDlib
    # @return tree decomposition (object of TreeDecomp)
    def create(self, size, dependencies):
        bindependencies = self.expand_to_cliques(dependencies)

        if self.tmpfile is None:
            fh,tmpfile = tempfile.mkstemp()
            os.close(fh)
        else:
            tmpfile = self.tmpfile

        makeTDFile_TDlib(tmpfile, size, bindependencies, strategy=self.strategy)
        tdfile = tmpfile + ".td"
        with open(tdfile) as tdfh:
            td = parseTD_TDlib(tdfh, size)
        os.remove(tdfile)
        os.remove(tmpfile)
        return td

def _bagweights(bags, weights):
    return [prod(weights[i] for i in bag) for bag in bags]


class NXTreeDecompositionFactory(TreeDecompositionFactoryBase):
    """Tree decomposition factory using min fill in heuristic from networkx

    Supports optimization over randomized runs of the heuristic
    """

    def __init__(
        self,
        *,
        maxdiffsize=1,
        iterations=20,
        adaptive=1.8,
        objective=None,
        weights=None,
        join=None,
        verbose=False,
    ):
        """
        Init tree decomposition factory

        Args:
            maxdiffsize: tree decomposition is expanded to ensure a maximum size of diff sets
            iterations:  minimum number of iterations for opimization
            adaptive:    perform at least adaptive**w iterations at tree width w (turn off with None or 0)
            objective:   minimize objective; objetive is a function on width, bags, edges of a td
            weights:     weights of the variables, used in weighting objetive functions [experimental]
            join:        function indicating if nodes i,j, i<j, shall be joined; joined nodes are collapsed
                for the tree decomposer and then expanded again; this could
                help to find better decompositions for certain models with
                non-uniform domain size and make complexity analysis simpler, but typically fails [experimental]
            verbose:     potentially print some information

        """

        self._maxdiffsize = maxdiffsize
        self._iterations = iterations
        self._adaptive = adaptive if adaptive is not None else 0
        self._weights = weights
        self._join = join

        objectives = {
            "width": lambda width, bags, edges: width,
            "weight": lambda width, bags, edges: sum(_bagweights(bags, self._weights)),
            "maxweight": lambda width, bags, edges: max(
                _bagweights(bags, self._weights)
            ),
        }

        self._objective = objective

        if type(objective) == str:
            try:
                self._objective = objectives[self._objective]
            except KeyError:
                raise KeyError(
                    f"Undefined objective function {self._objective} for tree decomposition. "
                    f"Available predefined objectives: {objectives.keys()}."
                )

    def create(self, size, dependencies):
        """Create tree decomposition

        Iteratively applies tree decomposition heuristics to randomized graphs;
        returns best tree decomposition.
        """
        # produce networkx graph from size, dependencies

        # import networkx here, so we depend on networkx only if it is used
        # for tree decomposition (and not some other tree decomposer)
        from networkx import Graph
        from networkx.algorithms.approximation import treewidth

        dg_edges = self.expand_to_cliques(dependencies)

        cnodes, cedges, collapse_info = self._collapse(size, dg_edges)

        best_value = None
        best_width = None

        k = 0
        while best_width is None or k < max(
            self._iterations, self._adaptive**best_width
        ):
            scnodes, scedges, shuffle_info = self._shuffle(cnodes, cedges)

            # construct a networkx graph as shuffled, compacted
            # dependency graph
            G = Graph()
            G.add_nodes_from(scnodes)
            G.add_edges_from(scedges)

            # apply min fill in heuristic; compute a tree decomposition
            width, tree = treewidth.treewidth_min_fill_in(G)

            # keep best tree decomposition
            if self._objective is None:
                value = width
            else:
                cbags, edges = self._unshuffle_tree(tree, shuffle_info)
                bags = self._uncollapse_bags(cbags, collapse_info)
                value = self._objective(width, bags, edges)

            if best_width is None or width < best_width:
                best_width = width

            if best_value is None or value < best_value:
                best_value, best_tree = value, tree
                best_shuffle_info = shuffle_info
            k += 1

        cbags, edges = self._unshuffle_tree(best_tree, best_shuffle_info)
        bags = self._uncollapse_bags(cbags, collapse_info)
        td = TreeDecomposition(bags, edges)
        td.expand_treedecomposition(self._maxdiffsize)

        return td

    def _collapse(self, size, edges):
        # compute transitive closure of self._join
        # i.e. compute dictionary such that merged[j]=i means
        # that j is merged to i
        nodes = list(range(size))

        merged = {i: i for i in nodes}
        if self._join is not None:
            for i in range(size):
                for j in range(i + 1, size):
                    if self._join(i, j):
                        merged[j] = merged[i]
        else:
            return nodes, edges, None

        cedges = [(merged[i], merged[j]) for (i, j) in edges]
        # orient and unique
        cedges = [tuple(sorted(edge)) for edge in cedges]
        cedges = list(set(cedges))
        cnodes = [x for x in nodes if merged[x] == x]

        from collections import defaultdict

        inv_merged = defaultdict(list)
        for k, v in merged.items():
            inv_merged[v].append(k)

        return cnodes, cedges, inv_merged

    @staticmethod
    def _uncollapse_bags(cbags, collapse_info):
        if collapse_info is None:
            return cbags

        inv_merged = collapse_info

        bags = [sum((inv_merged[x] for x in bag), []) for bag in cbags]

        return bags

    @staticmethod
    def _shuffle(nodes, edges):
        perm = list(nodes)
        _MyRandom.shuffle(perm)
        perm = {i: j for i, j in zip(list(nodes), perm)}
        shuffle_info = {j: i for i, j in perm.items()}
        edges = [[perm[x] for x in edge] for edge in edges]
        nodes = [perm[x] for x in nodes]
        return nodes, edges, shuffle_info

    @staticmethod
    def _unshuffle_tree(tree, shuffle_info):
        inv_perm = shuffle_info
        # convert data strucutures of tree nodes and edges
        bags = list(map(list, tree.nodes))
        edges = [(bags.index(list(i)), bags.index(list(j))) for i, j in tree.edges]
        # revert the shuffling of the dependency graph nodes in all bags
        bags = [[inv_perm[x] for x in bag] for bag in bags]
        return bags, edges


# @brief default tree decomposition factory
TreeDecompositionFactory = NXTreeDecompositionFactory


# @brief the available, predefined td factories with some description
_td_factories = [
    ["nx", "using networkx module", NXTreeDecompositionFactory],
    [
        "tdlib",
        "using TDlib, strategy 2",
        lambda: TDLibTreeDecompositionFactory(strategy=2),
    ],
    ["htd", "using libhtd", HTDTreeDecompositionFactory],
]


# @brief get a tree decomposition factory by a descriptor string
def td_factory_from_descriptor(descriptor):
    for x in _td_factories:
        if descriptor == x[0]:
            return x[2]()
    return None


def get_td_factory_descriptors():
    return [x[0] for x in _td_factories]


# End of Interface tree demposition libraries
# ----------------------------------------------------------


if __name__ == "__main__":
    pass
