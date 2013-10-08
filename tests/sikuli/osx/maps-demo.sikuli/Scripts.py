def resizeApp(app, dx, dy):
2        switchApp(app)
3        corner = find(Pattern().targetOffset(3,14))
4
5        drop_point = corner.getTarget().offset(dx, dy)
6        dragDrop(corner, drop_point)
7
8resizeApp("Safari", 50, 50)