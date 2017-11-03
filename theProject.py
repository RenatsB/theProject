import prman

ri = prman.Ri()

filename = "theProject.rib"
ri.Begin(filename)

ri.Display("theProject", "it", "rgb")
ri.Format(1024,720,1)
ri.Projection("perspective", {"fov":[45]})
ri.Integrator('PxrPathTracer', 'Integrator')
ri.DepthOfField(12,0.100,4)



def Cup(posX, posY, posZ, rotX, rotY, rotZ) :
    ri.TransformBegin()
    ri.Rotate(rotX-90,1,0,0)
    ri.Rotate(rotZ,0,1,0)
    ri.Rotate(rotY,0,0,1)

    ri.Translate(posX,-posY,posZ)

    ri.TransformBegin()
    ri.AttributeBegin()
    ri.Pattern("PxrVoronoise", "noiseTexture",
    {
    "float frequency":[5],
    "float jitter":[0.5],
    "float smoothness":[0]
    }
    )
    ri.Pattern("testShader", "testit",
    {
    "color Cin":[1,1,1],
    "float pos":[0.5],
    "float width":[0.1]
    }
    )
    ri.Bxdf("PxrDisney", "cupTex",
    {
    #"color baseColor" [ 0.9 0.0 0.0 ],
    "reference color baseColor":[ "testit:Cout" ],
    "reference float metallic":["testit:inStripe"],
    #"float metallic":[0.5],
    "float specular":[0.75],
    #"float anisotropic":[1.0],
    "float clearcoat":[0.35]
    }
    )

    ri.TransformBegin()
    ri.Translate(0,0,-2.75)
    ri.Scale(1,1,2)
    ri.Paraboloid(0.65,0.8,1.8,360)
    ri.TransformEnd()

    ri.TransformBegin()
    ri.Translate(0,0,0.85)
    ri.Scale(1,1,4)
    ri.Sphere(0.65,0,0.1,360)
    ri.TransformEnd()

    ri.TransformBegin()
    ri.Translate(-0.025,0,0)
    ri.Rotate(90,1,0,0)
    ri.Rotate(45,0,0,1)
    ri.Rotate(85,0,0,1)
    ri.Scale(1,1,2)
    ri.Torus(0.8,0.1,360,0,110)
    ri.TransformEnd()

    ri.AttributeEnd()
    ri.TransformEnd()

    ri.TransformEnd()
#endCup

def Donut(posX, posY, posZ, rotX, rotY, rotZ, sc) :
    ri.TransformBegin()
    ri.Rotate(rotX-90,1,0,0)
    ri.Rotate(rotZ,0,1,0)
    ri.Rotate(rotY,0,0,1)

    ri.Translate(posX,posZ,posY)
    ri.Scale(sc,sc,sc)
    
    ri.TransformBegin()
    ri.AttributeBegin()
    ri.Bxdf("PxrDisney","baseDonut",{"color baseColor":[0.6,0.3,0.1]})
    ri.TransformBegin()
    ri.Torus(0.8,0.3,360,0,360)
    ri.TransformEnd()
    ri.AttributeEnd()

    ri.AttributeBegin()
    ri.Pattern("PxrVoronoise","noiseTexture",
    {	
        "float frequency":[8],
        "float jitter":[0.5],
        "float smoothness":[0.4]
    }
    )
    ri.Bxdf("PxrDisney","chocDonut",
    {
        "color baseColor":[0.225,0.075,0.025],
        "reference float metallic":["noiseTexture:resultF"],
        "float specular":[0.2],
        "float metallic":[1.0],
        "float anisotropic":[1.0],
        "float clearcoat":[0.2]
    }
    )
    ri.TransformBegin()
    ri.Torus(0.805,0.305,180,0,360)
    ri.TransformEnd()
    ri.AttributeEnd()
    ri.TransformEnd()

    ri.TransformEnd()
#endDonut

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

ri.Rotate(-12,1,0,0)

Cup(-0.8,0,0,0,-15,0)

Donut(0.6,-1,0,0,0,0,0.75)

Table(0,-1.19,0,0,0,0,3)

#All the geometry goes here ^^^
ri.WorldEnd()
ri.End()