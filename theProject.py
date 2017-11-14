import prman

ri = prman.Ri()

filename = "theProject.rib"
ri.Begin(filename)

ri.Display("theProject", "it", "rgb")
ri.Format(720,512,1)
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
	points=[-0.5,0,-2.5,
	-0.45,0,-2.7,
	-0.35,0,-2.85,
	-0.2,0,-2.95,
	0,0,-3,
	0.2,0,-2.95,
	0.35,0,-2.85,
	0.45,0,-2.7,
	0.5,0,-2.5,
	
	0.5,-0.2,-2.5,
	0.45,-0.2,-2.7,
	0.35,-0.2,-2.85,
	0.2,-0.2,-2.95,
	0,-0.2,-3,
	-0.2,-0.2,-2.95,
	-0.35,-0.2,-2.85,
	-0.45,-0.2,-2.7,
	-0.5,-0.2,-2.5,
	-0.5,0,-2.5]
	ri.GeneralPolygon ([len(points)/3], {ri.P:points})

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
	ri.AttributeEnd()
	ri.AttributeBegin()

	MetalCurvedTop1()
	MetalCurvedTop2()
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

ri.Translate(0,0,7)
ri.AttributeBegin()
ri.Rotate(-90,1,0,0)
ri.Light("PxrDomeLight", "holyLight",
{
"float exposure":[0],
"string lightColorMap":["hdrTex.tx"]
}
)
ri.AttributeEnd()

ri.Rotate(-45,1,0,0)
ri.Rotate(60,0,1,0)
MetalPart(0,0,0)

Table(0,-1.19,0,0,0,0,3)

#All the geometry goes here ^^^
ri.WorldEnd()
ri.End()