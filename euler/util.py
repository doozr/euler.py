def ptab(xss):
    for xs in [list(xs) for xs in xss]:
        print "\t".join(str(x) for x in xs)
