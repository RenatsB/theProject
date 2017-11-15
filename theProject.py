import prman

ri = prman.Ri()

filename = "theProject.rib"
ri.Begin(filename)

ri.Display("theProject.tiff", "it", "rgb")
ri.Format(1920,1080,1)
ri.Projection("perspective", {"fov":[45]})
ri.Integrator('PxrPathTracer', 'Integrator')
ri.DepthOfField(36,0.1,3)

def MetalTop() :
	points=[-0.5,0.2,1.5,
	0.5,0.2,1.5,
	0.5,0.2,-1.5,
	0.25,0.2,-1.42,
	0,0.2,-1.385,
	-0.25,0.2,-1.42,
	-0.5,0.2,-1.5]
	ri.GeneralPolygon ([len(points)/3], {ri.P:points})

def MetalSide(signF) :
	val=signF*0.5
	points=[val,-0.2,1.5,
	val,0.2,1.5,
	val,0.2,-1.5,
	val,0.075,-2,
	val,0,-2.5,
	val,-0.2,-2.5,
	val,-0.2,1.5]
	ri.GeneralPolygon ([len(points)/3], {ri.P:points})

def MetalBottom() :
	points=[-0.5,-0.2,1.5,
	0.5,-0.2,1.5,
	0.5,-0.2,-2.5,
	0.4,-0.2,-2.5,
	0.36,-0.2,-2.34,
	0.28,-0.2,-2.22,
	0.16,-0.2,-2.14,
	0,-0.2,-2.1,
	-0.16,-0.2,-2.14,
	-0.28,-0.2,-2.22,
	-0.36,-0.2,-2.34,
	-0.4,-0.2,-2.5,
	-0.5,-0.2,-2.5,
	-0.5,-0.2,1.5]
	ri.GeneralPolygon ([len(points)/3], {ri.P:points})

def MetalRingHoriz(signF) :
	val=signF*0.2
	points=[0.5,val,-2.5,
	0.4,val,-2.5,
	0.36,val,-2.66,
	0.28,val,-2.78,
	0.16,val,-2.86,
	0,val,-2.9,
	-0.16,val,-2.86,
	-0.28,val,-2.78,
	-0.36,val,-2.66,
	-0.4,val,-2.5,
	-0.5,val,-2.5,
	-0.45,val,-2.7,
	-0.35,val,-2.85,
	-0.2,val,-2.95,
	0,val,-3,
	0.2,val,-2.95,
	0.35,val,-2.85,
	0.45,val,-2.7]
	ri.GeneralPolygon ([len(points)/3], {ri.P:points})

def MetalRingSideOuter() :
	signA = 0.0
	signB = -0.2
	points1a=[-0.5,signA,-2.5,
	-0.45,signA,-2.7,
	-0.45,signB,-2.7,
	-0.5,signB,-2.5]
	points2a=[-0.45,signA,-2.7,
	-0.35,signA,-2.85,	
	-0.35,signB,-2.85,
	-0.45,signB,-2.7]
	points3a=[-0.35,signA,-2.85,
	-0.2,signA,-2.95,
	-0.2,signB,-2.95,
	-0.35,signB,-2.85]
	points4a=[-0.2,signA,-2.95,
	0,signA,-3,
	0,signB,-3,
	-0.2,signB,-2.95]
	#end of left side
	signA = -0.2
	signB = 0.0
	points1b=[0.5,signA,-2.5,
	0.45,signA,-2.7,
	0.45,signB,-2.7,
	0.5,signB,-2.5]
	points2b=[0.45,signA,-2.7,
	0.35,signA,-2.85,	
	0.35,signB,-2.85,
	0.45,signB,-2.7]
	points3b=[0.35,signA,-2.85,
	0.2,signA,-2.95,
	0.2,signB,-2.95,
	0.35,signB,-2.85]
	points4b=[0.2,signA,-2.95,
	0,signA,-3,
	0,signB,-3,
	0.2,signB,-2.95]
	#end of right side
	ri.GeneralPolygon ([len(points1a)/3], {ri.P:points1a})
	ri.GeneralPolygon ([len(points2a)/3], {ri.P:points2a})
	ri.GeneralPolygon ([len(points3a)/3], {ri.P:points3a})
	ri.GeneralPolygon ([len(points4a)/3], {ri.P:points4a})
	ri.GeneralPolygon ([len(points1b)/3], {ri.P:points1b})
	ri.GeneralPolygon ([len(points2b)/3], {ri.P:points2b})
	ri.GeneralPolygon ([len(points3b)/3], {ri.P:points3b})
	ri.GeneralPolygon ([len(points4b)/3], {ri.P:points4b})

def MetalCurvedTop1() :
	points=[0.5,0.2,-1.5,
	0.25,0.2,-1.42,
	0,0.2,-1.385,
	-0.25,0.2,-1.42,
	-0.5,0.2,-1.5,
	-0.5,0.075,-2,
	-0.25,0.075,-1.92,
	0,0.075,-1.885,
	0.25,0.075,-1.92,
	0.5,0.075,-2]
	ri.GeneralPolygon ([len(points)/3], {ri.P:points})

def MetalCurvedTop2() :
	points=[-0.5,0.075,-2,
	-0.25,0.075,-1.92,
	0,0.075,-1.885,
	0.25,0.075,-1.92,
	0.5,0.075,-2,
	0.5,0,-2.5,
	0.4,0,-2.5,
	0.36,0,-2.34,
	0.28,0,-2.22,
	0.16,0,-2.14,
	0,0,-2.1,
	-0.16,0,-2.14,
	-0.28,0,-2.22,
	-0.36,0,-2.34,
	-0.4,0,-2.5,
	-0.5,0,-2.5]
	ri.GeneralPolygon ([len(points)/3], {ri.P:points})

def MetalCurvedTop2Test() :
	points1=[-0.5,0.075,-2,
	-0.25,0.075,-1.92,
	0,0.075,-1.885,
	0,0,-2.1,
	-0.16,0,-2.14,
	-0.28,0,-2.22,
	-0.36,0,-2.34,
	-0.4,0,-2.5,
	-0.5,0,-2.5]
	points2=[0.5,0.075,-2,
	0.25,0.075,-1.92,
	0,0.075,-1.885,
	0,0,-2.1,
	0.16,0,-2.14,
	0.28,0,-2.22,
	0.36,0,-2.34,
	0.4,0,-2.5,
	0.5,0,-2.5]
	ri.GeneralPolygon ([len(points1)/3], {ri.P:points1})
	ri.GeneralPolygon ([len(points2)/3], {ri.P:points2})

def MetalPart(posX, posY, posZ) :
	ri.TransformBegin()
	ri.Translate(posX,posY,posZ)
	ri.AttributeBegin()

	ri.Bxdf("PxrDisney", "metal",
    {		
            "color baseColor":[0.25,0.25,0.25],
            "float metallic":[1],
            "float specular":[1],
            "float anisotropic":[0.5],
            "float clearcoat":[0.95]
    }
    )

	MetalTop()
	MetalSide(1.0)
	MetalSide(-1)
	MetalBottom()
	MetalRingHoriz(-1.0)
	MetalRingHoriz(0)
	MetalRingSideOuter()
	MetalCurvedTop1()
	MetalCurvedTop2Test()
	ri.TransformBegin()
	ri.Rotate(90,1,0,0)
	ri.Translate(0,-2.5,0)
	ri.Cylinder(0.4,0,0.2,360.0)
	ri.TransformEnd()
	ri.AttributeEnd()
	ri.TransformEnd()
	

def Table(posX, posY, posZ, rotX, rotY, rotZ, sc) :
    ri.Bxdf("PxrDisney", "table",
    {		
            "color baseColor":[1,1,1],
            "float metallic":[0.8],
            "float specular":[1],
            "float anisotropic":[0.5],
            "float clearcoat":[0.95]
    }
    )
    ri.TransformBegin()
    ri.Translate(posX,posY,posZ)
    ri.Rotate(rotX,1,0,0)
    ri.Rotate(rotY,0,1,0)
    ri.Rotate(rotZ,0,0,1)
    ri.Scale(sc,sc,sc)
    ri.Patch("bilinear",{"P":[5,0,-5,5,0,5,-5,0,-5,-5,0,5]})
    ri.TransformEnd()
#endTable

ri.WorldBegin()
#All the geometry goes here vvv
vertAngle = -25
ri.Translate(0,0,7)
ri.AttributeBegin()
ri.Rotate(-90+vertAngle,1,0,0)
ri.Rotate(5,1,0,0)
ri.Rotate(90,0,0,1)
ri.Light("PxrDomeLight", "holyLight",
{
"float exposure":[0],
"string lightColorMap":["hdrTex.tx"]
}
)
ri.AttributeEnd()

ri.Rotate(vertAngle,1,0,0)
ri.Rotate(-135,0,1,0)
ri.TransformBegin()
ri.Translate(0,-1,0)
MetalPart(0,0,0)
ri.TransformEnd()
Table(0,-1.19,-1,0,45,0,3)

#All the geometry goes here ^^^
ri.WorldEnd()
ri.End()