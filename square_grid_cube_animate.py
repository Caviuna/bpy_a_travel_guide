"""
This code is cube animation using square grid.

"""



import bpy 

grid_loc= (-10, -5, 0, 5, 10)       

count = 0 

for x in grid_loc: 
    for y in grid_loc: 
        for z in grid_loc: 
            obj_location = (x, y, z) 
            count += 1 
            obj_type = count % 4 
            if obj_type == 0: 
                bpy.ops.mesh.primitive_cube_add(size=2, align='WORLD',location=obj_location, scale=(1, 1, 1))
            elif obj_type == 1:
                bpy.ops.mesh.primitive_cube_add(size=2, align='WORLD',location=obj_location, scale=(1, 1, 1))
            elif obj_type == 2: 
                bpy.ops.mesh.primitive_cube_add(size=2, align='WORLD',location=obj_location, scale=(1, 1, 1))
            elif obj_type == 3: 
                bpy.ops.mesh.primitive_cube_add(size=2, align='WORLD',location=obj_location, scale=(1, 1, 1))
  
cubes = bpy.data.collections["Cubes"].objects

offset = 0  
for x in cubes: 
    x.rotation_euler = [0, 0, 0] 
    x.keyframe_insert(data_path = "rotation_euler", frame = 1 + offset)
    x.rotation_euler = [1, 1, 10] 
    x.keyframe_insert(data_path = "rotation_euler", frame = 50 + offset)
    x.rotation_euler = [.5, 1,.5] 
    x.keyframe_insert(data_path = "rotation_euler", frame = 70 + offset)
    x.rotation_euler = [1, 1, 1] 
    x.keyframe_insert(data_path = "rotation_euler", frame = 80 + offset)
    x.rotation_euler = [0, 0, 0] 
    x.keyframe_insert(data_path = "rotation_euler", frame = 120 + offset)
    offset += 1 
