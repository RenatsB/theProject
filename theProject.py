import prman

ri = prman.Ri()

filename = "theProject.rib"
ri.Begin(filename)

ri.Display("theProject", "it", "rgb")
ri.Format(640,480,0.9)
ri.Projection("perspective", {"fov":[45]})
ri.Integrator('PxrPathTracer', 'Integrator')
ri.DepthOfField(12,0.100,4)



def Cup(posX, posY, posZ, rotX, rotY, rotZ) :
    ri.TransformBegin()
    
    ri.Rotate(rotX,1,0,0)
    ri.Rotate(rotY,0,1,0)
    ri.Rotate(rotZ,0,0,1)

    ri.Translate(posX,posY,posZ)

    ri.TransformBegin()
    ri.Translate(0,0,0)
    ri.Scale(1,1,2)
    ri.Paraboloid(0.65,0.8,1.8,360)
    ri.TransformEnd()

    ri.TransformBegin()
    ri.Translate(0,0,1.78)
    ri.Scale(1,1,4)
    ri.Sphere(0.65,0,0.1,360)
    ri.TransformEnd()
    ri.TransformBegin()
    ri.Translate(-0.025,0,1)
    ri.Rotate(90,1,0,0)
    ri.Rotate(45,0,0,1)
    ri.Rotate(90,0,0,1)
    ri.Scale(1,1,2)
    ri.Torus(0.8,0.1,360,0,105)
    ri.TransformEnd()
    ri.TransformEnd()


ri.WorldBegin()
ri.AttributeBegin()
ri.Rotate(90,1,0,0)
ri.Light("PxrDomeLight", "holyLight",
{
"float exposure":[0],
"string lightColorMap":["hdrTest.tx"]
}
)
ri.AttributeEnd()

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
ri.Bxdf("PxrDisney", "test1",
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
Cup(0.25,0,-0.25,0,0,0)
ri.AttributeEnd()
ri.WorldEnd()
ri.End()