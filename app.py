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

"""
curve Change Dimension
ChangeDimension(desiredDimension)
Changes the dimension of a curve.

Parameters:	desiredDimension (int) – The desired dimension.
Returns:	True if the curve’s dimension was already desired
Dimension or if the curve’s dimension was successfully 
changed to desiredDimension; otherwise false.
Return type:	bool
"""
@hops.component(
    "/crvChangeDimension",
    name="Change Dimension",
    nickname="CrvChangeDim",
    description="Change dimension of curve",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to change dimension of"),
        hs.HopsInteger("DesiredDimension", "D", "Desired dimension")
    ],
    outputs=[hs.HopsBoolean("Changed", "Ch", "Changed")]
)
def crv_change_dimension(curve: rhino3dm.Curve, desiredDimension):
    return curve.ChangeDimension(desiredDimension)

"""
curve IsLinear
IsLinear(tolerance)
Test a curve to see if it is linear 
to within RhinoMath.ZeroTolerance units (1e-12).

Returns:	True if the curve is linear.
Return type:	bool
"""
@hops.component(
    "/crvIsLinear",
    name="Is Linear",
    nickname="CrvLinear",
    description="Curve is linear",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to test")
    ],
    outputs=[hs.HopsBoolean("IsLinear", "Lin", "Is linear")]
)
def crv_is_linear(curve: rhino3dm.Curve):
    return curve.IsLinear()

"""
curve is polyline
IsPolyline()
Several types of Curve can have the form of a polyline including a degree 1 NurbsCurve, a PolylineCurve, and a PolyCurve all of whose segments are some form of polyline. IsPolyline tests a curve to see if it can be represented as a polyline.

Returns:	True if this curve can be represented as a polyline; otherwise, false.
Return type:	bool
"""
@hops.component(
    "/crvIsPolyline",
    name="Is Polyline",
    nickname="CrvPolyline",
    description="Curve is polyline",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to test")
    ],
    outputs=[hs.HopsBoolean("IsPolyline", "Poly", "Is polyline")]
)
def crv_is_polyline(curve: rhino3dm.Curve):
    return curve.IsPolyline()

"""curve try get polyline
TryGetPolyline()
Several types of Curve can have the form of a 
polyline including a degree 1 NurbsCurve, 
a PolylineCurve, and a PolyCurve all of 
whose segments are some form of polyline. 
IsPolyline tests a curve to see if it can be represented as a polyline.

Returns:	tuple (bool, rhino3dm.Polyline)
True if this curve can be represented as a polyline; otherwise, false.
If True is returned, then the polyline form is returned here.
Return type:	(bool, rhino3dm.Polyline)
"""
# @hops.component(
#     "/crvTryGetPolyline",
#     name="Try Get Polyline",
#     nickname="CrvTryPoly",
#     description="Try get polyline",
#     inputs=[
#         hs.HopsCurve("Curve", "C", "Curve to test")
#     ],
#     outputs=[hs.HopsLine("Polyline", "Poly", "Polyline")]
# )
# def crv_try_get_polyline(curve: rhino3dm.Curve):
#     polyline = rhino3dm.Polyline()
#     if curve.TryGetPolyline(polyline):
#         return polyline
#     else:
#         return None


"""
curve is arc
IsArc(tolerance)
Test a curve to see if it can be represented 
by an arc or circle within RhinoMath.ZeroTolerance.

Returns:	True if the curve can 
be represented by an arc or a circle within tolerance.
Return type:	bool
"""
@hops.component(
    "/crvIsArc",
    name="Is Arc",
    nickname="CrvArc",
    description="Curve is arc",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to test")
    ],
    outputs=[hs.HopsBoolean("IsArc", "Arc", "Is arc")]
)
def crv_is_arc(curve: rhino3dm.Curve):
    return curve.IsArc()

# curve try get arc

"""
curve is circle
IsCircle(tolerance)
Test a curve to see if it can be represented 
by a circle within RhinoMath.ZeroTolerance.

Returns:	True if the Curve can be 
represented by a circle within tolerance.
Return type:	bool
"""
@hops.component(
    "/crvIsCircle",
    name="Is Circle",
    nickname="CrvCircle",
    description="Curve is circle",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to test")
    ],
    outputs=[hs.HopsBoolean("IsCircle", "Circ", "Is circle")]
)
def crv_is_circle(curve: rhino3dm.Curve):
    return curve.IsCircle()

# curve try get circle

"""
curve is ellipse
IsEllipse(tolerance)
Test a curve to see if it can be represented 
by an ellipse within RhinoMath.ZeroTolerance.

Returns:	True if the Curve can be 
represented by an ellipse within tolerance.
Return type:	bool
"""
@hops.component(
    "/crvIsEllipse",
    name="Is Ellipse",
    nickname="CrvEllipse",
    description="Curve is ellipse",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to test")
    ],
    outputs=[hs.HopsBoolean("IsEllipse", "Ell", "Is ellipse")]
)
def crv_is_ellipse(curve: rhino3dm.Curve):
    return curve.IsEllipse()

# curve try get ellipse

"""
curve is planar
IsPlanar(tolerance)
Test a curve for planarity.

Returns:	True if the curve is planar (flat) 
to within RhinoMath.ZeroTolerance units (1e-12).
Return type:	bool
"""
@hops.component(
    "/crvIsPlanar",
    name="Is Planar",
    nickname="CrvPlanar",
    description="Curve is planar",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to test")
    ],
    outputs=[hs.HopsBoolean("IsPlanar", "Plan", "Is planar")]
)
def crv_is_planar(curve: rhino3dm.Curve):
    return curve.IsPlanar()

"""
curve change closed seam
ChangeClosedCurveSeam(t)
If this curve is closed, then modify it 
so that the start/end point is at 
curve parameter t.

Parameters:	t (float) – Curve parameter 
of new start/end point. The returned 
curves domain will start at t.
Returns:	True on success, False on failure.
Return type:	bool
"""
@hops.component(
    "/crvChangeClosedCurveSeam",
    name="Change Closed Curve Seam",
    nickname="CrvChangeClosedCurveSeam",
    description="Change closed curve seam",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to change seam of"),
        hs.HopsNumber("Parameter", "T", "Parameter of new start/end point")
    ],
    outputs=[hs.HopsBoolean("Changed", "Ch", "Changed")]
)
def crv_change_closed_curve_seam(curve: rhino3dm.Curve, parameter):
    return curve.ChangeClosedCurveSeam(parameter)

"""
curve is closable
IsClosable(tolerance, minimumAbsoluteSize, 
minimumRelativeSize)
Decide if it makes sense to close off 
this curve by moving the endpoint to the 
start based on start-end gap size and 
length of curve as approximated by 
chord defined by 6 points.

Returns:	True if start and end points 
are close enough based on above conditions.
Return type:	bool
"""
@hops.component(
    "/crvIsClose",
    name="Is Closable",
    nickname="CrvClosable",
    description="Curve is closable",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to test"),
        hs.HopsNumber("Tolerance", "T", "Tolerance"),
        hs.HopsNumber("MinimumAbsoluteSize", "MA", "Minimum absolute size"),
        hs.HopsNumber("MinimumRelativeSize", "MR", "Minimum relative size")
    ],
    outputs=[hs.HopsBoolean("IsClosable", "Clos", "Is closable")]
)
def crv_is_close(curve: rhino3dm.Curve, tolerance, minimum_absolute_size, minimum_relative_size):
    return curve.IsClosable(tolerance, minimum_absolute_size, minimum_relative_size)

"""
curve reverse
Reverse()
Reverses the direction of the curve.

Returns:	True on success, False on failure.
Return type:	bool
"""
@hops.component(
    "/crvReverse",
    name="Reverse",
    nickname="CrvReverse",
    description="Curve reverse",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to reverse")
    ],
    outputs=[hs.HopsBoolean("Reversed", "Rev", "Reversed")]
)
def crv_reverse(curve: rhino3dm.Curve):
    return curve.Reverse()

"""
curve close curve orientation
ClosedCurveOrientation()
Determines the orientation (counterclockwise or clockwise) 
of a closed, planar curve in the world XY plane. 
Only works with simple (no self intersections) closed, planar curves.

Returns:	The orientation of this curve with respect to world XY plane.
Return type:	CurveOrientation
"""
@hops.component(
    "/crvClosedCurveOrientation",
    name="Closed Curve Orientation",
    nickname="CrvClosedCurveOrientation",
    description="Curve close curve orientation",
    inputs=[    
        hs.HopsCurve("Curve", "C", "Curve to test")
    ],
    # bugging out with hs.HopsEnum
    outputs=[hs.HopsInteger("Orientation", "O", "Orientation", ["Clockwise", "Counterclockwise"])]
)
def crv_closed_curve_orientation(curve: rhino3dm.Curve):
    return curve.ClosedCurveOrientation()

"""
curve point at parameter
PointAt(t)
Evaluates point at a curve parameter.

Parameters:	t (float) – Evaluation parameter.
Returns:	Point (location of curve at the parameter t).
Return type:	rhino3dm.Point3d
"""
@hops.component(
    "/crvPointAt",
    name="Point At",
    nickname="CrvPointAt",
    description="Curve point at parameter",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("Parameter", "T", "Parameter to evaluate")
    ],
    outputs=[hs.HopsPoint("Point", "P", "Point")]
)
def crv_point_at(curve: rhino3dm.Curve, parameter):
    return curve.PointAt(parameter)

"""
curve set start point
SetStartPoint(point)
Forces the curve to start at a specified point. Not all curve types support this operation.

Parameters:	point (rhino3dm.Point3d) – New start point of curve.
Returns:	True on success, False on failure.
Return type:	bool
"""
@hops.component(
    "/crvSetStartPoint",
    name="Set Start Point",
    nickname="CrvSetStartPoint",
    description="Curve set start point",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to set start point of"),
        hs.HopsPoint("Point", "P", "Point to set start point of")
    ],
    outputs=[hs.HopsBoolean("Set", "Set", "Set")]
)
def crv_set_start_point(curve: rhino3dm.Curve, point: rhino3dm.Point3d):
    return curve.SetStartPoint(point)

"""
curve set end point
SetEndPoint(point)
Forces the curve to end at a specified point. Not all curve types support this operation.

Parameters:	point (rhino3dm.Point3d) – New end point of curve.
Returns:	True on success, False on failure.
Return type:	bool
"""
@hops.component(
    "/crvSetEndPoint",
    name="Set End Point",
    nickname="CrvSetEndPoint",
    description="Curve set end point",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to set end point of"),
        hs.HopsPoint("Point", "P", "Point to set end point of")
    ],
    outputs=[hs.HopsBoolean("Set", "Set", "Set")]
)
def crv_set_end_point(curve: rhino3dm.Curve, point: rhino3dm.Point3d):
    return curve.SetEndPoint(point)

""".
TangentAt(t)
Evaluates the unit tangent vector at a curve parameter.

Parameters:	t (float) – Evaluation parameter.
Returns:	Unit tangent vector of the curve at the parameter t.
Return type:	rhino3dm.Vector3d
"""
@hops.component(
    "/crvTangentAt",
    name="Tangent At",
    nickname="CrvTangentAt",
    description="Curve tangent at parameter",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("Parameter", "T", "Parameter to evaluate")
    ],
    outputs=[hs.HopsVector("Tangent", "T", "Tangent")]
)
def crv_tangent_at(curve: rhino3dm.Curve, parameter):
    return curve.TangentAt(parameter)

"""
CurvatureAt(t)
Evaluate the curvature vector at a curve parameter.

Parameters:	t (float) – Evaluation parameter.
Returns:	Curvature vector of the curve at the parameter t.
Return type:	rhino3dm.Vector3d
"""
@hops.component(
    "/crvCurvatureAt",
    name="Curvature At",
    nickname="CrvCurvatureAt",
    description="Curve curvature at parameter",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("Parameter", "T", "Parameter to evaluate")
    ],
    outputs=[hs.HopsVector("Curvature", "C", "Curvature")]
)
def crv_curvature_at(curve: rhino3dm.Curve, parameter):
    return curve.CurvatureAt(parameter)

"""
curve frame at parameter
FrameAt(t)
Returns a 3d frame at a parameter.

Parameters:	t (float) – Evaluation parameter.
Returns:	tuple (bool, rhino3dm.Plane)
True on success, False on failure.
The frame is returned here.
Return type:	(bool, rhino3dm.Plane)
"""
@hops.component(
    "/crvFrameAt",
    name="Frame At",
    nickname="CrvFrameAt",
    description="Curve frame at parameter",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("Parameter", "T", "Parameter to evaluate")
    ],
    # need to output an origin point and vectors for creating a plane in the UI
    outputs=[
        hs.HopsBoolean("Success", "Success", "Success"), 
        hs.HopsPoint("Origin", "O", "Origin"),
        hs.HopsVector("X", "X", "X"),
        hs.HopsVector("Y", "Y", "Y"),
        hs.HopsVector("Z", "Z", "Z")
    ]
)
def crv_frame_at(curve: rhino3dm.Curve, parameter):
    success, frame = curve.FrameAt(parameter)
    return success, frame.Origin, frame.XAxis, frame.YAxis, frame.ZAxis

"""
curve get curve parameter form nurbs from parameter
GetCurveParameterFromNurbsFormParameter(nurbsParameter)
Convert a NURBS curve parameter to a curve parameter.

Parameters:	nurbsParameter (float) – NURBS form parameter.
Returns:	tuple (bool, float)
True on success, False on failure.
Curve parameter.
Return type:	(bool, float)
"""
@hops.component(
    "/crvGetCurveParameterFromNurbsFormParameter",
    name="Get Curve Parameter From Nurbs Form Parameter",
    nickname="CrvGetCurveParameterFromNurbsFormParameter",
    description="Curve get curve parameter from nurbs form parameter",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("NurbsFormParameter", "N", "Nurbs form parameter to evaluate")
    ],
    outputs=[
            hs.HopsBoolean("Success", "Success", "Success"), 
            hs.HopsNumber("CurveParameter", "P", "Curve parameter")]
)
def crv_get_curve_parameter_from_nurbs_form_parameter(curve: rhino3dm.Curve, nurbs_form_parameter):
    success, curve_parameter = curve.GetCurveParameterFromNurbsFormParameter(nurbs_form_parameter)
    return success, curve_parameter

"""
curve get nurbs form parameter from curve parameter
GetNurbsFormParameterFromCurveParameter(curveParameter)
Convert a curve parameter to a NURBS curve parameter.

Parameters:	curveParameter (float) – Curve parameter.
Returns:	tuple (bool, float)
True on success, False on failure.
NURBS form parameter.
Return type:	(bool, float)
"""
@hops.component(
    "/crvGetNurbsFormParameterFromCurveParameter",
    name="Get Nurbs Form Parameter From Curve Parameter",
    nickname="CrvGetNurbsFormParameterFromCurveParameter",
    description="Curve get nurbs form parameter from curve parameter",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("CurveParameter", "P", "Curve parameter to evaluate")
    ],
    outputs=[
            hs.HopsBoolean("Success", "Success", "Success"), 
            hs.HopsNumber("NurbsFormParameter", "N", "Nurbs form parameter")]
)
def crv_get_nurbs_form_parameter_from_curve_parameter(curve: rhino3dm.Curve, curve_parameter):
    success, nurbs_form_parameter = curve.GetNurbsFormParameterFromCurveParameter(curve_parameter)
    return success, nurbs_form_parameter

"""
curve trim(t0, t1)
Trim(t0, t1)
Removes portions of the curve outside the specified interval.

Parameters:	
t0 (float) – Start of the trimming interval. Portions of the curve before curve(t0) are removed.
t1 (float) – End of the trimming interval. Portions of the curve after curve(t1) are removed.
Returns:	
Trimmed portion of this curve is successful, None on failure.

Return type:	
rhino3dm.Curve
"""
@hops.component(
    "/crvTrim",
    name="Trim",
    nickname="CrvTrim",
    description="Curve trim",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("Start", "S", "Start of the trimming interval"),
        hs.HopsNumber("End", "E", "End of the trimming interval")
    ],
    outputs=[hs.HopsCurve("Trimmed", "T", "Trimmed curve")]
)
def crv_trim(curve: rhino3dm.Curve, start, end):
    return curve.Trim(start, end)

"""
curve split(t)
Split(t)
Splits (divides) the curve at the specified parameter. 
The parameter must be in the interior of the curve’s domain.

Parameters:	t (float) – Parameter to split 
the curve at in the interval returned by Domain().
Returns:	Two curves on success, None on failure.
Return type:	rhino3dm.Curve[]
"""
@hops.component(
    "/crvSplit",
    name="Split",
    nickname="CrvSplit",
    description="Curve split",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("Parameter", "T", "Parameter to split the curve at in the interval returned by Domain()")
    ],
    outputs=[hs.HopsCurve("First", "F", "First curve"), hs.HopsCurve("Second", "S", "Second curve")]
)
def crv_split(curve: rhino3dm.Curve, parameter):
    return curve.Split(parameter)

"""
curve to nurbs curve
ToNurbsCurve()
Constructs a NURBS curve representation of this curve.

Returns:	NURBS representation of the curve on success, None on failure.
Return type:	rhino3dm.NurbsCurve
"""
@hops.component(
    "/crvToNurbsCurve",
    name="To Nurbs Curve",
    nickname="CrvToNurbsCurve",
    description="Curve to nurbs curve",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate")
    ],
    outputs=[hs.HopsCurve("Nurbs", "N", "Nurbs curve")]
)
def crv_to_nurbs_curve(curve: rhino3dm.Curve):
    return curve.ToNurbsCurve()

"""
curve to nurbs (subdomain) curve
ToNurbsCurve(subdomain)
Constructs a NURBS curve representation of this curve.

Returns:	NURBS representation of the curve on success, None on failure.
Return type:	rhino3dm.NurbsCurve
"""
@hops.component(
    "/crvToNurbsCurveSudDomain",
    name="To Nurbs Curve (Subdomain)",
    nickname="CrvToNurbsCurve(sudDomain)",
    description="Curve to nurbs (subdomain) curve",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("Subdomain", "S", "Subdomain")
    ],
    outputs=[hs.HopsCurve("Nurbs", "N", "Nurbs curve")]
)
def crv_to_nurbs_curve_Subdomain(curve: rhino3dm.Curve, subdomain):
    return curve.ToNurbsCurve(subdomain)

















if __name__ == "__main__":
    app.run(debug=True)
