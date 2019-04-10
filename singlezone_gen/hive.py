
from dict_update import update

def hive(wall_i=2, zone_x=5, zone_y=4, zone_height=3, floor_height=10, ground=1, roof=1, door=False):
    # Creates the adjacent zone and its surfaces
    
    wall_blank = {
        "surface_type": "Wall",
        "construction_name": "wall_construction_inverse",
        "idf_max_extensible_fields": 12,
        "idf_max_fields": 22,
        "number_of_vertices": 4.0,
        "zone_name": "hive_"+str(wall_i)
    }
    
    afn_zone = {
        "AirflowNetwork:MultiZone:Zone "+str(wall_i+1): {
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 8,
            "idf_order": 78,
            "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
            "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
            "zone_name": "hive_" +str(wall_i)
        }
    }
        
    zone = {
        "direction_of_relative_north": 0.0,
        "idf_max_extensible_fields": 0,
        "idf_max_fields": 7,
        "multiplier": 1,
        "x_origin": 0,
        "y_origin": 0,
        "z_origin": floor_height
    }
    
    hive_externalnodes = {}
    hive_cracks = {}
    hive_surfaces = {}
    hive_door = {}
    
    ceiling_obj = {
            "zone_name": "hive_" +str(wall_i),
            "construction_name": "ceiling_construction",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "number_of_vertices": 4.0
    }
    
    if roof > 0:
        ceiling_obj["outside_boundary_condition"] = "Outdoors"
        ceiling_obj["surface_type"] = "Roof"
        ceiling_obj["sun_exposure"] = "SunExposed"
        ceiling_obj["wind_exposure"] = "WindExposed"
    else:
        ceiling_obj["outside_boundary_condition"] = "Adiabatic"
        ceiling_obj["surface_type"] = "Ceiling"
        ceiling_obj["sun_exposure"] = "NoSun"
        ceiling_obj["wind_exposure"] = "NoWind"
    
    hive_surfaces['hive_'+str(wall_i)+'_ceiling'] = ceiling_obj
    
    ground_obj = {
            "zone_name": "hive_" +str(wall_i),
            "surface_type": "Floor",
            "construction_name": "floor_construction",
            "sun_exposure": "NoSun",
            "wind_exposure": "NoWind",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "number_of_vertices": 4.0
        }
        
    if ground > 0:
        ground_obj["outside_boundary_condition"] = "OtherSideConditionsModel"
        ground_obj["outside_boundary_condition_object"] = "GroundCoupledOSCM"

    else:
        ground_obj["outside_boundary_condition"] = "Adiabatic"
    
    hive_surfaces['hive_'+str(wall_i)+'_floor'] = ground_obj
    
    for j in range(4):
        hive_surfaces["hive_"+str(wall_i)+"_wall-"+str(j)] = {}
        if (j+2)%4 == wall_i:
            hive_surfaces["hive_"+str(wall_i)+"_wall-"+str(j)]["outside_boundary_condition"] = "Surface"
            hive_surfaces["hive_"+str(wall_i)+"_wall-"+str(j)]["outside_boundary_condition_object"] = "wall-"+str((j+2)%4)
            hive_surfaces["hive_"+str(wall_i)+"_wall-"+str(j)]["sun_exposure"] = "NoSun"
            hive_surfaces["hive_"+str(wall_i)+"_wall-"+str(j)]["wind_exposure"] = "NoWind"
        else:
            hive_surfaces["hive_"+str(wall_i)+"_wall-"+str(j)]["outside_boundary_condition"] = "Outdoors"
            hive_surfaces["hive_"+str(wall_i)+"_wall-"+str(j)]["sun_exposure"] = "SunExposed"
            hive_surfaces["hive_"+str(wall_i)+"_wall-"+str(j)]["wind_exposure"] = "WindExposed"
            hive_cracks["Surface_hive_"+str(wall_i)+"_wall-"+str(j)] = {
                "external_node_name": "Node_hive_"+str(wall_i)+"_wall-"+str(j),
                "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
                "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
                "leakage_component_name": "crack",
                "surface_name": "hive_"+str(wall_i)+"_wall-"+str(j)                
            }
            hive_externalnodes["Node_hive_"+str(wall_i)+"_wall-"+str(j)] = {
                "idf_max_extensible_fields": 0,
                "idf_max_fields": 5,
                "symmetric_wind_pressure_coefficient_curve": "No",
                "wind_angle_type": "Absolute",
                "wind_pressure_coefficient_curve_name": "side_"+str(j)+"_coef"
            }
            
        hive_surfaces["hive_"+str(wall_i)+"_wall-"+str(j)].update(wall_blank)
        
    if wall_i == 0:
        
        x0 = 0
        x1 = zone_x
        y0 = zone_y
        y1 = 2*zone_y
    
    if wall_i == 1:
        
        x0 = zone_x
        x1 = 2*zone_x
        y0 = 0
        y1 = zone_y
    
    if wall_i == 2:
        
        x0 = 0
        x1 = zone_x
        y0 = -zone_y
        y1 = 0
    
    if wall_i == 3:
        
        x0 = -zone_x
        x1 = 0
        y0 = 0
        y1 = zone_y
    
    hive_surfaces["hive_"+str(wall_i)+"_ceiling"]["vertices"] = [
        {
            "vertex_x_coordinate": x0,
            "vertex_y_coordinate": y1,
            "vertex_z_coordinate": zone_height
        },
        {
            "vertex_x_coordinate": x0,
            "vertex_y_coordinate": y0,
            "vertex_z_coordinate": zone_height
        },
        {
            "vertex_x_coordinate": x1,
            "vertex_y_coordinate": y0,
            "vertex_z_coordinate": zone_height
        },
        {
            "vertex_x_coordinate": x1,
            "vertex_y_coordinate": y1,
            "vertex_z_coordinate": zone_height
        }
    ]    

    hive_surfaces["hive_"+str(wall_i)+"_floor"]["vertices"] = [
        {
            "vertex_x_coordinate": x1,
            "vertex_y_coordinate": y1,
            "vertex_z_coordinate": 0.0
        },
        {
            "vertex_x_coordinate": x1,
            "vertex_y_coordinate": y0,
            "vertex_z_coordinate": 0.0
        },
        {
            "vertex_x_coordinate": x0,
            "vertex_y_coordinate": y0,
            "vertex_z_coordinate": 0.0
        },
        {
            "vertex_x_coordinate": x0,
            "vertex_y_coordinate": y1,
            "vertex_z_coordinate": 0.0
        }
    ]    

    hive_surfaces["hive_"+str(wall_i)+"_wall-0"]["vertices"] = [
        {
            "vertex_x_coordinate": x1,
            "vertex_y_coordinate": y1,
            "vertex_z_coordinate": zone_height
        },
        {
            "vertex_x_coordinate": x1,
            "vertex_y_coordinate": y1,
            "vertex_z_coordinate": 0.0
        },
        {
            "vertex_x_coordinate": x0,
            "vertex_y_coordinate": y1,
            "vertex_z_coordinate": 0.0
        },
        {
            "vertex_x_coordinate": x0,
            "vertex_y_coordinate": y1,
            "vertex_z_coordinate": zone_height
        }
    ]    

    hive_surfaces["hive_"+str(wall_i)+"_wall-1"]["vertices"] = [
        {
            "vertex_x_coordinate": x1,
            "vertex_y_coordinate": y0,
            "vertex_z_coordinate": zone_height
        },
        {
            "vertex_x_coordinate": x1,
            "vertex_y_coordinate": y0,
            "vertex_z_coordinate": 0.0
        },
        {
            "vertex_x_coordinate": x1,
            "vertex_y_coordinate": y1,
            "vertex_z_coordinate": 0.0
        },
        {
            "vertex_x_coordinate": x1,
            "vertex_y_coordinate": y1,
            "vertex_z_coordinate": zone_height
        }
    ]    

    hive_surfaces["hive_"+str(wall_i)+"_wall-2"]["vertices"] = [
        {
            "vertex_x_coordinate": x0,
            "vertex_y_coordinate": y0,
            "vertex_z_coordinate": zone_height
        },
        {
            "vertex_x_coordinate": x0,
            "vertex_y_coordinate": y0,
            "vertex_z_coordinate": 0.0
        },
        {
            "vertex_x_coordinate": x1,
            "vertex_y_coordinate": y0,
            "vertex_z_coordinate": 0.0
        },
        {
            "vertex_x_coordinate": x1,
            "vertex_y_coordinate": y0,
            "vertex_z_coordinate": zone_height
        }
    ]    

    hive_surfaces["hive_"+str(wall_i)+"_wall-3"]["vertices"] = [
        {
            "vertex_x_coordinate": x0,
            "vertex_y_coordinate": y1,
            "vertex_z_coordinate": zone_height
        },
        {
            "vertex_x_coordinate": x0,
            "vertex_y_coordinate": y1,
            "vertex_z_coordinate": 0.0
        },
        {
            "vertex_x_coordinate": x0,
            "vertex_y_coordinate": y0,
            "vertex_z_coordinate": 0.0
        },
        {
            "vertex_x_coordinate": x0,
            "vertex_y_coordinate": y0,
            "vertex_z_coordinate": zone_height
        }
    ]
    
    
    
    if wall_i == 2 and door:
        hive_door["hive_door"] = {
            "building_surface_name": "hive_2_wall-0",
            "outside_boundary_condition_object": 'door',
            "construction_name": "door_construction",
            "number_of_vertices": 4.0,
            "surface_type": "Door",
            "vertex_1_x_coordinate": 1,
            "vertex_1_y_coordinate": 0,
            "vertex_1_z_coordinate": 2.1,
            "vertex_2_x_coordinate": 1,
            "vertex_2_y_coordinate": 0,
            "vertex_2_z_coordinate": 0,
            "vertex_3_x_coordinate": .1,
            "vertex_3_y_coordinate": 0,
            "vertex_3_z_coordinate": 0,
            "vertex_4_x_coordinate": .1,
            "vertex_4_y_coordinate": 0,
            "vertex_4_z_coordinate": 2.1,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22
        }
    
    afn = {'cracks':hive_cracks,'zone':afn_zone, 'nodes': hive_externalnodes}
    return(zone, afn, hive_surfaces, hive_door)

'''
print(hive(wall_i=0, zone_x=5, zone_y=4, zone_height=3, floor_height=10, ground=1, roof=1))
print(hive(wall_i=1, zone_x=6, zone_y=5, zone_height=4, floor_height=12, ground=0, roof=0))
print(hive(wall_i=2, zone_x=7, zone_y=6, zone_height=5, floor_height=14, ground=0, roof=1))
print(hive(wall_i=3, zone_x=8, zone_y=7, zone_height=6, floor_height=16, ground=1, roof=0))
'''     
