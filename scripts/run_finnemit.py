import finnemit
import sys
import getopt

optlist, args = getopt.getopt(sys.argv[1:], 'mf')


assume_majority_lct_input = True
for o, a in optlist:
    # TODO these options should be mutex, but i let it go for now
    # i do better if we really need this to be option in released version
    if o == '-f':
        assume_majority_lct_input = False
    elif o == '-m':
        assume_majority_lct_input = True
    else:
        assert False, 'unhandled option'

fname = args[0]
dct = finnemit.get_emissions(fname, assume_majority_lct_input=assume_majority_lct_input)
print()
for k,v in dct.items():
    print(', '.join([str(_) for _ in (k,v)]))

