
library(ggplot2)

setwd('/home/marcelo/Documents/equipe-r/analise_climas/')
#
# REF ----
#00
df_ref_PA_00 <- read.csv('PA/ref_floor0_roof0_PAout.csv')
df_ref_SM_00 <- read.csv('SM/ref_floor0_roof0_SMout.csv')
df_ref_SP_00 <- read.csv('SP/ref_floor0_roof0_SPout.csv')
df_ref_RJ_00 <- read.csv('RJ/ref_floor0_roof0_RJout.csv')

#11
df_ref_PA_11 <- read.csv('PA/ref_floor1_roof1_PAout.csv')
df_ref_SM_11 <- read.csv('SM/ref_floor1_roof1_SMout.csv')
df_ref_SP_11 <- read.csv('SP/ref_floor1_roof1_SPout.csv')
df_ref_RJ_11 <- read.csv('RJ/ref_floor1_roof1_RJout.csv')

#10
df_ref_PA_10 <- read.csv('PA/ref_floor0_roof1_PAout.csv')
df_ref_SM_10 <- read.csv('SM/ref_floor0_roof1_SMout.csv')
df_ref_SP_10 <- read.csv('SP/ref_floor0_roof1_SPout.csv')
df_ref_RJ_10 <- read.csv('RJ/ref_floor0_roof1_RJout.csv')

#01
df_ref_PA_01 <- read.csv('PA/ref_floor1_roof0_PAout.csv')
df_ref_SM_01 <- read.csv('SM/ref_floor1_roof0_SMout.csv')
df_ref_SP_01 <- read.csv('SP/ref_floor1_roof0_SPout.csv')
df_ref_RJ_01 <- read.csv('RJ/ref_floor1_roof0_RJout.csv')

#pilotis
df_ref_PA_pil <- read.csv('PA/ref_pilotis_roof0_PAout.csv')
df_ref_SM_pil <- read.csv('SM/ref_pilotis_roof0_SMout.csv')
df_ref_SP_pil <- read.csv('SP/ref_pilotis_roof0_SPout.csv')
df_ref_RJ_pil <- read.csv('RJ/ref_pilotis_roof0_RJout.csv')

# ADAPTED ----
#00
df_adap_PA_00 <- read.csv('PA/adapted_floor0_roof0_PAout.csv')
df_adap_SM_00 <- read.csv('SM/adapted_floor0_roof0_SMout.csv')
df_adap_SP_00 <- read.csv('SP/adapted_floor0_roof0_SPout.csv')
df_adap_RJ_00 <- read.csv('RJ/adapted_floor0_roof0_RJout.csv')
#11
df_adap_PA_11 <- read.csv('PA/adapted_floor1_roof1_PAout.csv')
df_adap_SM_11 <- read.csv('SM/adapted_floor1_roof1_SMout.csv')
df_adap_SP_11 <- read.csv('SP/adapted_floor1_roof1_SPout.csv')
df_adap_RJ_11 <- read.csv('RJ/adapted_floor1_roof1_RJout.csv')
#10
df_adap_PA_10 <- read.csv('PA/adapted_floor0_roof1_PAout.csv')
df_adap_SM_10 <- read.csv('SM/adapted_floor0_roof1_SMout.csv')
df_adap_SP_10 <- read.csv('SP/adapted_floor0_roof1_SPout.csv')
df_adap_RJ_10 <- read.csv('RJ/adapted_floor0_roof1_RJout.csv')
#01
df_adap_PA_01 <- read.csv('PA/adapted_floor1_roof0_PAout.csv')
df_adap_SM_01 <- read.csv('SM/adapted_floor1_roof0_SMout.csv')
df_adap_SP_01 <- read.csv('SP/adapted_floor1_roof0_SPout.csv')
df_adap_RJ_01 <- read.csv('RJ/adapted_floor1_roof0_RJout.csv')
#pil
df_adap_PA_pil <- read.csv('PA/adapted_pilotis_roof0_PAout.csv')
df_adap_SM_pil <- read.csv('SM/adapted_pilotis_roof0_SMout.csv')
df_adap_SP_pil <- read.csv('SP/adapted_pilotis_roof0_SPout.csv')
df_adap_RJ_pil <- read.csv('RJ/adapted_pilotis_roof0_RJout.csv')

# DOUBLE ----
#00
df_sin_PA_00 <- read.csv('PA/double_floor0_roof0_PAout.csv')
df_sin_SM_00 <- read.csv('SM/double_floor0_roof0_SMout.csv')
df_sin_SP_00 <- read.csv('SP/double_floor0_roof0_SPout.csv')
df_sin_RJ_00 <- read.csv('RJ/double_floor0_roof0_RJout.csv')
#11
df_sin_PA_11 <- read.csv('PA/double_floor1_roof1_PAout.csv')
df_sin_SM_11 <- read.csv('SM/double_floor1_roof1_SMout.csv')
df_sin_SP_11 <- read.csv('SP/double_floor1_roof1_SPout.csv')
df_sin_RJ_11 <- read.csv('RJ/double_floor1_roof1_RJout.csv')
#10
df_sin_PA_10 <- read.csv('PA/double_floor0_roof1_PAout.csv')
df_sin_SM_10 <- read.csv('SM/double_floor0_roof1_SMout.csv')
df_sin_SP_10 <- read.csv('SP/double_floor0_roof1_SPout.csv')
df_sin_RJ_10 <- read.csv('RJ/double_floor0_roof1_RJout.csv')
#01
df_sin_PA_01 <- read.csv('PA/double_floor1_roof0_PAout.csv')
df_sin_SM_01 <- read.csv('SM/double_floor1_roof0_SMout.csv')
df_sin_SP_01 <- read.csv('SP/double_floor1_roof0_SPout.csv')
df_sin_RJ_01 <- read.csv('RJ/double_floor1_roof0_RJout.csv')
#pil
df_sin_PA_pil <- read.csv('PA/double_pilotis_roof0_PAout.csv')
df_sin_SM_pil <- read.csv('SM/double_pilotis_roof0_SMout.csv')
df_sin_SP_pil <- read.csv('SP/double_pilotis_roof0_SPout.csv')
df_sin_RJ_pil <- read.csv('RJ/double_pilotis_roof0_RJout.csv')
# HIVE ----
#00
df_sin_PA_00 <- read.csv('PA/hive_floor0_roof0_PAout.csv')
df_sin_SM_00 <- read.csv('SM/hive_floor0_roof0_SMout.csv')
df_sin_SP_00 <- read.csv('SP/hive_floor0_roof0_SPout.csv')
df_sin_RJ_00 <- read.csv('RJ/hive_floor0_roof0_RJout.csv')
#11
df_sin_PA_11 <- read.csv('PA/hive_floor1_roof1_PAout.csv')
df_sin_SM_11 <- read.csv('SM/hive_floor1_roof1_SMout.csv')
df_sin_SP_11 <- read.csv('SP/hive_floor1_roof1_SPout.csv')
df_sin_RJ_11 <- read.csv('RJ/hive_floor1_roof1_RJout.csv')
#10
df_sin_PA_10 <- read.csv('PA/hive_floor0_roof1_PAout.csv')
df_sin_SM_10 <- read.csv('SM/hive_floor0_roof1_SMout.csv')
df_sin_SP_10 <- read.csv('SP/hive_floor0_roof1_SPout.csv')
df_sin_RJ_10 <- read.csv('RJ/hive_floor0_roof1_RJout.csv')
#01
df_sin_PA_01 <- read.csv('PA/hive_floor1_roof0_PAout.csv')
df_sin_SM_01 <- read.csv('SM/hive_floor1_roof0_SMout.csv')
df_sin_SP_01 <- read.csv('SP/hive_floor1_roof0_SPout.csv')
df_sin_RJ_01 <- read.csv('RJ/hive_floor1_roof0_RJout.csv')
#pil
df_sin_PA_pil <- read.csv('PA/hive_pilotis_roof0_PAout.csv')
df_sin_SM_pil <- read.csv('SM/hive_pilotis_roof0_SMout.csv')
df_sin_SP_pil <- read.csv('SP/hive_pilotis_roof0_SPout.csv')
df_sin_RJ_pil <- read.csv('RJ/hive_pilotis_roof0_RJout.csv')
# DOUOBLE TIJOLO ----
#11
df_doub_PA_11 <- read.csv('PA/double_floor1_roof1_tijolo_PAout.csv')
df_doub_SM_11 <- read.csv('SM/double_floor1_roof1_tijolo_SMout.csv')
df_doub_SP_11 <- read.csv('SP/double_floor1_roof1_tijolo_SPout.csv')
df_doub_RJ_11 <- read.csv('RJ/double_floor1_roof1_tijolo_RJout.csv')
#00
df_doub_PA_00 <- read.csv('PA/double_floor0_roof0_tijolo_PAout.csv')
df_doub_SM_00 <- read.csv('SM/double_floor0_roof0_tijolo_SMout.csv')
df_doub_SP_00 <- read.csv('SP/double_floor0_roof0_tijolo_SPout.csv')
df_doub_RJ_00 <- read.csv('RJ/double_floor0_roof0_tijolo_RJout.csv')
#10
df_doub_PA_10 <- read.csv('PA/double_floor0_roof1_tijolo_PAout.csv')
df_doub_SM_10 <- read.csv('SM/double_floor0_roof1_tijolo_SMout.csv')
df_doub_SP_10 <- read.csv('SP/double_floor0_roof1_tijolo_SPout.csv')
df_doub_RJ_10 <- read.csv('RJ/double_floor0_roof1_tijolo_RJout.csv')
#01
df_doub_PA_01 <- read.csv('PA/double_floor1_roof0_tijolo_PAout.csv')
df_doub_SM_01 <- read.csv('SM/double_floor1_roof0_tijolo_SMout.csv')
df_doub_SP_01 <- read.csv('SP/double_floor1_roof0_tijolo_SPout.csv')
df_doub_RJ_01 <- read.csv('RJ/double_floor1_roof0_tijolo_RJout.csv')
#pil
df_doub_PA_pil <- read.csv('PA/double_pilotis_roof0_tijolo_PAout.csv')
df_doub_SM_pil <- read.csv('SM/double_pilotis_roof0_tijolo_SMout.csv')
df_doub_SP_pil <- read.csv('SP/double_pilotis_roof0_tijolo_SPout.csv')
df_doub_RJ_pil <- read.csv('RJ/double_pilotis_roof0_tijolo_RJout.csv')
# HIVE TIJOLO ----
#11
df_hive_PA_11 <- read.csv('PA/hive_floor1_roof1_tijolo_PAout.csv')
df_hive_SM_11 <- read.csv('SM/hive_floor1_roof1_tijolo_SMout.csv')
df_hive_SP_11 <- read.csv('SP/hive_floor1_roof1_tijolo_SPout.csv')
df_hive_RJ_11 <- read.csv('RJ/hive_floor1_roof1_tijolo_RJout.csv')
#00
df_hive_PA_00 <- read.csv('PA/hive_floor0_roof0_tijolo_PAout.csv')
df_hive_SM_00 <- read.csv('SM/hive_floor0_roof0_tijolo_SMout.csv')
df_hive_SP_00 <- read.csv('SP/hive_floor0_roof0_tijolo_SPout.csv')
df_hive_RJ_00 <- read.csv('RJ/hive_floor0_roof0_tijolo_RJout.csv')
#10
df_hive_PA_10 <- read.csv('PA/hive_floor0_roof1_tijolo_PAout.csv')
df_hive_SM_10 <- read.csv('SM/hive_floor0_roof1_tijolo_SMout.csv')
df_hive_SP_10 <- read.csv('SP/hive_floor0_roof1_tijolo_SPout.csv')
df_hive_RJ_10 <- read.csv('RJ/hive_floor0_roof1_tijolo_RJout.csv')
#01
df_hive_PA_01 <- read.csv('PA/hive_floor1_roof0_tijolo_PAout.csv')
df_hive_SM_01 <- read.csv('SM/hive_floor1_roof0_tijolo_SMout.csv')
df_hive_SP_01 <- read.csv('SP/hive_floor1_roof0_tijolo_SPout.csv')
df_hive_RJ_01 <- read.csv('RJ/hive_floor1_roof0_tijolo_RJout.csv')
#pil
df_hive_PA_pil <- read.csv('PA/hive_pilotis_roof0_tijolo_PAout.csv')
df_hive_SM_pil <- read.csv('SM/hive_pilotis_roof0_tijolo_SMout.csv')
df_hive_SP_pil <- read.csv('SP/hive_pilotis_roof0_tijolo_SPout.csv')
df_hive_RJ_pil <- read.csv('RJ/hive_pilotis_roof0_tijolo_RJout.csv')
#
# TEMP OP----

# PARA TESTE
# ----- #
df_sin_PA <- df_doub_PA_00
df_sin_SM <- df_doub_SM_00
df_sin_SP <- df_doub_SP_00
df_sin_RJ <- df_doub_RJ_00
df_ref_PA <- df_ref_PA_00
df_ref_SM <- df_ref_SM_00
df_ref_SP <- df_ref_SP_00
df_ref_RJ <- df_ref_RJ_00
# ----- #

diff_temp_PA <- df_ref_PA[df_ref_PA$SALA1.People.Occupant.Count....TimeStep. > 0,'SALA.Zone.Operative.Temperature..C..TimeStep.'] - df_sin_PA$SINGLEZONE.Zone.Operative.Temperature..C..TimeStep.[df_sin_PA$SALA1.People.Occupant.Count....TimeStep. > 0]
diff_temp_SM <- df_ref_SM[df_ref_SM$SALA1.People.Occupant.Count....TimeStep. > 0,'SALA.Zone.Operative.Temperature..C..TimeStep.'] - df_sin_SM$SINGLEZONE.Zone.Operative.Temperature..C..TimeStep.[df_sin_SM$SALA1.People.Occupant.Count....TimeStep. > 0]
diff_temp_SP <- df_ref_SP[df_ref_SP$SALA1.People.Occupant.Count....TimeStep. > 0,'SALA.Zone.Operative.Temperature..C..TimeStep.'] - df_sin_SP$SINGLEZONE.Zone.Operative.Temperature..C..TimeSte[df_sin_SP$SALA1.People.Occupant.Count....TimeStep. > 0]
diff_temp_RJ <- df_ref_RJ[df_ref_RJ$SALA1.People.Occupant.Count....TimeStep. > 0,'SALA.Zone.Operative.Temperature..C..TimeStep.'] - df_sin_RJ$SINGLEZONE.Zone.Operative.Temperature..C..TimeStep[df_sin_RJ$SALA1.People.Occupant.Count....TimeStep. > 0]

meandif_PA <- mean(diff_temp_PA)
mediandif_PA <- median(diff_temp_PA)
mindif_PA <- min(diff_temp_PA)
maxdif_PA <- max(diff_temp_PA)
maxabs_PA <- max(abs(mindif_PA),abs(maxdif_PA))
tile5dif_PA <- quantile(diff_temp_PA,.05)
tile95dif_PA <- quantile(diff_temp_PA,.95)

meandif_SM <- mean(diff_temp_SM)
mediandif_SM <- median(diff_temp_SM)
mindif_SM <- min(diff_temp_SM)
maxdif_SM <- max(diff_temp_SM)
maxabs_SM <- max(abs(mindif_SM),abs(maxdif_SM))
tile5dif_SM <- quantile(diff_temp_SM,.05)
tile95dif_SM <- quantile(diff_temp_SM,.95)

meandif_SP <- mean(diff_temp_SP)
mediandif_SP <- median(diff_temp_SP)
mindif_SP <- min(diff_temp_SP)
maxdif_SP <- max(diff_temp_SP)
maxabs_SP <- max(abs(mindif_SP),abs(maxdif_SP))
tile5dif_SP <- quantile(diff_temp_SP,.05)
tile95dif_SP <- quantile(diff_temp_SP,.95)

meandif_RJ <- mean(diff_temp_RJ)
mediandif_RJ <- median(diff_temp_RJ)
mindif_RJ <- min(diff_temp_RJ)
maxdif_RJ <- max(diff_temp_RJ)
maxabs_RJ <- max(abs(mindif_RJ),abs(maxdif_RJ))
tile5dif_RJ <- quantile(diff_temp_RJ,.05)
tile95dif_RJ <- quantile(diff_temp_RJ,.95)

ggplot() +
  geom_histogram(aes(diff_temp_PA),fill='red',alpha=.3,binwidth = .005) +
  geom_histogram(aes(diff_temp_SM),fill='blue',alpha=.3,binwidth = .005) +
  geom_histogram(aes(diff_temp_SP),fill='darkgreen',alpha=.3,binwidth = .005) +
  geom_histogram(aes(diff_temp_RJ),fill='orange',alpha=.3,binwidth = .005)
  #geom_histogram(aes(diff_temp)) +
  #ggtitle(title[2]) +
  ggtitle(paste('Diferenças',title_ref,'e',title_sin)) #+
  # ylab('Timesteps') +
  # xlab('Diferença de Temperatura Opertativa (°C)') +
  # annotate("text", x = textx, y = texty, label = paste("Média =",round(meandif,2),'°C')) +
  # annotate("text", x = textx*.98, y = texty*.95, label = paste("Mediana =",round(mediandif,2),'°C')) +
  # annotate("text", x = textx*.93, y = texty*.9, label = paste("Maior dif. abs =",round(maxabs,2),'°C')) +
  # annotate("text", x = textx*.92, y = texty*.85, label = paste("Percentil 5% =",round(tile5dif,2),'°C')) +
  # annotate("text", x = textx*.92, y = texty*.8, label = paste("Percentil 95% =",round(tile95dif,2),'°C'))

# IDEAL LOADS
diff_loads_PA <- (df_ref_PA$SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.[
  df_ref_PA$SALA1.People.Occupant.Count....TimeStep. > 0
  ] - df_sin_PA$SINGLEZONE.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.[
    df_sin_PA$SALA1.People.Occupant.Count....TimeStep. > 0
    ])/(area*3600)


sum(df_sin_PA$SINGLEZONE.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.)/sum(df_ref_PA$SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.)

meandif_PA <- mean(diff_loads_PA)
mediandif_PA <- median(diff_loads_PA)
mindif_PA <- min(diff_loads_PA)
maxdif_PA <- max(diff_loads_PA)
maxabs_PA <- max(abs(mindif_PA),abs(maxdif_PA))
tile5dif_PA <- quantile(diff_loads_PA,.05)
tile95dif_PA <- quantile(diff_loads_PA,.9)
cooling_ref_PA <- sum(df_ref_PA[,loads_zone])/(area*3600000)
cooling_sin_PA <- sum(df_sin_PA$SINGLEZONE.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.)/(area*3600000)

diff_loads_SM <- (df_ref_SM$SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.[
  df_ref_SM$SALA1.People.Occupant.Count....TimeStep. > 0
  ] - df_sin_SM$SINGLEZONE.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.[
    df_sin_SM$SALA1.People.Occupant.Count....TimeStep. > 0
    ])/(area*3600)


sum(df_sin_SM$SINGLEZONE.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.)/sum(df_ref_SM$SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.)

meandif_SM <- mean(diff_loads_SM)
mediandif_SM <- median(diff_loads_SM)
mindif_SM <- min(diff_loads_SM)
maxdif_SM <- max(diff_loads_SM)
maxabs_SM <- max(abs(mindif_SM),abs(maxdif_SM))
tile5dif_SM <- quantile(diff_loads_SM,.05)
tile95dif_SM <- quantile(diff_loads_SM,.9)
cooling_ref_SM <- sum(df_ref_SM[,loads_zone])/(area*3600000)
cooling_sin_SM <- sum(df_sin_SM$SINGLEZONE.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.)/(area*3600000)

diff_loads_SP <- (df_ref_SP$SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.[
  df_ref_SP$SALA1.People.Occupant.Count....TimeStep. > 0
  ] - df_sin_SP$SINGLEZONE.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.[
    df_sin_SP$SALA1.People.Occupant.Count....TimeStep. > 0
    ])/(area*3600)


sum(df_sin_SP$SINGLEZONE.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.)/sum(df_ref_SP$SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.)

meandif_SP <- mean(diff_loads_SP)
mediandif_SP <- median(diff_loads_SP)
mindif_SP <- min(diff_loads_SP)
maxdif_SP <- max(diff_loads_SP)
maxabs_SP <- max(abs(mindif_SP),abs(maxdif_SP))
tile5dif_SP <- quantile(diff_loads_SP,.05)
tile95dif_SP <- quantile(diff_loads_SP,.9)
cooling_ref_SP <- sum(df_ref_SP[,loads_zone])/(area*3600000)
cooling_sin_SP <- sum(df_sin_SP$SINGLEZONE.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.)/(area*3600000)

diff_loads_RJ <- (df_ref_RJ$SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.[
  df_ref_RJ$SALA1.People.Occupant.Count....TimeStep. > 0
  ] - df_sin_RJ$SINGLEZONE.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.[
    df_sin_RJ$SALA1.People.Occupant.Count....TimeStep. > 0
    ])/(area*3600)


sum(df_sin_RJ$SINGLEZONE.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.)/sum(df_ref_RJ$SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.)

meandif_RJ <- mean(diff_loads_RJ)
mediandif_RJ <- median(diff_loads_RJ)
mindif_RJ <- min(diff_loads_RJ)
maxdif_RJ <- max(diff_loads_RJ)
maxabs_RJ <- max(abs(mindif_RJ),abs(maxdif_RJ))
tile5dif_RJ <- quantile(diff_loads_RJ,.05)
tile95dif_RJ <- quantile(diff_loads_RJ,.9)
cooling_ref_RJ <- sum(df_ref_RJ[,loads_zone])/(area*3600000)
cooling_sin_RJ <- sum(df_sin_RJ$SINGLEZONE.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.)/(area*3600000)

# DIF RELATIVA ----

comfcount <- function(df, case, t_low=18, t_upp=26){
  if(case=="ref"){
    zone_name <- "SALA"
  }else{
    zone_name <- "SINGLEZONE"
  }
  comf_vec <- ifelse(df[,'SALA1.People.Occupant.Count....TimeStep.'] > 0 & 
                       df[,paste(zone_name,'.Zone.Operative.Temperature..C..TimeStep.',sep="")] < 26 & 
                       df[,paste(zone_name,'.Zone.Operative.Temperature..C..TimeStep.',sep="")] > 18 & 
                       df[,'HVAC_SALA.Schedule.Value....TimeStep.'] == 0, 
                     1,0)
  return(comf_vec)
}

dfs <- list(
  df_ref_PA_00,  df_ref_SM_00,  df_ref_SP_00,  df_ref_RJ_00,  df_ref_PA_11,  df_ref_SM_11,  df_ref_SP_11,  df_ref_RJ_11,  # ref
          df_ref_PA_10,  df_ref_SM_10,  df_ref_SP_10,  df_ref_RJ_10,  df_ref_PA_01,  df_ref_SM_01,  df_ref_SP_01,  df_ref_RJ_01,
          df_ref_PA_pil,  df_ref_SM_pil,  df_ref_SP_pil,   df_ref_RJ_pil,
  # df_adap_PA_00,  df_adap_SM_00,  df_adap_SP_00,  df_adap_RJ_00,  df_adap_PA_11,  df_adap_SM_11,  df_adap_SP_11,  df_adap_RJ_11,  # adap
  # df_adap_PA_10,  df_adap_SM_10,  df_adap_SP_10,  df_adap_RJ_10,  df_adap_PA_01,  df_adap_SM_01,  df_adap_SP_01,  df_adap_RJ_01,
  # df_adap_PA_pil,  df_adap_SM_pil,  df_adap_SP_pil,   df_adap_RJ_pil,
  # df_doub_PA_00,   df_doub_SM_00,   df_doub_SP_00,  df_doub_RJ_00,  df_doub_PA_11,  df_doub_SM_11,  df_doub_SP_11,  df_doub_RJ_11,  # doub
  # df_doub_PA_10,  df_doub_SM_10,  df_doub_SP_10,  df_doub_RJ_10,  df_doub_PA_01,  df_doub_SM_01,  df_doub_SP_01,  df_doub_RJ_01,
  # df_doub_PA_pil,  df_doub_SM_pil,  df_doub_SP_pil,  df_doub_RJ_pil #,
  df_hive_PA_00,   df_hive_SM_00,   df_hive_SP_00,  df_hive_RJ_00,  df_hive_PA_11,  df_hive_SM_11,  df_hive_SP_11,  df_hive_RJ_11,  # hive
             df_hive_PA_10,  df_hive_SM_10,  df_hive_SP_10,  df_hive_RJ_10,  df_hive_PA_01,  df_hive_SM_01,  df_hive_SP_01,  df_hive_RJ_01,
             df_hive_PA_pil,  df_hive_SM_pil,  df_hive_SP_pil,  df_hive_RJ_pil
)

climas <- c('Belém-PA','Santa Maria-RS','São Paulo-SP','Rio de Janeiro-RJ')
exp <- c('Intermediário','Unifamiliar','Cobertura','Térreo','Pilotis')

df <- data.frame("clima"=rep(NA,length(exp)*length(climas)),
                 "exp"=rep(NA,length(exp)*length(climas)),
                 "conforto"=rep(NA,length(exp)*length(climas)),
                 "carga.termica"=rep(NA,length(exp)*length(climas))
                 )

for(i in 1:length(exp)){
  # print(i)
  for(j in 1:length(climas)){
    # print(j)
    print(paste(exp[i],climas[j],as.character((i-1)*4+j)))
    df[(i-1)*4+j,'clima'] <- climas[j]
    df[(i-1)*4+j,'exp'] <- exp[i]
    
    comf_sin <- sum(comfcount(dfs[[20+(i-1)*4+j]],case="sin"))
    comf_ref <- sum(comfcount(dfs[[(i-1)*4+j]],case="ref"))
    diff_temp <- comf_sin/comf_ref
    df[(i-1)*4+j,'conforto'] <- diff_temp
    
    # loads_sin <- sum(dfs[[20+(i-1)*4+j]][,'SINGLEZONE.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.'])
    # loads_ref <- sum(dfs[[(i-1)*4+j]][,'SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Cooling.Energy..J..TimeStep.'])
    loads_sin <- sum(dfs[[20+(i-1)*4+j]][,'SINGLEZONE.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Heating.Energy..J..TimeStep.'])
    loads_ref <- sum(dfs[[(i-1)*4+j]][,'SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Heating.Energy..J..TimeStep.'])
    diff_loads <- loads_sin/loads_ref
    df[(i-1)*4+j,'carga.termica'] <- diff_loads
  }
}

df <- df[df$clima =='Santa Maria-RS' | df$clima =='São Paulo-SP',]

Cidade <- df$clima
# plottitle <- 'Double Wall'
plottitle <- 'Hive'
ggplot(df,aes(df$exp,df$conforto,fill=Cidade)) +
  geom_bar(stat="identity", position=position_dodge()) +
  ylab('Diferença Temp Operativa') +
  xlab('Exposição') +
  ylim(c(0,1.1)) +
  ggtitle(plottitle) +
  geom_hline(yintercept = 1)
  
ggplot(df,aes(df$exp,df$carga.termica,fill=Cidade)) +
  geom_bar(stat="identity", position=position_dodge()) +
  ylab('Diferença Cargas Térmicas') +
  xlab('Exposição') +
  # ylim(c(0,1.3)) +
  ggtitle(plottitle) +
  geom_hline(yintercept = 1) #+
  geom_hline(yintercept = .75, linetype="dotted")
  
  # diff_temp <- df_hive_SP_00$SINGLEZONE.Zone.Operative.Temperature..C..TimeStep.[df_hive_SP_00$SALA1.People.Occupant.Count....TimeStep. > 0 & df_adap_SP_00$HVAC_SALA.Schedule.Value....TimeStep. == 0] -
    diff_temp <- df_doub_SP_00$SINGLEZONE.Zone.Operative.Temperature..C..TimeStep.[df_doub_SP_00$SALA1.People.Occupant.Count....TimeStep. > 0 & df_adap_SP_00$HVAC_SALA.Schedule.Value....TimeStep. == 0] -
  df_adap_SP_00$SALA.Zone.Operative.Temperature..C..TimeStep.[df_adap_SP_00$SALA1.People.Occupant.Count....TimeStep. > 0 & df_adap_SP_00$HVAC_SALA.Schedule.Value....TimeStep. == 0]

ggplot() +
  geom_histogram(aes(diff_temp), binwidth = .1)+
  ylab('Número de timesteps') +
  xlab('Temp_op - Single menos Ref (°C)') +
  # ggtitle('Hive')
  ggtitle('Double Wall')
  

  
sum(df_hive_SP_00$SINGLEZONE.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Heating.Energy..J..TimeStep.)/(3600000*21.43)
sum(df_hive_SP_11$SINGLEZONE.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Heating.Energy..J..TimeStep.)/(3600000*21.43)

# RESTO ----
# PA
df_sin_PA$comfort <- comfcount(df_sin_PA,case="sin")
df_ref_PA$comfort <- comfcount(df_ref_PA,case="ref")
# SM
df_sin_SM$comfort <- comfcount(df_sin_SM,case="sin")
df_ref_SM$comfort <- comfcount(df_ref_SM,case="ref")
# SP
df_sin_SP$comfort <- comfcount(df_sin_SP,case="sin")
df_ref_SP$comfort <- comfcount(df_ref_SP,case="ref")
# SM
df_sin_RJ$comfort <- comfcount(df_sin_RJ,case="sin")
df_ref_RJ$comfort <- comfcount(df_ref_RJ,case="ref")

diff_temp_PA <- sum(df_sin_PA$comfort)/sum(df_ref_PA$comfort)
diff_temp_SM <- sum(df_sin_SM$comfort)/sum(df_ref_SM$comfort)
diff_temp_SP <- sum(df_sin_SP$comfort)/sum(df_ref_SP$comfort)
diff_temp_RJ <- sum(df_sin_RJ$comfort)/sum(df_ref_RJ$comfort)

area <- 21.43
sum(df_ref_SM_00$SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Heating.Energy..J..TimeStep.)/(3600000*area)
sum(df_ref_SM_11$SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Heating.Energy..J..TimeStep.)/(3600000*area)
sum(df_ref_SM_10$SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Heating.Energy..J..TimeStep.)/(3600000*area)
sum(df_ref_SM_01$SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Heating.Energy..J..TimeStep.)/(3600000*area)
sum(df_ref_SM_pil$SALA.IDEAL.LOADS.AIR.SYSTEM.Zone.Ideal.Loads.Zone.Total.Heating.Energy..J..TimeStep.)/(3600000*area)
