import json

def scaling(scalex=1.55, scaley=1.55,scalez=1.55,
    ratio_of_building_afn=0.85, window_scale=True, shading_scale=False,
    input_file='model.epJSON',output_name='scaled_model.epJSON'):
    # This function multiplies the vertices of the epJSON model by a
    # determined value.
    
    # scalex - Scale factor to be multiplied by the x vertices.
    # scaley - Scale factor to be multiplied by the y vertices.
    # scalez - Scale factor to be multiplied by the z vertices.
    # ratio_of_building_afn - New ratio of building value for AFN.
    # window_scale - Condition to change geometry of windows too.
    # shading_scale - Condition to change geometry of shading too.
    # input_file - The epJSON file to be edited.
    # output_name - The name of the output file to be created.
    
    # reading epJSON file
    file = open(input_file, "r")
    content = json.load(file)
    file.close()

    # changing epJSON fields
    ## AirflowNetwork:SimulationControl
    for i in list(content["AirflowNetwork:SimulationControl"].keys()):
        content["AirflowNetwork:SimulationControl"][i]["ratio_of_building_width_along_short_axis_to_width_along_long_axis"] =  ratio_of_building_afn

    ## BuildingSurface:Detailed
    for i in list(content["BuildingSurface:Detailed"].keys()):
        for j,k in enumerate(content["BuildingSurface:Detailed"][i]["vertices"]):
            content["BuildingSurface:Detailed"][i]["vertices"][j]["vertex_x_coordinate"] = content["BuildingSurface:Detailed"][i]["vertices"][j]["vertex_x_coordinate"]*scalex
            content["BuildingSurface:Detailed"][i]["vertices"][j]["vertex_y_coordinate"] = content["BuildingSurface:Detailed"][i]["vertices"][j]["vertex_y_coordinate"]*scaley
            content["BuildingSurface:Detailed"][i]["vertices"][j]["vertex_z_coordinate"] = content["BuildingSurface:Detailed"][i]["vertices"][j]["vertex_z_coordinate"]*scalez

    ## FenestrationSurface:Detailed
    if window_scale:
        for i in list(content["FenestrationSurface:Detailed"].keys()):
            if content["FenestrationSurface:Detailed"][i]["surface_type"] == "Window":
                content["FenestrationSurface:Detailed"][i]["vertex_1_x_coordinate"] = content["FenestrationSurface:Detailed"][i]["vertex_1_x_coordinate"]*scalex
                content["FenestrationSurface:Detailed"][i]["vertex_2_x_coordinate"] = content["FenestrationSurface:Detailed"][i]["vertex_2_x_coordinate"]*scalex
                content["FenestrationSurface:Detailed"][i]["vertex_3_x_coordinate"] = content["FenestrationSurface:Detailed"][i]["vertex_3_x_coordinate"]*scalex
                content["FenestrationSurface:Detailed"][i]["vertex_4_x_coordinate"] = content["FenestrationSurface:Detailed"][i]["vertex_4_x_coordinate"]*scalex
                    
                content["FenestrationSurface:Detailed"][i]["vertex_1_y_coordinate"] = content["FenestrationSurface:Detailed"][i]["vertex_1_y_coordinate"]*scaley
                content["FenestrationSurface:Detailed"][i]["vertex_2_y_coordinate"] = content["FenestrationSurface:Detailed"][i]["vertex_2_y_coordinate"]*scaley
                content["FenestrationSurface:Detailed"][i]["vertex_3_y_coordinate"] = content["FenestrationSurface:Detailed"][i]["vertex_3_y_coordinate"]*scaley
                content["FenestrationSurface:Detailed"][i]["vertex_4_y_coordinate"] = content["FenestrationSurface:Detailed"][i]["vertex_4_y_coordinate"]*scaley

                content["FenestrationSurface:Detailed"][i]["vertex_1_z_coordinate"] = content["FenestrationSurface:Detailed"][i]["vertex_1_z_coordinate"]*scalez
                content["FenestrationSurface:Detailed"][i]["vertex_2_z_coordinate"] = content["FenestrationSurface:Detailed"][i]["vertex_2_z_coordinate"]*scalez
                content["FenestrationSurface:Detailed"][i]["vertex_3_z_coordinate"] = content["FenestrationSurface:Detailed"][i]["vertex_3_z_coordinate"]*scalez
                content["FenestrationSurface:Detailed"][i]["vertex_4_z_coordinate"] = content["FenestrationSurface:Detailed"][i]["vertex_4_z_coordinate"]*scalez

    ## Shading:Building:Detailed
    if shading_scale:
        for i in list(content["Shading:Building:Detailed"].keys()):
            for j,k in enumerate(content["Shading:Building:Detailed"][i]["vertices"]):
                content["Shading:Building:Detailed"][i]["vertices"][j]["vertex_x_coordinate"] = content["Shading:Building:Detailed"][i]["vertices"][j]["vertex_x_coordinate"]*scalex
                content["Shading:Building:Detailed"][i]["vertices"][j]["vertex_y_coordinate"] = content["Shading:Building:Detailed"][i]["vertices"][j]["vertex_y_coordinate"]*scaley
                content["Shading:Building:Detailed"][i]["vertices"][j]["vertex_z_coordinate"] = content["Shading:Building:Detailed"][i]["vertices"][j]["vertex_z_coordinate"]*scalez

    ## Zone
    ## Shading:Building:Detailed
    for i in list(content["Zone"].keys()):
        content["Zone"][i]["x_origin"] = content["Zone"][i]["x_origin"]*scalex
        content["Zone"][i]["y_origin"] = content["Zone"][i]["y_origin"]*scaley
        content["Zone"][i]["z_origin"] = content["Zone"][i]["z_origin"]*scalez

    # writing  epJSON file
    file = open(output_name, "w")
    content = json.dumps(content)
    file.write(content)
    file.close()
