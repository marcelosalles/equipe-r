#### Values of components' transmittance and thermal capacity ----------
    
def concrete_wall(wall_u, wall_ct, absorptance):
    # Creates the materials and construction objects using the 
    # CONCRETE+EPS wall approach
    
    ## absorptance - The value of the absorptace of walls.
    ## wall_u - The value of transmittance of the walls.
    ## wall_ct - The value of thermal capacity of the walls.
    
    # Returns a dictionary with the objects of the model.

    CONDUCTIVITY = 1.75    # concrete's condutivity {W/m-K}
    SPECIFIC_HEAT = 1    # concrete's specific heat {kJ/kg-K}
    DENSITY = 2200       # concrete's density {kg/m3}
    
    e_concrete = wall_ct/(SPECIFIC_HEAT*DENSITY)
    R_concrete = e_concrete/CONDUCTIVITY
    R_eps = (1-(.17+R_concrete)*wall_u)/wall_u
    eps = True
    if R_eps < 0.0001:
        # Condition to ignore EPS with insignificant R values.
        eps = False
        CONDUCTIVITY = (wall_u*e_concrete)/(1-.17*wall_u)
        print('EPS not used!')
        print('wall_u: ', wall_u, '\n', 'wall_ct: ', wall_ct) 

    concrete_objects = {}
    
    concrete_objects["Material"] = {
        "concrete": {
            "conductivity": CONDUCTIVITY,
            "thickness": e_concrete
        }
    }
    
    if eps:
        concrete_objects['Material:NoMass'] = {
            'EPS': {
                'thermal_resistance': R_eps,
                'solar_absorptance': absorptance
            }
        }    
        
        concrete_objects["Construction"] = {
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
        concrete_objects["Construction"] = {
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
    
    return(concrete_objects)
