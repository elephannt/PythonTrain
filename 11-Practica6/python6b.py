import cProfile, pstats, StringIO
pr = cProfile.Profile()
pr.enable()
pr.disable()
s=StringIO.StringIO()
sortby = 'cumulative'
ps=pstats.Stats(pr,stream=s).sort_stats(sortby)
ps.print_stats()
print s.getvalue()