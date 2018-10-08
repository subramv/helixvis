import helixvis

helixvis.draw_wheel("LTTGLPALISWIKRKRQQ", showplot = True)
fig, ax = helixvis.draw_wheel("DTTGLPALISWIKRKRQQ")
fig.savefig("testwheel.png")

helixvis.draw_wenxiang("LTTGLPALISWIKRKRQQ", showplot = True)
fig, ax = helixvis.draw_wenxiang("DTTGLPALISWIKRKRQQ")
fig.savefig("testwheel.png")
