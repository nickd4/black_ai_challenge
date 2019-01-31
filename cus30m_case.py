from __future__ import division # allows floating point division from integers
import FreeCAD, FreeCADGui, Part 
from FreeCAD import Base
import math

#App.getDocument("Unnamed").removeObject("Shape")

xs = 130 #83 # x size, box length
ys = 68 #54 # y size, box width
zs = 44 #31 # z size, box height
xt = 15 # tab x size, protrusion length
yt = 7.5 # tab y size, chamfer
hd = 6 # hole distance from edge of box
hr = 1.5 # hole radius
pr = 2.5 # post radius
gr = 3.5 # post guide radius
wt = 1.5 # wall thickness
xe = 50 # x explode distance
ze = 50 # z explode distance
vs = zs/4 # vent spacing
vr = 2 # vent radius
vx = vs # lower left vent hole x
vz = ze+vs # lower left vent hole z

face = Part.Face(
  Part.Wire(
    [
      Part.makeLine((-xs/2, ys/2, 0), (xs/2, ys/2, 0)), 
      Part.makeLine((xs/2, ys/2, 0), (xs/2+xt, ys/2-yt, 0)), 
      Part.makeLine((xs/2+xt, ys/2-yt, 0), (xs/2+xt,-ys/2+yt, 0)), 
      Part.makeLine((xs/2+xt, -ys/2+yt, 0), (xs/2,-ys/2, 0)), 
      Part.makeLine((xs/2, -ys/2, 0), (-xs/2, -ys/2, 0)), 
      Part.makeLine((-xs/2, -ys/2, 0), (-xs/2-xt, -ys/2+yt, 0)), 
      Part.makeLine((-xs/2-xt, -ys/2+yt, 0), (-xs/2-xt, ys/2-yt, 0)), 
      Part.makeLine((-xs/2-xt, ys/2-yt, 0), (-xs/2, ys/2, 0))
    ]
  )
)
for x, y in [
  (-xs/2+hd, ys/2-hd),
  (xs/2-hd, ys/2-hd),
  (xs/2+xt-hd, ys/2-yt-hd),
  (xs/2+xt-hd, -ys/2+yt+hd),
  (xs/2-hd, -ys/2+hd),
  (-xs/2+hd, -ys/2+hd),
  (-xs/2-xt+hd, -ys/2+yt+hd),
  (-xs/2-xt+hd, ys/2-yt-hd)
]:
  face = face.cut(
    Part.Face(
      Part.Wire(
        Part.makeCircle(hr, Base.Vector(x, y, 0))
      )
    )
  )
base = face.extrude(Base.Vector(0, 0, wt))
for x, y in [
  (-xs/2+hd, ys/2-hd),
  (xs/2-hd, ys/2-hd),
  (xs/2-hd, -ys/2+hd),
  (-xs/2+hd, -ys/2+hd),
]:
  base = base.fuse(
    Part.Face(
      Part.Wire(
        Part.makeCircle(gr, Base.Vector(x, y, wt))
      )
    ).cut(
      Part.Face(
        Part.Wire(
          Part.makeCircle(pr, Base.Vector(x, y, wt))
        )
      )
    ).extrude(Base.Vector(0, 0, wt))
  )
Part.show(base, 'Base')

lid = Part.makeBox(xs, ys, zs-wt, Base.Vector(-xs/2, -ys/2, ze+wt)).cut(
  Part.makeBox(xs-wt*2, ys-wt*2, zs-wt*2, Base.Vector(-xs/2+wt, -ys/2+wt, ze+wt))
).cut(
  Part.makeBox(wt, 7, 7.5, Base.Vector(-xs/2, -3.5, ze+wt))
).cut(
  Part.makeBox(wt, 18.5, 15, Base.Vector(xs/2-wt, -9.25, ze+wt))
)
for x, y in [
  (-xs/2+hd, ys/2-hd),
  (xs/2-hd, ys/2-hd),
  (xs/2-hd, -ys/2+hd),
  (-xs/2+hd, -ys/2+hd),
]:
  lid = lid.fuse(
    Part.Face(
      Part.Wire(
        Part.makeCircle(pr, Base.Vector(x, y, ze+wt*2))
      )
    ).cut(
      Part.Face(
        Part.Wire(
          Part.makeCircle(hr, Base.Vector(x, y, ze+wt*2))
        )
      )
    ).extrude(Base.Vector(0, 0, zs-wt*3))
  )
for x, z in [
  (vx, vz),
  (vx+vs, vz),
  (vx+vs*2, vz),
  (vx, vz+vs),
  (vx+vs, vz+vs),
  (vx+vs*2, vz+vs),
  (vx, vz+vs*2),
  (vx+vs, vz+vs*2),
  (vx+vs*2, vz+vs*2)
]:
  lid = lid.cut(
    Part.makeCylinder(vr, ys, Base.Vector(x, -ys/2, z), Base.Vector(0, 1, 0))
  )
Part.show(lid, 'Lid')

dc = Part.makeCylinder(2.5, 25, Base.Vector(-xe-xs/2+5, 0, ze+wt+5), Base.Vector(-1, 0, 0)).fuse(
  Part.makeCylinder(3, 2.5, Base.Vector(-xe-xs/2-15, 0, ze+wt+5), Base.Vector(-1, 0, 0))
).fuse(
  Part.makeCylinder(3.5, 2.5, Base.Vector(-xe-xs/2-10, 0, ze+wt+5), Base.Vector(-1, 0, 0))
).fuse(
  Part.makeCylinder(4, 2.5, Base.Vector(-xe-xs/2-5, 0, ze+wt+5), Base.Vector(-1, 0, 0))
).fuse(
  Part.makeCylinder(5, 2.5, Base.Vector(-xe-xs/2, 0, ze+wt+5), Base.Vector(-1, 0, 0))
).fuse(
  Part.makeBox(2.5, 7, 5, Base.Vector(-xe-xs/2, -3.5, ze+wt+2.5))
).fuse(
  Part.makeBox(2.5, 10, 10, Base.Vector(-xe-xs/2+2.5, -10/2, ze+wt))
).fuse(
  Part.makeCylinder(1, 45, Base.Vector(-xe-xs/2+15, -1, ze+wt+5), Base.Vector(-1, 0, 0))
).fuse(
  Part.makeCylinder(1, 45, Base.Vector(-xe-xs/2+15, 1, ze+wt+5), Base.Vector(-1, 0, 0))
)
Part.show(dc, 'DC')

ac = Part.makeBox(14.5, 18.5, 13.4, Base.Vector(xe+xs/2-12.5, -9.25, ze+wt+1.6)).fuse(
  Part.makeBox(1.5, 22, 13.4, Base.Vector(xe+xs/2-2.7, -11, ze+wt+1.6))
).fuse(
  Part.makeBox(2, 22, 15, Base.Vector(xe+xs/2, -11, ze+wt))
).fuse(
  Part.makeCylinder(1.5, 3, Base.Vector(xe+xs/2-5.35, -6.5, ze+wt+15))
).fuse(
  Part.makeCylinder(1.5, 3, Base.Vector(xe+xs/2-5.35, 6.5, ze+wt+15))
).fuse(
  Part.makeCylinder(0.6, 3.2, Base.Vector(xe+xs/2-5.35-6.55, 2.65-9, ze+wt+15))
).fuse(
  Part.makeCylinder(0.6, 3.2, Base.Vector(xe+xs/2-5.35-6.55, 2.65, ze+wt+15))
).cut(
  Part.makeCylinder(4.1, 11, Base.Vector(xe+xs/2-9, -4.3, ze+wt+7.5), Base.Vector(1, 0, 0))
).cut(
  Part.makeCylinder(4.1, 11, Base.Vector(xe+xs/2-9, 4.3, ze+wt+7.5), Base.Vector(1, 0, 0))
).cut(
  Part.makeBox(11, 2, 4.2, Base.Vector(xe+xs/2-9, -1, ze+wt+7.5-2.1))
).fuse(
  Part.makeCylinder(1.18, 11, Base.Vector(xe+xs/2-9, -4.3, ze+wt+7.5), Base.Vector(1, 0, 0))
).fuse(
  Part.makeCylinder(1.18, 11, Base.Vector(xe+xs/2-9, 4.3, ze+wt+7.5), Base.Vector(1, 0, 0))
)
Part.show(ac, 'AC')