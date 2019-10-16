from goatools.obo_parser import GODag
go_obo_file_path = ''
go_term_name = GO:0015979"
godag = GODag(obo_file=go_obo_file)
mygo = godag.query_term(go_term_name)
print go_term_name + " Parents"
print mygo.get_all_parents()
print go_term_name + " Children"
print mygo.get_all_children() 
