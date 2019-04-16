# setwd('/home/marcelo/Documents/equipe-r/idf_R01/')
# df <- read.csv('emsout.csv')
# df <- read.csv('rj_emsout.csv')

setwd('C:/Users/Matheus/Desktop/analise_dormitorios')
df <- read.csv('adapted_floor1_roof1.csv')

### DORM1 ----

## OCCUP(sala & dorm) = 0; VN = 0
check <- subset(df, df$DORMITORIO1.People.Occupant.Count....TimeStep. == 0 & df$SALA1.People.Occupant.Count....TimeStep. == 0)
unique(check$VN_DORM1.Schedule.Value....TimeStep.)

## OCCUP = 0; HVAC = 0
check <- subset(df, df$DORMITORIO1.People.Occupant.Count....TimeStep. == 0)
unique(check$HVAC_DORM1.Schedule.Value....TimeStep.)

## VN > 0; HVAC = 0; 
## HVAC > 0; VN = 0
nrow(subset(df, df$HVAC_DORM1.Schedule.Value....TimeStep. > 0 & df$VN_DORM1.Schedule.Value....TimeStep. > 0))

## OCCUP > 0; 16 < T < 26
nrow(subset(df, df$DORMITORIO1.People.Occupant.Count....TimeStep. > 0 & df$DORM1.Zone.Operative.Temperature..C..TimeStep. > 26))
# 5 timesteps no inicio da ocupacao, entao ok!
nrow(subset(df, df$DORMITORIO1.People.Occupant.Count....TimeStep. > 0 & df$DORM1.Zone.Operative.Temperature..C..TimeStep. < 16))
# conferindo com epw de RJ
check <- subset(df, df$DORMITORIO1.People.Occupant.Count....TimeStep. > 0 & df$DORM1.Zone.Operative.Temperature..C..TimeStep. > 26 &
                  df$HVAC_DORM1.Schedule.Value....TimeStep. == 0)  # 29 timesteps
max(check$DORM1.Zone.Mean.Air.Temperature..C..TimeStep.)
max(check$DORM1.Zone.Operative.Temperature..C..TimeStep.)

check <- subset(df, df$DORMITORIO1.People.Occupant.Count....TimeStep. > 0 & df$DORM1.Zone.Operative.Temperature..C..TimeStep. > 26 &
                  df$HVAC_DORM1.Schedule.Value....TimeStep. > 0)  # 232 timesteps
max(check$DORM1.Zone.Mean.Air.Temperature..C..TimeStep.)
max(check$DORM1.Zone.Operative.Temperature..C..TimeStep.)

## HVAC > 0; 18 < T < 26
nrow(subset(df, df$HVAC_DORM1.Schedule.Value....TimeStep. > 0 & df$DORM1.Zone.Operative.Temperature..C..TimeStep. > 26))
nrow(subset(df, df$HVAC_DORM1.Schedule.Value....TimeStep. > 0 & df$DORM1.Zone.Operative.Temperature..C..TimeStep. < 18))
# HVAC funciona baseado na T_ar, e nao T_op. Por isso 480 timesteps tem T_op inferior a 18.
# Ao checar com T_ar:
nrow(subset(df, df$HVAC_DORM1.Schedule.Value....TimeStep. > 0 & df$DORM1.Zone.Mean.Air.Temperature..C..TimeStep. < 18))
# 222 timesteps ainda estao com T_ar abaixo de 18
check <- subset(df, df$HVAC_DORM1.Schedule.Value....TimeStep. > 0 & df$DORM1.Zone.Mean.Air.Temperature..C..TimeStep. < 18)
min(check$DORM1.Zone.Mean.Air.Temperature..C..TimeStep.)
# Na pratica, eh um problema de arredondamento ou algo do genero, pois o min = 18
nrow(subset(df, df$HVAC_DORM1.Schedule.Value....TimeStep. > 0 & df$DORM1.Zone.Mean.Air.Temperature..C..TimeStep. < 17.999))
# suspeita confirmada!

## VN = 0; OPEN_FAC = 0
check <- subset(df, df$VN_DORM1.Schedule.Value....TimeStep. == 0)
unique(check$PORTAINT_DORM1SALA.AFN.Surface.Venting.Window.or.Door.Opening.Factor....TimeStep.)
unique(check$JANQUARTO1_SUL.AFN.Surface.Venting.Window.or.Door.Opening.Factor....TimeStep.)

## HVAC = 0; IDEAL_LOADS = 0
check <- subset(df, df$HVAC_DORM1.Schedule.Value....TimeStep. == 0)
unique(check$DORM1.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Supply.Air.Total.Cooling.Energy..J..TimeStep.)
unique(check$DORM1.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.)
unique(check$DORM1.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Supply.Air.Total.Heating.Energy..J..TimeStep.)
unique(check$DORM1.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Heating.Energy..J..TimeStep.)

### DORM2 ----

## OCCUP(sala & dorm) = 0; VN = 0
check <- subset(df, df$DORMITORIO2.People.Occupant.Count....TimeStep. == 0 & df$SALA1.People.Occupant.Count....TimeStep. == 0)
unique(check$VN_DORM2.Schedule.Value....TimeStep.)

## OCCUP = 0; HVAC = 0
check <- subset(df, df$DORMITORIO2.People.Occupant.Count....TimeStep. == 0)
unique(check$HVAC_DORM2.Schedule.Value....TimeStep.)

## VN > 0; HVAC = 0; 
## HVAC > 0; VN = 0
nrow(subset(df, df$HVAC_DORM2.Schedule.Value....TimeStep. > 0 & df$VN_DORM2.Schedule.Value....TimeStep. > 0))

## OCCUP > 0; 16 < T < 26
nrow(subset(df, df$DORMITORIO2.People.Occupant.Count....TimeStep. > 0 & df$DORM2.Zone.Operative.Temperature..C..TimeStep. > 26))
# 6 timesteps, entao ok!
nrow(subset(df, df$DORMITORIO2.People.Occupant.Count....TimeStep. > 0 & df$DORM2.Zone.Operative.Temperature..C..TimeStep. < 16))
# 1 timestep
# conferindo com epw de RJ
check <- subset(df, df$DORMITORIO2.People.Occupant.Count....TimeStep. > 0 & df$DORM2.Zone.Operative.Temperature..C..TimeStep. > 26 &
                  df$HVAC_DORM2.Schedule.Value....TimeStep. == 0)  # 29 timesteps
max(check$DORM2.Zone.Mean.Air.Temperature..C..TimeStep.)
max(check$DORM2.Zone.Operative.Temperature..C..TimeStep.)

check <- subset(df, df$DORMITORIO2.People.Occupant.Count....TimeStep. > 0 & df$DORM2.Zone.Operative.Temperature..C..TimeStep. > 26 &
                  df$HVAC_DORM2.Schedule.Value....TimeStep. > 0)  # 232 timesteps
max(check$DORM2.Zone.Mean.Air.Temperature..C..TimeStep.)
max(check$DORM2.Zone.Operative.Temperature..C..TimeStep.)

## HVAC > 0; 18 < T < 26
nrow(subset(df, df$HVAC_DORM2.Schedule.Value....TimeStep. > 0 & df$DORM2.Zone.Operative.Temperature..C..TimeStep. > 26))
nrow(subset(df, df$HVAC_DORM2.Schedule.Value....TimeStep. > 0 & df$DORM2.Zone.Operative.Temperature..C..TimeStep. < 18))
# HVAC funciona baseado na T_ar, e nao T_op. Por isso 480 timesteps tem T_op inferior a 18.
# Ao checar com T_ar:
nrow(subset(df, df$HVAC_DORM2.Schedule.Value....TimeStep. > 0 & df$DORM2.Zone.Mean.Air.Temperature..C..TimeStep. < 18))
# 202 timesteps ainda estao com T_ar abaixo de 18
check <- subset(df, df$HVAC_DORM2.Schedule.Value....TimeStep. > 0 & df$DORM2.Zone.Mean.Air.Temperature..C..TimeStep. < 18)
min(check$DORM2.Zone.Mean.Air.Temperature..C..TimeStep.)
# Na pratica, eh um problema de arredondamento ou algo do genero, pois o min = 18
nrow(subset(df, df$HVAC_DORM2.Schedule.Value....TimeStep. > 0 & df$DORM2.Zone.Mean.Air.Temperature..C..TimeStep. < 17.999))
# suspeita confirmada!

## VN = 0; OPEN_FAC = 0
check <- subset(df, df$VN_DORM2.Schedule.Value....TimeStep. == 0)
unique(check$PORTAINT_DORM2SALA.AFN.Surface.Venting.Window.or.Door.Opening.Factor....TimeStep.)
unique(check$JANQUARTO2_LESTE.AFN.Surface.Venting.Window.or.Door.Opening.Factor....TimeStep.)

## HVAC = 0; IDEAL_LOADS = 0
check <- subset(df, df$HVAC_DORM2.Schedule.Value....TimeStep. == 0)
unique(check$DORM2.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Supply.Air.Total.Cooling.Energy..J..TimeStep.)
unique(check$DORM2.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Supply.Air.Total.Heating.Energy..J..TimeStep.)
unique(check$DORM2.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.)
unique(check$DORM2.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Heating.Energy..J..TimeStep.)

### SALA ----

## OCCUP(sala & dorm) = 0; VN = 0
check <- subset(df, df$DORMITORIO1.People.Occupant.Count....TimeStep. == 0 & df$SALA1.People.Occupant.Count....TimeStep. == 0)
unique(check$VN_SALA.Schedule.Value....TimeStep.)

## OCCUP = 0; HVAC = 0
check <- subset(df, df$SALA1.People.Occupant.Count....TimeStep. == 0)
unique(check$HVAC_SALA.Schedule.Value....TimeStep.)

## VN > 0; HVAC = 0; 
## HVAC > 0; VN = 0
nrow(subset(df, df$HVAC_SALA.Schedule.Value....TimeStep. > 0 & df$VN_SALA.Schedule.Value....TimeStep. > 0))

## OCCUP > 0; 16 < T < 26
nrow(subset(df, df$SALA1.People.Occupant.Count....TimeStep. > 0 & df$SALA.Zone.Operative.Temperature..C..TimeStep. > 26))
nrow(subset(df, df$SALA1.People.Occupant.Count....TimeStep. > 0 & df$SALA.Zone.Operative.Temperature..C..TimeStep. < 16))
# Apesar de 987 timesteps com T_op > 26, sao quase que na totalidade timesteps onde HVAC esta ligado e T_ar < 26
check <- subset(df, df$SALA1.People.Occupant.Count....TimeStep. > 0 & df$SALA.Zone.Operative.Temperature..C..TimeStep. > 26)
nrow(subset(check, check$HVAC_SALA.Schedule.Value....TimeStep. == 0))
nrow(subset(check, check$SALA.Zone.Mean.Air.Temperature..C..TimeStep. > 26))

## HVAC > 0; 18 < T < 26
nrow(subset(df, df$HVAC_SALA.Schedule.Value....TimeStep. > 0 & df$SALA.Zone.Operative.Temperature..C..TimeStep. > 26))
nrow(subset(df, df$HVAC_SALA.Schedule.Value....TimeStep. > 0 & df$SALA.Zone.Operative.Temperature..C..TimeStep. < 18))
# Analise analoga a de cima
check <- subset(df, df$HVAC_SALA.Schedule.Value....TimeStep. > 0 & df$SALA.Zone.Operative.Temperature..C..TimeStep. > 26)
nrow(subset(check, check$SALA.Zone.Mean.Air.Temperature..C..TimeStep. > 26))
check <- subset(df, df$HVAC_SALA.Schedule.Value....TimeStep. > 0 & df$SALA.Zone.Operative.Temperature..C..TimeStep. < 18)
nrow(subset(check, check$SALA.Zone.Mean.Air.Temperature..C..TimeStep. < 17.999))

## VN = 0; OPEN_FAC = 0
check <- subset(df, df$VN_SALA.Schedule.Value....TimeStep. == 0)
unique(check$PORTAINT_DORM1SALA.AFN.Surface.Venting.Window.or.Door.Opening.Factor....TimeStep.)
unique(check$PORTAINT_DORM2SALA.AFN.Surface.Venting.Window.or.Door.Opening.Factor....TimeStep.)
unique(check$JANSALA_OESTE.AFN.Surface.Venting.Window.or.Door.Opening.Factor....TimeStep.)
unique(check$JANSALA_SUL.AFN.Surface.Venting.Window.or.Door.Opening.Factor....TimeStep.)
unique(check$PORTAINT_BWCSALA.AFN.Surface.Venting.Window.or.Door.Opening.Factor....TimeStep.)

## HVAC = 0; IDEAL_LOADS = 0
check <- subset(df, df$HVAC_SALA.Schedule.Value....TimeStep. == 0)
unique(check$SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Supply.Air.Total.Cooling.Energy..J..TimeStep.)
unique(check$SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Supply.Air.Total.Heating.Energy..J..TimeStep.)
unique(check$SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.)
unique(check$SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Heating.Energy..J..TimeStep.)

### SINGLE ----

# df <- read.csv('dorm1out.csv')
# df <- read.csv('dorm2out.csv')
df <- read.csv('dorm1_hive_floor1_roof1.csv')

## OCCUP = 0; HVAC = 0
check <- subset(df, df$PEOPLE.People.Occupant.Count....TimeStep. == 0)
unique(check$HVAC.Schedule.Value....TimeStep.)

## VN > 0; HVAC = 0; 
## HVAC > 0; VN = 0
nrow(subset(df, df$HVAC.Schedule.Value....TimeStep. > 0 & df$VN.Schedule.Value....TimeStep. > 0))

## OCCUP > 0; 16 < T < 26
nrow(subset(df, df$PEOPLE.People.Occupant.Count....TimeStep. > 0 & df$ROOM.Zone.Operative.Temperature..C..TimeStep. > 26))
nrow(subset(df, df$PEOPLE.People.Occupant.Count....TimeStep. > 0 & df$ROOM.Zone.Operative.Temperature..C..TimeStep. < 16))
# Apesar de 987 timesteps com T_op > 26, sao quase que na totalidade timesteps onde HVAC esta ligado e T_ar < 26
check <- subset(df, df$PEOPLE.People.Occupant.Count....TimeStep. > 0 & df$ROOM.Zone.Operative.Temperature..C..TimeStep. > 26)
nrow(subset(check, check$HVAC.Schedule.Value....TimeStep. == 0))
nrow(subset(check, check$ROOM.Zone.Mean.Air.Temperature..C..TimeStep. > 26))


## HVAC > 0; 18 < T < 26
nrow(subset(df, df$HVAC.Schedule.Value....TimeStep. > 0 & df$ROOM.Zone.Operative.Temperature..C..TimeStep. > 26))
nrow(subset(df, df$HVAC.Schedule.Value....TimeStep. > 0 & df$ROOM.Zone.Operative.Temperature..C..TimeStep. < 18))
# Analise analoga a de cima
check <- subset(df, df$HVAC.Schedule.Value....TimeStep. > 0 & df$ROOM.Zone.Operative.Temperature..C..TimeStep. > 26)
nrow(subset(check, check$ROOM.Zone.Mean.Air.Temperature..C..TimeStep. > 26))
check <- subset(df, df$HVAC.Schedule.Value....TimeStep. > 0 & df$ROOM.Zone.Operative.Temperature..C..TimeStep. < 18)
nrow(subset(check, check$ROOM.Zone.Mean.Air.Temperature..C..TimeStep. < 17.999))


## VN = 0; OPEN_FAC = 0
check <- subset(df, df$VN.Schedule.Value....TimeStep. == 0)

unique(check$WINDOW_1.AFN.Surface.Venting.Window.or.Door.Opening.Factor....TimeStep.)
unique(check$DOOR.AFN.Surface.Venting.Window.or.Door.Opening.Factor....TimeStep.)

## HVAC = 0; IDEAL_LOADS = 0
check <- subset(df, df$HVAC.Schedule.Value....TimeStep. == 0)
unique(check$ROOM.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Heating.Energy..J..TimeStep.)
unique(check$ROOM.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.)


### ACH

mean(ach_room$ROOM.AFN.Zone.Infiltration.Air.Change.Rate..ach..TimeStep.)
quantile(ach_room$ROOM.AFN.Zone.Infiltration.Air.Change.Rate..ach..TimeStep.,.05)
mean(ach_dorm2$DORM2.AFN.Zone.Infiltration.Air.Change.Rate..ach..TimeStep.)
quantile(ach_dorm2$DORM2.AFN.Zone.Infiltration.Air.Change.Rate..ach..TimeStep.,.05)
mean(ach_sala$SALA.AFN.Zone.Infiltration.Air.Change.Rate..ach..TimeStep.)
quantile(ach_sala$SALA.AFN.Zone.Infiltration.Air.Change.Rate..ach..TimeStep.,.05)
