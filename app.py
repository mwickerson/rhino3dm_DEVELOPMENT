"""Hops flask middleware example"""
from flask import Flask
import ghhops_server as hs
import rhino3dm


# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)


# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"

# hs.HopsNumber(name="Angle", nickname="Ang", description="Angle"),
# hs.HopsInteger(name="Grid", nickname="G", description="Grid size"),
# hs.HopsBoolean(name="Adaptive", nickname="Ad", description="Adaptive meshing"),
# hs.HopsString(name="String", nickname="S", description="String to mesh"),

# hs.HopsVector(name="Vector", nickname="V", description="Vector to mesh")
# hs.HopsPoint(name="Point", nickname="P", description="Point to mesh"),
# hs.HopsLine(name="Line", nickname="L", description="Line to mesh"),
# hs.HopsCurve(name="Curve", nickname="C", description="Curve to mesh"),

# hs.HopsSurface(name="Surface", nickname="S", description="Surface to mesh"),
# hs.HopsBrep(name="Brep", nickname="B", description="Brep to mesh"),
# hs.HopsMesh(name="Mesh", nickname="M", description="Mesh to mesh"),
# hs.HopsSubD(name="SubD", nickname="SD", description="SubD to mesh"),

# hs.HopsParamAccess(name="Param", nickname="Pa", description="Parametric access"),
# hs.HopsDefault(name="Density", nickname="D", description="Density"),
# hs.HopsFlask(name="Flask", nickname="F", description="Flask to mesh"),
# hs._HopsEncoder(name="Encoder", nickname="En", description="Encoder to mesh")



@hops.component(
    "/pointat",
    name="PointAt",
    nickname="PtAt",
    description="Get point along curve",
    icon="pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate")
    ],
    outputs=[hs.HopsPoint("P", "P", "Point on curve at t")]
)
def pointat(curve: rhino3dm.Curve, t=0.0):
    return curve.PointAt(t)


@hops.component(
    "/srf4pt",
    name="4Point Surface",
    nickname="Srf4Pt",
    description="Create ruled surface from four points",
    inputs=[
        hs.HopsPoint("Corner A", "A", "First corner"),
        hs.HopsPoint("Corner B", "B", "Second corner"),
        hs.HopsPoint("Corner C", "C", "Third corner"),
        hs.HopsPoint("Corner D", "D", "Fourth corner")
    ],
    outputs=[hs.HopsSurface("Surface", "S", "Resulting surface")]
)
def ruled_surface(a: rhino3dm.Point3d,
                  b: rhino3dm.Point3d,
                  c: rhino3dm.Point3d,
                  d: rhino3dm.Point3d):
    edge1 = rhino3dm.LineCurve(a, b)
    edge2 = rhino3dm.LineCurve(c, d)
    return rhino3dm.NurbsSurface.CreateRuledSurface(edge1, edge2)

# param containers in grasshopper 
# are represented as lists in python
@hops.component(
    "/createpoint",
    name="Create Point",
    nickname="Pt",
    description="Create point",
    inputs=[
        hs.HopsNumber("X", "X", "X coordinate of point"),
        hs.HopsNumber("Y", "Y", "Y coordinate of point"),
        hs.HopsNumber("Z", "Z", "Z coordinate of point")
    ],
    outputs=[hs.HopsPoint("Point", "P", "Resulting point")]
)
def create_point(x=0.0, y=0.0, z=0.0):
    return rhino3dm.Point3d(x, y, z)


@hops.component(
    "/createCurve",
    name="Create Curve",
    nickname="Crv",
    description="Create curve",
    inputs=[
        hs.HopsPoint("Start", "S", "Start point of curve"),
        hs.HopsPoint("End", "E", "End point of curve")
    ],
    outputs=[hs.HopsCurve("Curve", "C", "Resulting curve")]
)
def create_curve(start: rhino3dm.Point3d, end: rhino3dm.Point3d):
    return rhino3dm.LineCurve(start, end)  

@hops.component(
    "/createSurface",
    name="Create Surface",
    nickname="Srf",
    description="Create surface",
    inputs=[
        hs.HopsPoint("Corner A", "A", "First corner"),
        hs.HopsPoint("Corner B", "B", "Second corner"),
        hs.HopsPoint("Corner C", "C", "Third corner"),
        hs.HopsPoint("Corner D", "D", "Fourth corner")
    ],
    outputs=[hs.HopsSurface("Surface", "S", "Resulting surface")]
)
def create_surface(a: rhino3dm.Point3d,
                     b: rhino3dm.Point3d,
                     c: rhino3dm.Point3d,
                     d: rhino3dm.Point3d):
     edge1 = rhino3dm.LineCurve(a, b)
     edge2 = rhino3dm.LineCurve(c, d)
     return rhino3dm.NurbsSurface.CreateRuledSurface(edge1, edge2)

@hops.component(
    "/createBrep",
    name="Create Brep",
    nickname="Brep",
    description="Create brep",
    inputs=[
        hs.HopsSurface("Surface", "S", "Surface to create brep from")
    ],
    outputs=[hs.HopsBrep("Brep", "B", "Resulting brep")]
)
def create_brep(surface: rhino3dm.NurbsSurface):
    return rhino3dm.Brep.CreateFromSurface(surface)


# create hops line
@hops.component(
    "/createLine",
    name="Create Line",
    nickname="Ln",
    description="Create line",
    inputs=[
        hs.HopsPoint("Start", "S", "Start point of line"),
        hs.HopsPoint("End", "E", "End point of line")
    ],
    outputs=[hs.HopsLine("Line", "L", "Resulting line")]
)
def create_line(start: rhino3dm.Point3d, end: rhino3dm.Point3d):
    return rhino3dm.LineCurve(start, end)



# create hops vector
@hops.component(
    "/createVector",
    name="Create Vector",
    nickname="Vec",
    description="Create vector",
    inputs=[
        hs.HopsNumber("X", "X", "X coordinate of vector"),
        hs.HopsNumber("Y", "Y", "Y coordinate of vector"),
        hs.HopsNumber("Z", "Z", "Z coordinate of vector")
    ],
    outputs=[hs.HopsVector("Vector", "V", "Resulting vector")]
)
def create_vector(x: float, y: float, z: float):
    return rhino3dm.Vector3d(x, y, z)

# create hops mesh
# create hops subd

"""
 ██████╗██╗   ██╗██████╗ ██╗   ██╗███████╗███████╗
██╔════╝██║   ██║██╔══██╗██║   ██║██╔════╝██╔════╝
██║     ██║   ██║██████╔╝██║   ██║█████╗  ███████╗
██║     ██║   ██║██╔══██╗╚██╗ ██╔╝██╔══╝  ╚════██║
╚██████╗╚██████╔╝██║  ██║ ╚████╔╝ ███████╗███████║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝
                                                  
"""

"""curve domain
Domain
rhino3dm.Interval: Gets or sets the domain of the curve.
"""
@hops.component(
    "/crvDomainT0T1",
    name="Curve Domain",
    nickname="CrvDom",
    description="Curve domain",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get domain from")
    ],
    outputs=[hs.HopsNumber("T0", "T0", "T0 of domain"), hs.HopsNumber("T1", "T1", "T1 of domain")]
)
def crv_domain(curve: rhino3dm.Curve):
    return curve.Domain.T0, curve.Domain.T1

"""
curve dimension
Dimension
int: Gets the dimension of the object. 
The dimension is typically three. 
For parameter space trimming curves the dimension is two. 
In rare cases the dimension can be one or greater than three.
"""
@hops.component(
    "/crvDimension",
    name="Curve Dimension",
    nickname="CrvDim",
    description="Curve dimension",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get dimension from")
    ],
    outputs=[hs.HopsNumber("Dimension", "D", "Dimension of curve")]
)
def crv_dimension(curve: rhino3dm.Curve):
    return curve.Dimension

"""
curve span count
SpanCount
int: Gets the number of non-empty smooth (c-infinity) spans in the curve.
"""
@hops.component(
    "/crvSpanCount",
    name="Curve Span Count",
    nickname="CrvSpan",
    description="Curve span count",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get span count from")
    ],
    outputs=[hs.HopsNumber("SpanCount", "Span", "Span count of curve")]
)
def crv_span_count(curve: rhino3dm.Curve):
    return curve.SpanCount

"""
curve degree
Degree
int: Gets the maximum algebraic degree 
of any span or a good estimate if 
curve spans are not algebraic.
"""
@hops.component(
    "/crvDegree",
    name="Curve Degree",
    nickname="CrvDeg",
    description="Curve degree",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get degree from")
    ],
    outputs=[hs.HopsNumber("Degree", "Deg", "Degree of curve")]
)
def crv_degree(curve: rhino3dm.Curve):
    return curve.Degree

"""
curve IsClosed
IsClosed
bool: Gets a value indicating whether 
or not this curve is a closed curve.
"""
@hops.component(
    "/crvIsClosed",
    name="Curve Is Closed",
    nickname="CrvClosed",
    description="Curve is closed",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get is closed from")
    ],
    outputs=[hs.HopsBoolean("IsClosed", "Closed", "Is curve closed")]
)
def crv_is_closed(curve: rhino3dm.Curve):
    return curve.IsClosed

"""
curve IsPeriodic
IsPeriodic
bool: Gets a value indicating whether 
or not this curve is considered to be Periodic.
"""
@hops.component(
    "/crvIsPeriodic",
    name="Curve Is Periodic",
    nickname="CrvPeriodic",
    description="Curve is periodic",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get is periodic from")
    ],
    outputs=[hs.HopsBoolean("IsPeriodic", "Periodic", "Is curve periodic")]
)
def crv_is_periodic(curve: rhino3dm.Curve):
    return curve.IsPeriodic

"""
curve PointAtStart
PointAtStart
rhino3dm.Point3d: 
Evaluates point at the start of the curve.
"""
@hops.component(
    "/crvPointAtStart",
    name="Curve Point At Start",
    nickname="CrvStart",
    description="Curve point at start",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get point at start from")
    ],
    outputs=[hs.HopsPoint("PointAtStart", "P", "Point at start of curve")]
)
def crv_point_at_start(curve: rhino3dm.Curve):
    return curve.PointAtStart

"""
curve PointAtEnd
PointAtEnd
rhino3dm.Point3d:
Evaluates point at the end of the curve.
"""
@hops.component(
    "/crvPointAtEnd",
    name="Curve Point At End",
    nickname="CrvEnd",
    description="Curve point at end",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get point at end from")
    ],
    outputs=[hs.HopsPoint("PointAtEnd", "P", "Point at end of curve")]
)
def crv_point_at_end(curve: rhino3dm.Curve):
    return curve.PointAtEnd

"""
curve TangentAtStart
TangentAtStart
rhino3dm.Vector3d: Evaluates the unit 
tangent vector at the start of the curve.
"""
@hops.component(
    "/crvTangentAtStart",
    name="Curve Tangent At Start",
    nickname="CrvStartTang",
    description="Curve tangent at start", 
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get tangent at start from")
    ],
    outputs=[hs.HopsVector("TangentAtStart", "T", "Tangent at start of curve")]
)   
def crv_tangent_at_start(curve: rhino3dm.Curve):
    return curve.TangentAtStart

"""
curve TangentAtEnd
TangentAtEnd
rhino3dm.Vector3d: Evaluates the unit
tangent vector at the end of the curve.
"""
@hops.component(
    "/crvTangentAtEnd",
    name="Curve Tangent At End",
    nickname="CrvEndTang",
    description="Curve tangent at end",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to get tangent at end from")
    ],
    outputs=[hs.HopsVector("TangentAtEnd", "T", "Tangent at end of curve")]
)   
def crv_tangent_at_end(curve: rhino3dm.Curve):
    return curve.TangentAtEnd

"""
static Create Control Point Curve
staticCreateControlPointCurve(points, degree)
Constructs a curve from a set of control-point locations.

Parameters:	
points (list[rhino3dm.Point3d]) – Control points.
degree (int) – Degree of curve. The number of control points must be at least degree+1.
Return type:	
rhino3dm.Curve
"""
@hops.component(
    "/crvCP5",
    name="Create Control Point Curve",
    nickname="CrvCreateCP",
    description="Create control point curve",
    inputs=[
        hs.HopsPoint("Points", "P", "Control points", access=hs.HopsParamAccess.LIST),
        hs.HopsInteger("Degree", "D", "Degree of curve")
    ],
    outputs=[hs.HopsCurve("Curve", "C", "Curve")]
)
def crvCP5(points, degree):
    return rhino3dm.Curve.CreateControlPointCurve(points, degree)






if __name__ == "__main__":
    app.run(debug=True)
