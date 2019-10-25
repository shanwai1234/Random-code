from ete2 import Tree, TreeStyle, faces, AttrFace, TreeStyle, NodeStyle
#import sys
#mycgi = sys.argv[1]
#cgi = open(mycgi,'r')
#def layout(node):
#    if node.is_leaf():
#        N = AttrFace("name", fsize=30)
#        faces.add_face_to_node(N, node, 0, position="aligned")

#def get_example_tree():

    # Set dashed blue lines in all leaves
#nst1 = NodeStyle()
#nst1["bgcolor"] = "LightSteelBlue"
#nst2 = NodeStyle()
#nst2["bgcolor"] = "Moccasin"
#nst3 = NodeStyle()
#nst3["bgcolor"] = "DarkSeaGreen"
#nst4 = NodeStyle()
#nst4["bgcolor"] = "Khaki"

fh = open("/home/zliang/Documents/projects in James lab/calling SNP through RNA-seq data/30datav3_final.cgi.txt")
tlist = []
for x in fh:
	y = x.strip()
	tlist.append(y)
tstring = ''.join(tlist)

t = Tree(tstring)
#t = Tree("((((((((((((USA_MO_Givan:0.014012,(USA_NE_Schnable:0.004868,""(DEU_Bonn_Hochholdinger:0.000001,DEU_Cologne_Urbany:0.000001)0.000000:0.001763)""0.698000:0.005346)0.595000:0.006464,USA_IA_Schnable:0.000001)0.600000:0.006405,""(USA_FL_Kang:0.004029,USA_CA_Hake:0.000001)0.776000:0.018913)0.169000:0.004251,""(USA_AR_Grene:0.023224,((USA_MO_Brutnell:0.001414,CHN_Beijing_Deng:0.000001)""0.000000:0.000001,B73_ref:0.000001)0.893000:0.005364)0.936000:0.011380)""0.917000:0.009713,USA_WI_Doebley:0.061547)0.913000:0.020112,""(USA_NY_Ware:0.000001,(USA_NY_Eveland:0.000002,USA_IA_Becraft:0.017388)""0.107000:0.006859)0.837000:0.003822)0.793000:0.008552,(USA_NE_Zhang:0.009512,""((USA_NY_Scanlon:0.574641,USA_NY_Frank:0.000001)0.826000:0.004183,""USA_DE_Li:0.000001)0.945000:0.007740)1.000000:0.041025)1.000000:0.357856,""USA_MI_Buell:0.002442)0.581000:0.000968,USA_MN_Springer:0.000001)""1.000000:0.861620,CHN_Beijing_Xie:0.002607)0.000000:0.000323,""CHN_Beijing_Wang:0.005840)0.599000:0.001943,CHN_Beijing_Chen:0.001930,""CHN_Beijing_Lai:0.000001);")
#node1 = t.get_common_ancestor("CHN_Beijing_Xie","CHN_Beijing_Wang","CHN_Beijing_Chen","CHN_Beijing_Lai")
#t.set_outgroup(node1)
#    for n in t.traverse():
#            n.dist = 0

ancestor = t.get_common_ancestor("USA_MI_Buell","USA_MN_Springer")
t.set_outgroup(ancestor)
#print ancestor

#node1.set_outgroup("USA_MI_Buell")
#R = t.get_midpoint_outgroup()
ts = TreeStyle()
#    ts.layout_fn = layout
ts.show_leaf_name = True
#ts.show_branch_length = True
ts.show_branch_support = True
ts.scale = 100
#    ts.mode = "c"
#    ts.root_opening_factor = 1
#    return t, ts

#if __name__ == "__main__":
#    t, ts = get_example_tree()
    #t.render("node_background.png", w=400, tree_style=ts)
t.show(tree_style=ts)


#cgi.close()
