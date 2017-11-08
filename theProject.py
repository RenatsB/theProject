import prman

ri = prman.Ri()

filename = "theProject.rib"
ri.Begin(filename)

ri.Display("theProject", "it", "rgb")
ri.Format(720,512,1)
ri.Projection("perspective", {"fov":[45]})
ri.Integrator('PxrPathTracer', 'Integrator')
ri.DepthOfField(36,0.1,3)

def MetalPart(posX, posY, posZ) :
	points=[
	-0.5,0.2,1.5,
	-0.25,0.2,1.5,
	0.0,0.2,1.5,
	0.25,0.2,1.5,
	0.5,0.2,1.5,
	0.5,0.2,-1.5,
	0.25,0.2,-1.15,
	0,0.2,-1,
	-0.25,0.2,-1.15
	-0.5,0.2,-1.5
	]
	#ri.Basis(ri.BezierBasis,3,ri.BezierBasis,3)
	ri.GeneralPolygon ([len(points)/3], {ri.P:points})
	#ri.PatchMesh("bicubic",3,"nonperiodic",3,"nonperiodic", {ri.P: points})
	#ri.NuPatch(9,[0,0,0,1,1,2,2,3,3,4,4,4],0,4,
         #2,[0,0,1,1],0,1,
        #{"Pw":[1,0,0,1,1,1,0,1,0,2,0,2,
		#-1,1,0,1,-1,0,0,1,-1,-1,0,1,
		#0,-2,0,2,1,-1,0,1,1,0,0,1,
		#1,0,-3,1,1,1,-3,1,0,2,-6,2,
		#-1,1,-3,1,-1,0,-3,1,-1,-1,-3,1,
		#0,-2,-6,2,1,-1,-3,1,1,0,-3,1]})
	

def Table(posX, posY, posZ, rotX, rotY, rotZ, sc) :
    ri.Bxdf("PxrDisney", "table",
    {		
            "color baseColor":[0,0,0],
            "float metallic":[1],
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

ri.Translate(0,0,5.75)
ri.AttributeBegin()
ri.Rotate(90,1,0,0)
ri.Light("PxrDomeLight", "holyLight",
{
"float exposure":[0],
"string lightColorMap":["hdrTest.tx"]
}
)
ri.AttributeEnd()

ri.Rotate(-15,1,0,0)

MetalPart(0,0,0)

Table(0,-1.19,0,0,0,0,3)

#All the geometry goes here ^^^
ri.WorldEnd()
ri.End()