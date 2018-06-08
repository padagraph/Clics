# -*- encoding: utf-8 -*-
import igraph
import sys
import codecs

NODES_HEADERS = ["@Concept: #id", "key", "label", "concept", "body_part", "frequency"]

EDGES_HEADERS = ["_Edge:", "languages", "families", "weight", "width"]



if __name__ == "__main__":
    input_file = "/home/pierre/Téléchargements/clics.gml" #  sys.argv[1]
    nodes_file = "./nodes.csv" #  sys.argv[2]
    edges_file = "./edges.csv" #  sys.argv[3]
    g = igraph.load(input_file)
    with codecs.open(nodes_file, "w", "utf-8") as f:
        f.write(", ".join(NODES_HEADERS))
        f.write("\n")
        for v in g.vs():
            v['id'] = int(v['id'])
            line =  [str(v[x]).replace(",","/") for x in  ["id"] + NODES_HEADERS[1:]]
            f.write(", ".join(line))
            f.write("\n")
    with codecs.open(edges_file, "w", "utf-8") as f:
        f.write("& https://raw.githubusercontent.com/padagraph/Clics/master/nodes.csv\n")
        f.write(", ".join(EDGES_HEADERS))
        f.write("\n")
        for e in g.es():
            src = str(g.vs[e.source]['id'])
            tgt = str(g.vs[e.target]['id'])
            e['width'] = int(e['weight'])
            line = src + " -- " + tgt + ", " + (", ".join([str(e[x]) for x in EDGES_HEADERS[1:]])) + "\n"
            f.write(line)

