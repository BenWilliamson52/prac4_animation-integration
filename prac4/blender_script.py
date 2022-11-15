import random                       # Math Random
import bpy                          # Blender Python Module
import os                           # Operating System Module
import sys                          # System Module
import importlib                    # Importing Modules Module
from math import pi, radians        # Transformations Rotation

# Find out root directory of Blender Project
directory = os.path.dirname(bpy.data.filepath)
if not directory in sys.path:       # Check if this directory is in system Path
    sys.path.append(directory)      # Add Directory to Discoverable Path

import console_blender              # Import Custom Write to Console
importlib.reload(console_blender)   # Add custom module to the Blender Project (now that directory is know)
from console_blender import *       # After a reload import all the functions of the custom module

console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_monkey_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(12), int(14), int(8)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                
                frames += 0
                object.rotation_euler = (radians(0), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 100
                object.rotation_euler = (radians(360), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 100
                object.rotation_euler = (radians(720), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(9), int(50), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames += 200
                object.location = (int(9), int(-70), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")

                offset += 0             

    console("ENDS:")

except Exception as e:
    console(e)
    
console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made rings"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_torus_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                  
                frames += 0
                object.rotation_euler = (radians(90), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 200
                object.rotation_euler = (radians(90), radians(0), radians(360)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(9), int(30), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames = 80
                object.scale = (int(0), int(0), int(0)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                offset += 0     
                
                frames = 40
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")        

    console("ENDS:")

except Exception as e:
    console(e)
    
console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made rings 2"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_torus_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                  
                frames += 0
                object.rotation_euler = (radians(90), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 200
                object.rotation_euler = (radians(90), radians(0), radians(360)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(9), int(20), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames = 50
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale") 
                
                frames = 80
                object.scale = (int(0), int(0), int(0)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                offset += 0     
                
                      

    console("ENDS:")

except Exception as e:
    console(e)
    
console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made rings 2"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_torus_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                  
                frames += 0
                object.rotation_euler = (radians(90), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 200
                object.rotation_euler = (radians(90), radians(0), radians(360)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(9), int(10), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames = 60
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale") 
                
                frames = 80
                object.scale = (int(0), int(0), int(0)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                offset += 0     
                
                      

    console("ENDS:")

except Exception as e:
    console(e)
    
console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made rings 2"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_torus_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                  
                frames += 0
                object.rotation_euler = (radians(90), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 200
                object.rotation_euler = (radians(90), radians(0), radians(360)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(9), int(0), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames = 70
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale") 
                
                frames = 90
                object.scale = (int(0), int(0), int(0)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                offset += 0     
                
                      

    console("ENDS:")

except Exception as e:
    console(e)
    
console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made rings 2"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_torus_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                  
                frames += 0
                object.rotation_euler = (radians(90), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 200
                object.rotation_euler = (radians(90), radians(0), radians(360)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(9), int(-10), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames = 80
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale") 
                
                frames = 100
                object.scale = (int(0), int(0), int(0)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                offset += 0     
                
                      

    console("ENDS:")

except Exception as e:
    console(e)
    
console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made rings 2"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_torus_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                  
                frames += 0
                object.rotation_euler = (radians(90), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 200
                object.rotation_euler = (radians(90), radians(0), radians(360)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(9), int(-20), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames = 90
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale") 
                
                frames = 120
                object.scale = (int(0), int(0), int(0)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                offset += 0     
                
                      

    console("ENDS:")

except Exception as e:
    console(e)

console("STARTS:")


# second set of rings and monkey



# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_monkey_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(12), int(14), int(8)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                
                frames += 0
                object.rotation_euler = (radians(0), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 100
                object.rotation_euler = (radians(360), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 100
                object.rotation_euler = (radians(720), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(37), int(60), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames += 200
                object.location = (int(30), int(-70), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")

                offset += 0             

    console("ENDS:")

except Exception as e:
    console(e)
    
console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made rings"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_torus_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                  
                frames += 0
                object.rotation_euler = (radians(90), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 200
                object.rotation_euler = (radians(90), radians(0), radians(360)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(35), int(40), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames = 80
                object.scale = (int(0), int(0), int(0)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                offset += 0     
                
                frames = 40
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")        

    console("ENDS:")

except Exception as e:
    console(e)
    
console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made rings 2"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_torus_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                  
                frames += 0
                object.rotation_euler = (radians(90), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 200
                object.rotation_euler = (radians(90), radians(0), radians(360)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(35), int(30), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames = 50
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale") 
                
                frames = 80
                object.scale = (int(0), int(0), int(0)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                offset += 0     
                
                      

    console("ENDS:")

except Exception as e:
    console(e)
    
console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made rings 2"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_torus_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                  
                frames += 0
                object.rotation_euler = (radians(90), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 200
                object.rotation_euler = (radians(90), radians(0), radians(360)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(35), int(20), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames = 60
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale") 
                
                frames = 80
                object.scale = (int(0), int(0), int(0)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                offset += 0     
                
                      

    console("ENDS:")

except Exception as e:
    console(e)
    
console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made rings 2"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_torus_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                  
                frames += 0
                object.rotation_euler = (radians(90), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 200
                object.rotation_euler = (radians(90), radians(0), radians(360)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(35), int(10), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames = 70
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale") 
                
                frames = 90
                object.scale = (int(0), int(0), int(0)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                offset += 0     
                
                      

    console("ENDS:")

except Exception as e:
    console(e)
    
console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made rings 2"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_torus_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                  
                frames += 0
                object.rotation_euler = (radians(90), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 200
                object.rotation_euler = (radians(90), radians(0), radians(360)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(35), int(0), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames = 80
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale") 
                
                frames = 100
                object.scale = (int(0), int(0), int(0)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                offset += 0     
                
                      

    console("ENDS:")

except Exception as e:
    console(e)
    
console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made rings 2"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_torus_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                  
                frames += 0
                object.rotation_euler = (radians(90), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 200
                object.rotation_euler = (radians(90), radians(0), radians(360)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(35), int(-10), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames = 90
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale") 
                
                frames = 120
                object.scale = (int(0), int(0), int(0)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                offset += 0     
                
                      

    console("ENDS:")

except Exception as e:
    console(e)

# third set of monkey and rings

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_monkey_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(12), int(14), int(8)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                
                frames += 0
                object.rotation_euler = (radians(0), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 100
                object.rotation_euler = (radians(360), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 100
                object.rotation_euler = (radians(720), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(-18), int(60), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames += 200
                object.location = (int(-18), int(-70), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")

                offset += 0             

    console("ENDS:")

except Exception as e:
    console(e)
    
console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made rings"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_torus_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                  
                frames += 0
                object.rotation_euler = (radians(90), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 200
                object.rotation_euler = (radians(90), radians(0), radians(360)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(-15), int(40), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames = 80
                object.scale = (int(0), int(0), int(0)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                offset += 0     
                
                frames = 40
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")        

    console("ENDS:")

except Exception as e:
    console(e)
    
console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made rings 2"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_torus_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                  
                frames += 0
                object.rotation_euler = (radians(90), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 200
                object.rotation_euler = (radians(90), radians(0), radians(360)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(-15), int(30), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames = 50
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale") 
                
                frames = 80
                object.scale = (int(0), int(0), int(0)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                offset += 0     
                
                      

    console("ENDS:")

except Exception as e:
    console(e)
    
console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made rings 2"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_torus_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                  
                frames += 0
                object.rotation_euler = (radians(90), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 200
                object.rotation_euler = (radians(90), radians(0), radians(360)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(-15), int(20), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames = 60
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale") 
                
                frames = 80
                object.scale = (int(0), int(0), int(0)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                offset += 0     
                
                      

    console("ENDS:")

except Exception as e:
    console(e)
    
console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made rings 2"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_torus_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                  
                frames += 0
                object.rotation_euler = (radians(90), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 200
                object.rotation_euler = (radians(90), radians(0), radians(360)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(-15), int(10), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames = 70
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale") 
                
                frames = 90
                object.scale = (int(0), int(0), int(0)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                offset += 0     
                
                      

    console("ENDS:")

except Exception as e:
    console(e)
    
console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made rings 2"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_torus_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                  
                frames += 0
                object.rotation_euler = (radians(90), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 200
                object.rotation_euler = (radians(90), radians(0), radians(360)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(-15), int(0), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames = 80
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale") 
                
                frames = 100
                object.scale = (int(0), int(0), int(0)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                offset += 0     
                
                      

    console("ENDS:")

except Exception as e:
    console(e)
    
console("STARTS:")

# catching code
try:          
    result = bpy.data.scenes
    console(f"Scenes: {result}")

    for object in result:
        console(f"Scene Name: {object.collection.name}")

    result = bpy.data.collections
    console(f"Collections: {result}")

    for object in result:
        console(f"Collection Name: {object.name}")

    # Add custom collection, rename it and add it as a scene child
    collection = bpy.data.collections.new('bennie collection')
    collection.name = "python made rings 2"

    # Add the Collection to the Scene
    bpy.context.scene.collection.children.link(collection)

    # Set the new collection as the active one
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    for i in range(1):
       
   
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        # Add objects to Collection
        obj = bpy.ops.mesh.primitive_torus_add(location=(x, y, z))
        bpy.ops.object.shade_smooth()    

    console("Accessing Data-Blocks")
    console("Accessing Scene Collection")
    result = bpy.data.objects
    console(f"Objects in the Scene: {result}")

    console("Accessing Collections in a Scene")

    # Rotation in radians
    degrees = 45
    radian_rotation = degrees * pi / 180

    offset = 0

    
    for result in bpy.data.collections:
        if result.name == collection.name:
            for object in result.objects:
                
                object.modifiers.new("Scripted Modifier","SOLIDIFY")
                
                frames = 0
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                  
                frames += 0
                object.rotation_euler = (radians(90), radians(0), radians(0)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames += 200
                object.rotation_euler = (radians(90), radians(0), radians(360)) # Rotation
                console(f"Rotation => x:{object.rotation_euler.x}, y:{object.rotation_euler.y}, x:{object.rotation_euler.z}")
                object.keyframe_insert(data_path="rotation_euler", frame=frames + offset, group="Rotation")
                
                frames = 0
                object.location = (int(-15), int(-10), int(5)) # Translate, moving along Y
                console(f"Translation => x:{object.location.x}, y:{object.location.y}, x:{object.location.z}")
                object.keyframe_insert(data_path="location", frame=frames + offset, group="Translation")
                frames = 0

                frames = 90
                object.scale = (int(5), int(6), int(3)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale") 
                
                frames = 120
                object.scale = (int(0), int(0), int(0)) # Scale
                console(f"Scale => x:{object.scale.x}, y:{object.scale.y}, x:{object.scale.z}")
                object.keyframe_insert(data_path="scale", frame=frames + offset, group="Scale")
                offset += 0     
                
                      

    console("ENDS:")

except Exception as e:
    console(e)