import sympy as sp
from sympy import symbols, simplify, Eq
import math

Cd = .6
Cq = .001
L = 2.1*2+.9*2
rho = 1.200
A_adj = 1

def cp_calc(ratio=1, bldg_type = 'lowrise', azimuth=0, cp_eq=True, window_areas=[.5,0,0,0]):
    
    # print(ratio, bldg_type, azimuth, room_type, cp_eq, zone_x, zone_y, wwr, zn, corner_window)
    
    surfaces = ['side_0_coef','side_1_coef','side_2_coef','side_3_coef']
      
    WindPressureCoefficientValues = {}
        
    for FacadeNum in range(4):
        WindPressureCoefficientValues[surfaces[FacadeNum]] = {              
            "airflownetwork_multizone_windpressurecoefficientarray_name": "ventos",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 14
        }
        
        FacadeAng = (azimuth + FacadeNum * 90)%360
        if FacadeNum == 0 or FacadeNum == 2:
            SideRatio = 1.0 / ratio
        else:
            SideRatio = ratio
        
        SideRatioFac = math.log(SideRatio)
        
        for WindDirNum in range(12):
            WindAng = WindDirNum * 30.0
            IncAng = abs(WindAng - FacadeAng)
            
            if IncAng > 180.0:
                IncAng = 360.0 - IncAng
            
            IAng = int(IncAng / 30.0)
            DelAng = IncAng%30.0
            WtAng = 1.0 - DelAng / 30.0
            
            if bldg_type == 'lowrise':
                IncRad = IncAng * math.pi/180
                cos_IncRad_over_2 = math.cos(IncRad / 2.0)
                cp = 0.6 * math.log(1.248 - 0.703 * math.sin(IncRad / 2.0) - 1.175 * math.sin(IncRad)**2 +
                    0.131 * math.sin(2.0 * IncRad * SideRatioFac)**3 + 0.769 * cos_IncRad_over_2 +
                    0.07 * (SideRatioFac * math.sin(IncRad / 2.0))**2 + 0.717 * cos_IncRad_over_2**2)
            
            else:
                
                CPHighRiseWall = [
                    [0.60, 0.54, 0.23,  -0.25, -0.61, -0.55, -0.51, -0.55, -0.61, -0.25, 0.23,  0.54],
                    [0.60, 0.48, 0.04,  -0.56, -0.56, -0.42, -0.37, -0.42, -0.56, -0.56, 0.04,  0.48],
                    [0.60, 0.44, -0.26, -0.70, -0.53, -0.32, -0.22, -0.32, -0.53, -0.70, -0.26, 0.44]
                ]
                
                SR = min(max(SideRatio, 0.25), 4.0)
                if (SR >= 0.25 and SR < 1.0):
                    ISR = 0
                    WtSR = (1.0 - SR) / 0.75
                else:
                    ISR = 1
                    WtSR = (4.0 - SR) / 3.0
                    
                cp = WtSR * (WtAng * CPHighRiseWall[ISR][IAng] + (1.0 - WtAng) * CPHighRiseWall[ISR][IAng + 1]) + (1.0 - WtSR) * (WtAng * CPHighRiseWall[ISR + 1][IAng] + (1.0 - WtAng) * CPHighRiseWall[ISR + 1][IAng + 1])
                
            WindPressureCoefficientValues[surfaces[FacadeNum]]["wind_pressure_coefficient_value_"+str(WindDirNum+1)] = cp
    
    if cp_eq:
        WindPressureCoefficientValues = const_calc(WindPressureCoefficientValues, window_areas)
            
    return(WindPressureCoefficientValues)


def const_calc(WindPressureCoefficientValues, window_areas):
    
    new_cp_values = {             
        "airflownetwork_multizone_windpressurecoefficientarray_name": "ventos",
        "idf_max_extensible_fields": 0,
        "idf_max_fields": 14
    }
    
    Cjan_0, Cjan_1, Cjan_2, Cjan_3, Cjan_adj, Cpor, Cp_0, Cp_1, Cp_2, Cp_3, P_out, P_room, P_adj = symbols('Cjan_0, Cjan_1, Cjan_2, Cjan_3, Cjan_adj, Cpor, Cp_0, Cp_1, Cp_2, Cp_3, P_out, P_room, P_adj')

    p_room = Eq(-Cpor*(P_adj-P_room) + Cjan_0*(P_room-P_out*Cp_0) + Cjan_1*(P_room-P_out*Cp_1) + Cjan_2*(P_room-P_out*Cp_2) + Cjan_3*(P_room-P_out*Cp_3))
    
    p_room = sp.expand(sp.solve(p_room, P_room)[0])
    
    p_adj = Eq(Cjan_adj*(P_adj-P_out*Cp_3)-Cpor*(p_room-P_adj))
    p_adj = sp.expand(sp.solve(p_adj, P_adj)[0])
    
    #print(p_room,'\n',p_adj)
    
    Cjan_adj_value = Cd**2+A_adj**2*2*rho
    Cpor_value = Cq**2+L**2
        
    for wind_dir in range(1,13):
    
        subs_dic = {
                'P_out': 1,
                'Cjan_adj': Cjan_adj_value,
                'Cpor': Cpor_value,
                'Cp_0': WindPressureCoefficientValues['side_0_coef']["wind_pressure_coefficient_value_"+str(wind_dir)],
                'Cp_1': WindPressureCoefficientValues['side_1_coef']["wind_pressure_coefficient_value_"+str(wind_dir)],
                'Cp_2': WindPressureCoefficientValues['side_2_coef']["wind_pressure_coefficient_value_"+str(wind_dir)],
                'Cp_3': WindPressureCoefficientValues['side_3_coef']["wind_pressure_coefficient_value_"+str(wind_dir)]
            }
        
        for i in range(4):
            if window_areas[i] > 0:
                Cjan_value = Cd**2+window_areas[i]**2*2*rho
            else:
                Cjan_value = 0
            subs_dic['Cjan_'+str(i)] = Cjan_value
        
        const = p_adj.subs(subs_dic)
        #print(const)
        
        new_cp_values["wind_pressure_coefficient_value_"+str(wind_dir)] = float(const)
    
    WindPressureCoefficientValues['door_coef'] = new_cp_values
    
    return(WindPressureCoefficientValues)

'''
print(cp_calc(ratio=1, bldg_type = 'lowrise', azimuth=270, cp_eq=True, window_areas=[1.2,0,0,1.5]))
'''
