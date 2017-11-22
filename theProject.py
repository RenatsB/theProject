import prman

ri = prman.Ri()

filename = "theProject.rib"
ri.Begin(filename)

ri.Display("theProject.tiff", "it", "rgb")
ri.Format(720,480,1)
ri.Projection("perspective", {"fov":[45]})
ri.Integrator('PxrPathTracer', 'Integrator')
ri.DepthOfField(36,0.1,3)

#variables used to position vertices
#hX - half width
hX = 0.6
#hY - half height
hY = 0.225
#hZ - half length
hZ = 2.25
#cB - beginning of the curved slope(top left or right end)
cB = 0.38
#rT - ring thickness
rT = 0.1
#rB - beginning of the ring (side)
rB = 1.75-rT
#rEp - ring end plus
rEp = (2*rB-hZ+rT)
#rEm - ring end minus
rEm = hZ-rT
#rR - ring radius
rR = hX-rT
#inner ring values
ringA=rR*(11.0/30.0)
ringB=rR*(21.0/30.0)
ringC=rR*(28.0/30.0)
#outer ring values
ringAo=hX*(11.0/30.0)
ringBo=hX*(21.0/30.0)
ringCo=hX*(28.0/30.0)
#hPart - height partitioning value
hPart = 2.25
#metal thickness at the front
metalThickness=0.045
#width and height of inner geometry 
hXt=hX-metalThickness
hYt=hY-metalThickness

def MetalTop() :
	points=[-hX,hY,hZ,
	hX,hY,hZ,
	hX,hY,-cB,
	hX/2,hY,-(cB-0.085),
	0,hY,-(cB-0.125),
	-hX/2,hY,-(cB-0.085),
	-hX,hY,-cB]
	ri.GeneralPolygon ([len(points)/3], {ri.P:points})

def MetalSide(signF) :
	val=signF*hX
	points=[val,-hY,hZ,
	val,hY,hZ,
	val,hY,-cB,
	val,hY/hPart,-(cB+0.5),
	val,0,-rB,
	val,-hY,-rB,
	val,-hY,hZ]
	ri.GeneralPolygon ([len(points)/3], {ri.P:points})

def MetalBottom() :
	points=[-hX,-hY,hZ,
	hX,-hY,hZ,
	hX,-hY,-rB,
	rR,-hY,-rB,
	ringC,-hY,-(rB-ringA),
	ringB,-hY,-(rB-ringB),
	ringA,-hY,-(rB-ringC),
	0,-hY,-rEp,
	-ringA,-hY,-(rB-ringC),
	-ringB,-hY,-(rB-ringB),
	-ringC,-hY,-(rB-ringA),
	-rR,-hY,-rB,
	-hX,-hY,-rB,
	-hX,-hY,hZ]
	ri.GeneralPolygon ([len(points)/3], {ri.P:points})

def MetalRingHoriz(signF) :
	val=signF*hY
	points=[hX,val,-rB,
	rR,val,-rB,
	ringC,val,-(rB+ringA),
	ringB,val,-(rB+ringB),
	ringA,val,-(rB+ringC),
	0,val,-rEm,
	-ringA,val,-(rB+ringC),
	-ringB,val,-(rB+ringB),
	-ringC,val,-(rB+ringA),
	-rR,val,-rB,
	-hX,val,-rB,
	-ringCo,val,-(rB+ringAo),
	-ringBo,val,-(rB+ringBo),
	-ringAo,val,-(rB+ringCo),
	0,val,-hZ,
	ringAo,val,-(rB+ringCo),
	ringBo,val,-(rB+ringBo),
	ringCo,val,-(rB+ringAo)]
	ri.GeneralPolygon ([len(points)/3], {ri.P:points})

def MetalRingSideOuter() :
	signA = 0.0
	signB = -hY
	rAo = (rB+ringAo)
	rBo = (rB+ringBo)
	rCo = (rB+ringCo)
	points1a=[-hX,signA,-rB,
	-ringCo,signA,-rAo,
	-ringCo,signB,-rAo,
	-hX,signB,-rB]
	points2a=[-ringCo,signA,-rAo,
	-ringBo,signA,-rBo,	
	-ringBo,signB,-rBo,
	-ringCo,signB,-rAo]
	points3a=[-ringBo,signA,-rBo,
	-ringAo,signA,-rCo,
	-ringAo,signB,-rCo,
	-ringBo,signB,-rBo]
	points4a=[-ringAo,signA,-rCo,
	0,signA,-hZ,
	0,signB,-hZ,
	-ringAo,signB,-rCo]
	#end of left side
	signA = -hY
	signB = 0.0
	points1b=[hX,signA,-rB,
	ringCo,signA,-rAo,
	ringCo,signB,-rAo,
	hX,signB,-rB]
	points2b=[ringCo,signA,-rAo,
	ringBo,signA,-rBo,	
	ringBo,signB,-rBo,
	ringCo,signB,-rAo]
	points3b=[ringBo,signA,-rBo,
	ringAo,signA,-rCo,
	ringAo,signB,-rCo,
	ringBo,signB,-rBo]
	points4b=[ringAo,signA,-rCo,
	0,signA,-hZ,
	0,signB,-hZ,
	ringAo,signB,-rCo]
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
	points=[hX,hY,-cB,
	hX/2,hY,-(cB-0.085),
	0,hY,-(cB-0.125),
	-hX/2,hY,-(cB-0.085),
	-hX,hY,-cB,
	-hX,hY/hPart,-(cB+0.5),
	-hX/2,hY/hPart-0.01,-(cB+0.48),
	0,hY/hPart-0.0125,-(cB+0.42),
	hX/2,hY/hPart-0.01,-(cB+0.48),
	hX,hY/hPart,-(cB+0.5)]
	ri.GeneralPolygon ([len(points)/3], {ri.P:points})

def MetalCurvedTop2() :
	points=[-hX,hY/hPart,-(cB+0.5),
	-hX/2,hY/hPart-0.01,-(cB+0.48),
	0,hY/hPart-0.0125,-(cB+0.42),
	hX/2,hY/hPart-0.01,-(cB+0.48),
	hX,hY/hPart,-(cB+0.5),
	hX,0,-rB,
	rR,0,-rB,
	ringC,0,-(rB-ringA),
	ringB,0,-(rB-ringB),
	ringA,0,-(rB-ringC),
	0,0,-rEp,
	-ringA,0,-(rB-ringC),
	-ringB,0,-(rB-ringB),
	-ringC,0,-(rB-ringA),
	-rR,0,-rB,
	-hX,0,-rB]
	ri.GeneralPolygon ([len(points)/3], {ri.P:points})

def MetalFront() :
	points=[hX,hY,hZ,
	-hX,hY,hZ,
	-hX,-hY,hZ,
	hX,-hY,hZ,
	
	hXt,hYt,hZ,
	-hXt,hYt,hZ,
	-hXt,-hYt,hZ,
	hXt,-hYt,hZ]
	ri.GeneralPolygon ([4,4],{ri.P:points})

def MetalInside(a,b) :
	points1=[a,b,hZ,
	a,b,1,
	-a,b,1,
	-a,b,hZ]
	points2=[a,b,hZ,
	a,b,1,
	a,-b,1,
	a,-b,hZ]
	points3=[-a,b,hZ,
	-a,b,1,
	-a,-b,1,
	-a,-b,hZ]
	points4=[-a,-b,hZ,
	a,-b,hZ,
	a,-b,1,
	-a,b,1]
	ri.GeneralPolygon ([len(points1)/3], {ri.P:points1})
	ri.GeneralPolygon ([len(points2)/3], {ri.P:points2})
	ri.GeneralPolygon ([len(points3)/3], {ri.P:points3})
	ri.GeneralPolygon ([len(points4)/3], {ri.P:points4})

def MetalPart(posX, posY, posZ) :
	ri.TransformBegin()
	ri.Translate(posX,posY,posZ)
	ri.AttributeBegin()
	ri.Pattern("scratchSh","scratchTx",{"float Cina":[1], "float Cinb":[0], "float scale":[1], "float freq":[2], "float variation":[0.2]})
	ri.Pattern("scratchSh","scratchTxFlipped",{"float Cina":[0], "float Cinb":[1], "float scale":[1], "float freq":[2], "float variation":[0.2]})
	ri.Pattern("stripes", "strTx")
	ri.Displace("PxrDisplace","metalDisp",
	{"float dispAmount":[0.1],
	"reference float dispScalar":["strTx:Cout"]})
	ri.Bxdf("PxrDisney", "metal",
    {		
            "reference color baseColor":["strTx:Cout"],
            "float metallic":[1],
            "reference float specular":["strTx:Cout"],
            "reference float anisotropic":["strTx:Cout"],
            "reference float clearcoat":["strTx:Cout"]
    }
    )

	MetalTop()
	MetalSide(1.0)
	MetalSide(-1.0)
	MetalBottom()
	MetalRingHoriz(-1.0)
	MetalRingSideOuter()
	ri.TransformBegin()
	ri.Rotate(90,1,0,0)
	ri.Translate(0,-rB,0)
	ri.Cylinder(rR,0,hY,360.0)
	ri.TransformEnd()
	MetalFront()
	MetalInside(hXt,hYt)
	MetalRingHoriz(0)
	MetalCurvedTop1()
	MetalCurvedTop2()
	ri.AttributeEnd()

	#ri.AttributeBegin()
	#ri.Attribute("displacementbound",{"sphere":[0.4],"coordinatesystem":["shader"]})
	#ri.Pattern("noiseSh","noiseTx",{"float frequency":[26], "float mag":[2]})
	#ri.Displace("PxrDisplace","metalDisp",
	#{"float dispAmount":[0.9],
	#"reference float dispScalar":["noiseTx:mag"]})
	#ri.Bxdf("PxrDisney","curvedTop",{"color baseColor":[0.5,0.5,0.5],"float metallic":[0.95]})

	
	#ri.AttributeEnd()
	ri.TransformEnd()
	
def PlasticBrick(xmin,ymin,zmin,xmax,ymax,zmax,col) :
	ri.AttributeBegin()
	ri.Bxdf("PxrDisney", "table",
    {		
            "color baseColor":[0,0,col],
            "float metallic":[0.9],
            "float specular":[0.9],
            "float anisotropic":[0.1],
            "float clearcoat":[0.5]
    }
    )
	front=[xmin,ymin,zmax,
	xmin,ymax,zmax,
	xmax,ymax,zmax,
	xmax,ymin,zmax]
	sideL=[xmin,ymin,zmax,
	xmin,ymax,zmax,
	xmin,ymax,zmin,
	xmin,ymin,zmin]
	sideR=[xmax,ymin,zmax,
	xmax,ymax,zmax,
	xmax,ymax,zmin,
	xmax,ymin,zmin]
	top=[xmin,ymax,zmax,
	xmin,ymax,zmin,
	xmax,ymax,zmin,
	xmax,ymax,zmax]
	ri.GeneralPolygon ([len(front)/3], {ri.P:front})
	ri.GeneralPolygon ([len(sideL)/3], {ri.P:sideL})
	ri.GeneralPolygon ([len(sideR)/3], {ri.P:sideR})
	ri.GeneralPolygon ([len(top)/3], {ri.P:top})
	ri.AttributeEnd()

def MetalContact(posx, posy, posz) :
	ri.TransformBegin()
	ri.Translate(posx,posy,posz)
	points=[-0.025,0,hZ,
	-0.025,0,1,
	0.025,0,1,
	0.025,0,hZ]
	ri.GeneralPolygon ([len(points)/3], {ri.P:points})
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
vertAngle = -12.5
horizAngle = -135
#ri.Translate(0,0,9)
ri.Translate(0,0,4)
ri.AttributeBegin()
ri.Rotate(-95+vertAngle,1,0,0)
ri.Rotate(5,1,0,0)
ri.Rotate(70+horizAngle,0,0,1)
ri.Light("PxrDomeLight", "holyLight",
{
"float exposure":[1],
"string lightColorMap":["hdrTex.tx"]
}
)
ri.AttributeEnd()

ri.Rotate(vertAngle,1,0,0)
ri.Rotate(horizAngle,0,1,0)
ri.TransformBegin()
ri.Translate(0,-1,0)
MetalPart(0,0,0)
ri.AttributeBegin()
ri.Bxdf("PxrDisney", "contact",
    {		
            "color baseColor":[1,1,0],
            "float metallic":[1],
            "float specular":[1],
            "float anisotropic":[0.05],
            "float clearcoat":[0.05]
    }
    )
MetalContact(-0.35,(-hYt)+0.185,-0.03)
MetalContact(0.35,(-hYt)+0.185,-0.03)
ri.AttributeEnd()
PlasticBrick(-hXt,-hYt,1,hXt,(-hYt)+0.14,hZ-0.005,0)
PlasticBrick(-(hXt-0.055),(-hYt)+0.14,1,(hXt-0.055),(-hYt)+0.18,hZ-0.005,1)
ri.TransformEnd()

Table(0,-1.19,-2,0,45,0,3)

#All the geometry goes here ^^^
ri.WorldEnd()
ri.End()