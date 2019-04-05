# This code creates a epJSON file (EnergyPlus model), according to the
# input parameters defined on the main function.
#
# Notice that the names given to the surfaces go from 0 to 3 clockwise,
# being: 0 up, 1 right, 2 down, and 3 left. 

from cp_calc_res import cp_calc
from dict_update import update
import json
from hive import hive

SEED_DOOR_FILE = 'seed_door.json'
    
def main(zone_area=10, zone_ratio=1, zone_height=3, azimuth=0,
    absorptance=.5, wall_u=2.5, wall_ct=100, ground=0, roof=0, 
    shading=[1,.5,0,0], living_room = True, exp=[1,1,1,0],
    wwr=[.6,0,0,0], open_fac=[.5,0,0,0], glass_fs=.87, equipment=120,
    lights = 5, bldg_ratio=1, floor_height=0, door=False, hive=True,
    input_file='seed.json' , output='output.epJSON'):
        
    ## Main function that creates the epJSON model.
    
    ## INPUTS:
    ## zone_area - The area of the "APP" in square meters.
    ## zone_ratio - Ratio between y length (walls 1 and 3), and xlength
    #  (walls 0 and 2). Or: Ratio = zone_y/zone_x.
    ## zone_height - Distance from floor to ceiling in meters.
    ## azimuth - Angle from north.
    ## ground - Condition of exposure: 0 = Adiabatic, 1 = Outdoors.
    ## roof - Condition of exposure: 0 = Adiabatic, 1 = Outdoors.
    ## shading - the length of horizontal shading in meters.
    ## living_room - Defines schedules for occupation: True = living 
    #  room occupation pattern, False = bedroom occupation pattern.
    ## exp - List with condition of exposure of walls: 0 = not exposed,
    #  1 = exposed (Outdoors).
    ## wwr - List with WWR of the walls.
    ## open_fac - List with the opening factors of windows.
    ## glass_fs - SHGC of the windows' glass.
    ## equipment - Equipment loads in Watts
    ## lights - Lights loads in Watts per square meters.
    ## bldg_ratio - The ratio of the reference building.
    ## floor_height - Distance from zone's floor to the ground in meters.
    ## door - Condition to create or not a door in the zone.
    ## hive - Condition to use or not the hive model approach.
    ## input_file - The name of the seed file. The seed files contains
    #  the information that do not depend on the input variables.
    ## output - The name of the generated epJSON model.
    
    print(output)
    
    #### Values of components' transmittance and thermal capacity ------
    #### CONCRETE+EPS wall approach
    
    c_concrete = 1.75    # concrete's condutivity {W/m-K}
    specific_heat = 1    # concrete's specific heat {kJ/kg-K}
    density = 2200       # concrete's density {kg/m3}
    e_concrete = wall_ct/(specific_heat*density)
    R_concrete = e_concrete/c_concrete
    R_eps = (1-(.17+R_concrete)*wall_u)/wall_u
    eps = True
    if R_eps < 0.0001:
        # Condition to ignore EPS with insignificant R values.
        eps = False
        c_concrete = (wall_u*e_concrete)/(1-.17*wall_u)
        print('EPS not used!')
        print('wall_u: ', wall_u, '\n', 'wall_ct: ', wall_ct)
        
    #### Defining zone's x and y length --------------------------------
    zone_x = (zone_area/zone_ratio)**(1/2)
    zone_y = (zone_area /zone_x)
    
    #### Defining Occupation condition ---------------------------------
    
    if living_room:
        occupation_sch = 'livingroom_occup'
        light_sch = 'livingroom_lights'
        activity_sch = 'livingroom_activity'
        number_of_people = 4
    else:
        occupation_sch = 'bedroom_occup'
        light_sch = 'bedroom_lights'
        activity_sch = 'bedroom_activity'
        number_of_people = 2

    #### START BUILDING OBJECTS ----------------------------------------
    model = dict()

    ##### Building -----------------------------------------------------
    model["Building"] = {
        output[:-7]: {
            "north_axis": azimuth,
            "loads_convergence_tolerance_value": 0.04,
            "maximum_number_of_warmup_days": 25,
            "solar_distribution": "FullInteriorAndExterior",
            "temperature_convergence_tolerance_value": 0.4,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 8,
            "terrain": "City"
        }
    }

    ##### ZONE ---------------------------------------------------------
    model["Zone"] = {
        "room": {
            "z_origin": floor_height
        }
    }

    ##### Building Surface ---------------------------------------------
    model["BuildingSurface:Detailed"] = {

        # Ceiling
        "ceiling": {
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": zone_height
                }
            ]
        },

        # Floor
        "floor": {
            "vertices": [
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": 0.0
                }
            ]
        },

        # Walls: 0 = up, 1 = right, 2 = down, 3 = left
        "wall-0": {
            "vertices": [
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": zone_height
                }
            ]
        },
        "wall-1": {
            "vertices": [
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": zone_height
                }
            ]
        },
        "wall-2": {
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": zone_height
                }
            ]
        },
        "wall-3": {
            "vertices": [
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": zone_height
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": zone_height
                }
            ]
        }
    }

    # Top Condition
    if roof == 0:
        ceiling_bound = {
            "outside_boundary_condition": "Adiabatic",
            "sun_exposure": "NoSun",
            "surface_type": "Ceiling",
            "wind_exposure": "NoWind"
        }

    else:
        ceiling_bound = {
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Roof",
            "wind_exposure": "WindExposed"
        }

    model["BuildingSurface:Detailed"]["ceiling"].update(ceiling_bound)

    # Bottom condition
    if ground == 0:
        ground_bound = {
            "outside_boundary_condition": "Adiabatic",
            "sun_exposure": "NoSun",
            "wind_exposure": "NoWind"
        }

    else:
        ground_bound = {
            "outside_boundary_condition": "Ground",
            "sun_exposure": "NoSun",
            "wind_exposure": "NoWind"
        }

    model["BuildingSurface:Detailed"]["floor"].update(ground_bound)

    # Wall exposition condition
    exposed_wall = {
        "outside_boundary_condition": "Outdoors",
        "sun_exposure": "SunExposed",
        "wind_exposure": "WindExposed"
    }
    adiabatic_wall = {
        "outside_boundary_condition": "Adiabatic",
        "sun_exposure": "NoSun",
        "wind_exposure": "NoWind"
    }
    hive_wall = {
        "outside_boundary_condition": "Surface",
        "sun_exposure": "NoSun",
        "wind_exposure": "NoWind"
    }
    
    
    if sum(exp) < 4:
        model['AirflowNetwork:MultiZone:Zone'] = {}
        model["AirflowNetwork:MultiZone:Surface:Crack"] = {}
        
    for i in range(4):
        
        if exp[i] > 0:
            model["BuildingSurface:Detailed"]["wall-"+str(i)].update(exposed_wall)
        else:
            if hive:
                model["BuildingSurface:Detailed"]["wall-"+str(i)].update(hive_wall)
                model["BuildingSurface:Detailed"]["wall-"+str(i)]["outside_boundary_condition_object"] = "hive_"+str(i)+"_wall-"+str((i+2)%4)
                model["Zone"]["hive_" +str(i)], afn_zone, hive_carcks, hive_surfaces, hive_door = hive(i, zone_x, zone_y, zone_height,floor_height, ground, roof, door)
                model['AirflowNetwork:MultiZone:Zone'].update(afn_zone)
                model["AirflowNetwork:MultiZone:Surface:Crack"].update(hive_carcks)
                model["BuildingSurface:Detailed"].update(hive_surfaces)
            else:
                model["BuildingSurface:Detailed"]["wall-"+str(i)].update(adiabatic_wall)

    #### FENESTRATION --------------------------------------------------
    model["FenestrationSurface:Detailed"] = {}
    for i in range(4):
        
        if wwr[i] > 0:

            window_z1 = zone_height*(1-wwr[i])*.5
            window_z2 = window_z1+(zone_height*wwr[i])
            
            if i == 0:
                window_x1 = zone_x*.999
                window_x2 = zone_x*.001
                window_y1 = zone_y
                window_y2 = zone_y
            elif i == 1:
                window_x1 = zone_x
                window_x2 = zone_x
                window_y1 = zone_y*.001
                window_y2 = zone_y*.999
            elif i == 2:
                window_x1 = zone_x*.001
                window_x2 = zone_x*.999
                window_y1 = 0
                window_y2 = 0
            else:
                window_x1 = 0
                window_x2 = 0
                window_y1 = zone_y*.999
                window_y2 = zone_y*.001
            
            model["FenestrationSurface:Detailed"]["window_"+str(i)] = {
                "building_surface_name": "wall-"+str(i),
                "construction_name": "glass_construction",
                "number_of_vertices": 4.0,
                "surface_type": "Window",
                "vertex_1_x_coordinate": window_x1,
                "vertex_1_y_coordinate": window_y1,
                "vertex_1_z_coordinate": window_z2,
                "vertex_2_x_coordinate": window_x1,
                "vertex_2_y_coordinate": window_y1,
                "vertex_2_z_coordinate": window_z1,
                "vertex_3_x_coordinate": window_x2,
                "vertex_3_y_coordinate": window_y2,
                "vertex_3_z_coordinate": window_z1,
                "vertex_4_x_coordinate": window_x2,
                "vertex_4_y_coordinate": window_y2,
                "vertex_4_z_coordinate": window_z2
            }
    
    for obj in model['FenestrationSurface:Detailed']:
        model['FenestrationSurface:Detailed'][obj].update({
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 22
        })
    
    #### SHADING -------------------------------------------------------
    
    z_shading = floor_height+zone_height
    
    if shading[0] > 0.01:
        
        model['Shading:Building:Detailed'] = {
            'shading_0': {
                "idf_max_extensible_fields": 12,
                "idf_max_fields": 15,
                'transmittance_schedule_name': '',
                'number_of_vertices': 4,
                "vertices": [
                    {
                    "vertex_x_coordinate": 0,
                    "vertex_y_coordinate": zone_y+shading[0],
                    "vertex_z_coordinate": z_shading
                    },
                    {
                    "vertex_x_coordinate": 0,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": z_shading
                    },
                    {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": zone_y,
                    "vertex_z_coordinate": z_shading
                    },
                    {
                    "vertex_x_coordinate": zone_x,
                    "vertex_y_coordinate": zone_y+shading[0],
                    "vertex_z_coordinate": z_shading
                    }
                ]
            }
        }
        
    if shading[1] > 0.01:

        model['Shading:Building:Detailed']['shading_1'] = {
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 15,
            'transmittance_schedule_name': '',
            'number_of_vertices': 4,
            "vertices": [
                {
                "vertex_x_coordinate": zone_x+shading[1],
                "vertex_y_coordinate": zone_y,
                "vertex_z_coordinate": z_shading
                },
                {
                "vertex_x_coordinate": zone_x,
                "vertex_y_coordinate": zone_y,
                "vertex_z_coordinate": z_shading
                },
                {
                "vertex_x_coordinate": zone_x,
                "vertex_y_coordinate": 0,
                "vertex_z_coordinate": z_shading
                },
                {
                "vertex_x_coordinate": zone_x+shading[1],
                "vertex_y_coordinate": 0,
                "vertex_z_coordinate": z_shading
                }
            ]
        }
        
    if shading[2] > 0.01:

        model['Shading:Building:Detailed']['shading_2'] = {
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 15,
            'transmittance_schedule_name': '',
            'number_of_vertices': 4,
            "vertices": [
                {
                "vertex_x_coordinate": zone_x,
                "vertex_y_coordinate": -shading[2],
                "vertex_z_coordinate": z_shading
                },
                {
                "vertex_x_coordinate": zone_x,
                "vertex_y_coordinate": 0,
                "vertex_z_coordinate": z_shading
                },
                {
                "vertex_x_coordinate": 0,
                "vertex_y_coordinate": 0,
                "vertex_z_coordinate": z_shading
                },
                {
                "vertex_x_coordinate": 0,
                "vertex_y_coordinate": -shading[2],
                "vertex_z_coordinate": z_shading
                }
            ]
        }
        
    if shading[3] > 0.01:

        model['Shading:Building:Detailed']['shading_3'] = {
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 15,
            'transmittance_schedule_name': '',
            'number_of_vertices': 4,
            "vertices": [
                {
                "vertex_x_coordinate": -shading[3],
                "vertex_y_coordinate": 0,
                "vertex_z_coordinate": z_shading
                },
                {
                "vertex_x_coordinate": 0,
                "vertex_y_coordinate": 0,
                "vertex_z_coordinate": z_shading
                },
                {
                "vertex_x_coordinate": 0,
                "vertex_y_coordinate": zone_y,
                "vertex_z_coordinate": z_shading,
                },
                {
                "vertex_x_coordinate": -shading[3],
                "vertex_y_coordinate": zone_y,
                "vertex_z_coordinate": z_shading
                }
            ]
        }
         
    #### THERMAL LOADS -------------------------------------------------
    if living_room:
        model["ElectricEquipment"] = {
            "equipment_loads": {
                "design_level": equipment,
                "design_level_calculation_method": "EquipmentLevel",
                "end_use_subcategory": "General",
                "fraction_latent": 0,
                "fraction_lost": 0,
                "fraction_radiant": 0.3,
                "idf_max_extensible_fields": 0,
                "idf_max_fields": 11,
                "schedule_name": "livingroom_equipment",
                "zone_or_zonelist_name": "room"
            }
        }

    model["Lights"] = {
        "lights": {
            "watts_per_zone_floor_area": lights,
            "schedule_name": light_sch
        }
    }

    model["People"] = {
        "people": {
            "number_of_people": number_of_people,
            "number_of_people_schedule_name": occupation_sch,
            "activity_level_schedule_name": activity_sch
        }
    }

    #### MATERIALS -----------------------------------------------------

    model["Material"] = {
        "ArgamassaReboco(25mm)": {
            "solar_absorptance": absorptance
        },
        "concrete": {
            "conductivity": c_concrete,
            "thickness": e_concrete
        }
    }
    
    if eps:
        model['Material:NoMass'] = {
            'EPS': {
                'thermal_resistance': R_eps,
                'solar_absorptance': absorptance
            }
        }

    model["WindowMaterial:SimpleGlazingSystem"] = {
        "glass_material": {
            "solar_heat_gain_coefficient": glass_fs
        }
    }

    #### AFN OBJECTS ---------------------------------------------------

    # AFN Simulation Control
    if bldg_ratio <= 1:  # x/y
        wind_azimuth = azimuth%180
    else:
        bldg_ratio = 1/bldg_ratio
        wind_azimuth = (azimuth+90)%180
        
    model["AirflowNetwork:SimulationControl"] = {
        "Ventilacao": {
            "azimuth_angle_of_long_axis_of_building": wind_azimuth,
            "ratio_of_building_width_along_short_axis_to_width_along_long_axis": bldg_ratio
        }
    }

    # AFN Surface

    model["AirflowNetwork:MultiZone:ExternalNode"] = {}
    model["AirflowNetwork:MultiZone:Surface"] = {}
    
    for i in range(4):
        if wwr[i] > 0:
            model["AirflowNetwork:MultiZone:Surface"]["AirflowNetwork:MultiZone:Surface "+str(i)] = {
                "external_node_name": "window_"+str(i)+"_Node",
                "indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor": 300000.0,
                "indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor": 100.0,
                "leakage_component_name": "detailed_window",
                "surface_name": "window_"+str(i),
                "ventilation_control_mode": "Temperature",
                "ventilation_control_zone_temperature_setpoint_schedule_name": "Temp_setpoint",
                "venting_availability_schedule_name": occupation_sch,
                "window_door_opening_factor_or_crack_factor": open_fac[i]
            }
            
            model["AirflowNetwork:MultiZone:ExternalNode"]["window_"+str(i)+"_Node"] = {
                "idf_max_extensible_fields": 0,
                "idf_max_fields": 5,
                "symmetric_wind_pressure_coefficient_curve": "No",
                "wind_angle_type": "Absolute",
                "wind_pressure_coefficient_curve_name": "side_"+str(i)+"_coef"
            }
    
    for obj in model["AirflowNetwork:MultiZone:Surface"]:
        
        model["AirflowNetwork:MultiZone:Surface"][obj].update({
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 12
        })
        
    window_areas = []
    
    for i in range(4):
        if i%2 == 0:
            window_areas.append(wwr[i] * open_fac[i] * zone_x)
        else:
            window_areas.append(wwr[i] * open_fac[i] * zone_y)
            
    if door:
        if hive:
            model["AirflowNetwork:MultiZone:WindPressureCoefficientValues"] = cp_calc(bldg_ratio, azimuth=azimuth, window_areas=window_areas, cp_eq=False)
            model["FenestrationSurface:Detailed"].update(hive_door)
        else:
            model["AirflowNetwork:MultiZone:WindPressureCoefficientValues"] = cp_calc(bldg_ratio, azimuth=azimuth, window_areas=window_areas, cp_eq=True)
        with open(SEED_DOOR_FILE, 'r') as file:
            seed_door = json.loads(file.read())
        model.update(seed_door)
    else:
        model["AirflowNetwork:MultiZone:WindPressureCoefficientValues"] = cp_calc(bldg_ratio, azimuth=azimuth, window_areas=window_areas, cp_eq=False)
    
    if eps:
        model["Construction"] = {
            "wall_construction": {
                "idf_max_extensible_fields": 0,
                "idf_max_fields": 3,
                "layer_2": "concrete",
                "outside_layer": "EPS"
            },
            "wall_construction_inverse": {
                "idf_max_extensible_fields": 0,
                "idf_max_fields": 3,
                "outside_layer": "concrete",
                "layer_2": "EPS"
            }
        }
    else:
        model["Construction"] = {
            "wall_construction": {
                "idf_max_extensible_fields": 0,
                "idf_max_fields": 2,
                "outside_layer": "concrete"
            },
            "wall_construction_inverse": {
                "idf_max_extensible_fields": 0,
                "idf_max_fields": 3,
                "outside_layer": "concrete"
            }
        }
        
    with open(input_file, 'r') as file:
        seed = json.loads(file.read())
        
    update(model, seed)
    
    with open(output, 'w') as file:
        file.write(json.dumps(model))
 
'''     
main(zone_area=21.4398, zone_ratio=0.6985559566, zone_height=2.5, azimuth=270,
    absorptance=.5, wall_u=4.083, wall_ct=165.6,
    ground=1, roof=1, shading=[.5,0,0,0.5], living_room = True,
    exp=[1,0,0,1], wwr=[0.0866425992,0,0,0.15503875], open_fac=[.45,0,0,.45], glass_fs=.87, 
    bldg_ratio=0.85, floor_height=0, door=False,
    input_file='seed.json' , output='hive_proto.epJSON')  #   3.87 x 5.54

main(exp=[0,0,0,0], shading=[0,0,0,0], wwr=[0,0,0,0], open_fac=[0,0,0,0], output= "hive_test.epJSON")  # (input_file='seed_single_U-conc-eps.json')
main(exp=[1,1,1,1], shading=[0,0,0,0], wwr=[1,0,0,0], open_fac=[.5,0,0,0], output= "ela_test.epJSON")  # (input_file='seed_single_U-conc-eps.json')
''' 
