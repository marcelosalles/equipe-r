
def idf_bundler(input_files, output_name):
    # Bundles files with different idf objects to create one idf model.
    # input_files - List of files with idf objects.
    # output_name - The name of the resulted idf model.
    
    print(output_name)
    
    for i in range(len(input_files)):
        input_files[i] = open(input_files[i], 'rb')
    
    with open(output_name, 'wb') as model:
        
        for i in range(len(input_files)):
            for line in input_files[i]:
                
                model.write(line)

'''
## EXEMPLES ##

# DOUBLE, TIJOLO
idf_bundler(input_files=['seed_upper.txt','geom_single_double.txt','sch_original_out_single.txt','roof1_single.txt','floor1_single.txt','construction_tijolo.txt'],output_name='double_floor1_roof1_tijolo.idf')
idf_bundler(input_files=['seed_upper.txt','geom_single_double.txt','sch_original_out_single.txt','roof1_single.txt','floor0_single.txt','construction_tijolo.txt'],output_name='double_floor0_roof1_tijolo.idf')
idf_bundler(input_files=['seed_upper.txt','geom_single_double.txt','sch_original_out_single.txt','roof0_single.txt','floor1_single.txt','construction_tijolo.txt'],output_name='double_floor1_roof0_tijolo.idf')
idf_bundler(input_files=['seed_upper.txt','geom_single_double.txt','sch_original_out_single.txt','roof0_single.txt','floor0_single.txt','construction_tijolo.txt'],output_name='double_floor0_roof0_tijolo.idf')
idf_bundler(input_files=['seed_upper.txt','geom_single_double.txt','sch_original_out_single.txt','roof0_single.txt','pilotis_single.txt','construction_tijolo.txt'],output_name='double_pilotis_roof0_tijolo.idf')

# HIVE, TIJOLO
idf_bundler(input_files=['seed_upper.txt','geom_single_hive.txt','sch_original_adi_single.txt','roof1_single_hive.txt','floor1_single_hive.txt','crack.txt','construction_tijolo.txt'],output_name='hive_floor1_roof1_tijolo.idf')
idf_bundler(input_files=['seed_upper.txt','geom_single_hive.txt','sch_original_adi_single.txt','roof1_single_hive.txt','floor0_single_hive.txt','crack.txt','construction_tijolo.txt'],output_name='hive_floor0_roof1_tijolo.idf')
idf_bundler(input_files=['seed_upper.txt','geom_single_hive.txt','sch_original_adi_single.txt','roof0_single_hive.txt','floor1_single_hive.txt','crack.txt','construction_tijolo.txt'],output_name='hive_floor1_roof0_tijolo.idf')
idf_bundler(input_files=['seed_upper.txt','geom_single_hive.txt','sch_original_adi_single.txt','roof0_single_hive.txt','floor0_single_hive.txt','crack.txt','construction_tijolo.txt'],output_name='hive_floor0_roof0_tijolo.idf')
idf_bundler(input_files=['seed_upper.txt','geom_single_hive.txt','sch_original_adi_single.txt','roof0_single_hive.txt','pilotis_single_hive.txt','crack.txt','construction_tijolo.txt'],output_name='hive_pilotis_roof0_tijolo.idf')

# REF
idf_bundler(input_files=['seed.txt','geom_ref.txt','sch_original.txt','roof1_ref.txt','floor1_ref.txt'],output_name='ref_floor1_roof1.idf')
idf_bundler(input_files=['seed.txt','geom_ref.txt','sch_original.txt','roof1_ref.txt','floor0_ref.txt'],output_name='ref_floor0_roof1.idf')
idf_bundler(input_files=['seed.txt','geom_ref.txt','sch_original.txt','roof0_ref.txt','floor1_ref.txt'],output_name='ref_floor1_roof0.idf')
idf_bundler(input_files=['seed.txt','geom_ref.txt','sch_original.txt','roof0_ref.txt','floor0_ref.txt'],output_name='ref_floor0_roof0.idf')
idf_bundler(input_files=['seed.txt','geom_ref.txt','sch_original.txt','roof0_ref.txt','pilotis_ref.txt'],output_name='ref_pilotis_roof0.idf')

# ADAPTED
idf_bundler(input_files=['seed.txt','geom_ref_adapted.txt','sch_original_adapted.txt','roof1_adapted.txt','floor1_adapted.txt'],output_name='adapted_floor1_roof1.idf')
idf_bundler(input_files=['seed.txt','geom_ref_adapted.txt','sch_original_adapted.txt','roof1_adapted.txt','floor0_adapted.txt'],output_name='adapted_floor0_roof1.idf')
idf_bundler(input_files=['seed.txt','geom_ref_adapted.txt','sch_original_adapted.txt','roof0_adapted.txt','floor1_adapted.txt'],output_name='adapted_floor1_roof0.idf')
idf_bundler(input_files=['seed.txt','geom_ref_adapted.txt','sch_original_adapted.txt','roof0_adapted.txt','floor0_adapted.txt'],output_name='adapted_floor0_roof0.idf')
idf_bundler(input_files=['seed.txt','geom_ref_adapted.txt','sch_original_adapted.txt','roof0_adapted.txt','pilotis_adapted.txt'],output_name='adapted_pilotis_roof0.idf')

# DOUBLE
idf_bundler(input_files=['seed_upper.txt','geom_single_double.txt','sch_original_out_single.txt','roof1_single.txt','floor1_single.txt','construction_concreto.txt'],output_name='double_floor1_roof1.idf')
idf_bundler(input_files=['seed_upper.txt','geom_single_double.txt','sch_original_out_single.txt','roof1_single.txt','floor0_single.txt','construction_concreto.txt'],output_name='double_floor0_roof1.idf')
idf_bundler(input_files=['seed_upper.txt','geom_single_double.txt','sch_original_out_single.txt','roof0_single.txt','floor1_single.txt','construction_concreto.txt'],output_name='double_floor1_roof0.idf')
idf_bundler(input_files=['seed_upper.txt','geom_single_double.txt','sch_original_out_single.txt','roof0_single.txt','floor0_single.txt','construction_concreto.txt'],output_name='double_floor0_roof0.idf')
idf_bundler(input_files=['seed_upper.txt','geom_single_double.txt','sch_original_out_single.txt','roof0_single.txt','pilotis_single.txt','construction_concreto.txt'],output_name='double_pilotis_roof0.idf')

# HIVE
idf_bundler(input_files=['seed_upper.txt','geom_single_hive.txt','sch_original_adi_single.txt','roof1_single_hive.txt','floor1_single_hive.txt','crack.txt','construction_concreto.txt'],output_name='hive_floor1_roof1.idf')
idf_bundler(input_files=['seed_upper.txt','geom_single_hive.txt','sch_original_adi_single.txt','roof1_single_hive.txt','floor0_single_hive.txt','crack.txt','construction_concreto.txt'],output_name='hive_floor0_roof1.idf')
idf_bundler(input_files=['seed_upper.txt','geom_single_hive.txt','sch_original_adi_single.txt','roof0_single_hive.txt','floor1_single_hive.txt','crack.txt','construction_concreto.txt'],output_name='hive_floor1_roof0.idf')
idf_bundler(input_files=['seed_upper.txt','geom_single_hive.txt','sch_original_adi_single.txt','roof0_single_hive.txt','floor0_single_hive.txt','crack.txt','construction_concreto.txt'],output_name='hive_floor0_roof0.idf')
idf_bundler(input_files=['seed_upper.txt','geom_single_hive.txt','sch_original_adi_single.txt','roof0_single_hive.txt','pilotis_single_hive.txt','crack.txt','construction_concreto.txt'],output_name='hive_pilotis_roof0.idf')
'''
