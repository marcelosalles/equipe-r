
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
                
ap = ['apm','apc']
geom = ['_geom.txt','_geom_180.txt','_geom_abs02.txt','_geom_abs08.txt']
cob = ['int','out']
floor = ['int','out']
mode = ['vn','ac']
construction = ['construction_ref.txt','construction_leve.txt','construction_pesada.txt']

for a in ap:
    for g in geom:
        for c in cob:
            for f in floor:
                for m in mode:
                    for cons in construction:
                        
                        if 'abs' in g and c != 'out':
                            pass
                        else:
                            if 'abs02' in g:
                                tipo = '_abs02'
                            elif 'abs08' in g:
                                tipo = '_abs08'
                            elif c == 'int' and f == 'int':
                                tipo = '_inter'
                            elif c == 'int' and f == 'out':
                                tipo = '_terreo'
                            elif c == 'out' and f == 'int':
                                tipo = '_cob'
                            
                            if m == 'vn':
                                mode_name = '_vn'
                            else:
                                mode_name = '_ac'
                            
                            if 'ref' in cons:
                                cons_name = '_ref'
                            elif 'leve' in cons:
                                cons_name = '_leve'
                            if 'pesada' in cons:
                                cons_name = '_pesada'
                            
                            if '180' in g:
                                azi = '_180'
                            else:
                                azi = ''
                            
                            output_name = a + tipo + mode_name + cons_name + azi + '.idf'
                            idf_bundler(input_files=[a+g, a+'_cob_'+c+'.txt', a+'_floor_'+f+'.txt', a+mode_name+'.txt', cons],output_name=output_name)
    

# idf_bundler(input_files=['apm_geom_abs02.txt','apm_cob_out.txt','apm_floor_int.txt','apm_vn.txt','construction_ref.txt'],output_name='apm_abs02_vn_ref.idf')
# idf_bundler(input_files=['apm_geom_abs02.txt','apm_cob_out.txt','apm_floor_int.txt','apm_vn.txt','construction_leve.txt'],output_name='apm_abs02_vn_leve.idf')
# idf_bundler(input_files=['apm_geom_abs02.txt','apm_cob_out.txt','apm_floor_int.txt','apm_vn.txt','construction_pesada.txt'],output_name='apm_abs02_vn_pesada.idf')

# idf_bundler(input_files=['apm_geom_abs08.txt','apm_cob_out.txt','apm_floor_int.txt','apm_vn.txt','construction_ref.txt'],output_name='apm_abs08_vn_ref.idf')
# idf_bundler(input_files=['apm_geom_abs08.txt','apm_cob_out.txt','apm_floor_int.txt','apm_vn.txt','construction_leve.txt'],output_name='apm_abs08_vn_leve.idf')
# idf_bundler(input_files=['apm_geom_abs08.txt','apm_cob_out.txt','apm_floor_int.txt','apm_vn.txt','construction_pesada.txt'],output_name='apm_abs08_vn_pesada.idf')

# idf_bundler(input_files=['apm_geom_abs02.txt','apm_cob_out.txt','apm_floor_int.txt','apm_ac.txt','construction_ref.txt'],output_name='apm_abs02_ac_ref.idf')
# idf_bundler(input_files=['apm_geom_abs02.txt','apm_cob_out.txt','apm_floor_int.txt','apm_ac.txt','construction_leve.txt'],output_name='apm_abs02_ac_leve.idf')
# idf_bundler(input_files=['apm_geom_abs02.txt','apm_cob_out.txt','apm_floor_int.txt','apm_ac.txt','construction_pesada.txt'],output_name='apm_abs02_ac_pesada.idf')

# idf_bundler(input_files=['apm_geom_abs08.txt','apm_cob_out.txt','apm_floor_int.txt','apm_ac.txt','construction_ref.txt'],output_name='apm_abs08_ac_ref.idf')
# idf_bundler(input_files=['apm_geom_abs08.txt','apm_cob_out.txt','apm_floor_int.txt','apm_ac.txt','construction_leve.txt'],output_name='apm_abs08_ac_leve.idf')
# idf_bundler(input_files=['apm_geom_abs08.txt','apm_cob_out.txt','apm_floor_int.txt','apm_ac.txt','construction_pesada.txt'],output_name='apm_abs08_ac_pesada.idf')

# idf_bundler(input_files=['apc_geom_abs02.txt','apc_cob_out.txt','apc_floor_int.txt','apc_vn.txt','construction_ref.txt'],output_name='apc_abs02_vn_ref.idf')
# idf_bundler(input_files=['apc_geom_abs02.txt','apc_cob_out.txt','apc_floor_int.txt','apc_vn.txt','construction_leve.txt'],output_name='apc_abs02_vn_leve.idf')
# idf_bundler(input_files=['apc_geom_abs02.txt','apc_cob_out.txt','apc_floor_int.txt','apc_vn.txt','construction_pesada.txt'],output_name='apc_abs02_vn_pesada.idf')

# idf_bundler(input_files=['apc_geom_abs08.txt','apc_cob_out.txt','apc_floor_int.txt','apc_vn.txt','construction_ref.txt'],output_name='apc_abs08_vn_ref.idf')
# idf_bundler(input_files=['apc_geom_abs08.txt','apc_cob_out.txt','apc_floor_int.txt','apc_vn.txt','construction_leve.txt'],output_name='apc_abs08_vn_leve.idf')
# idf_bundler(input_files=['apc_geom_abs08.txt','apc_cob_out.txt','apc_floor_int.txt','apc_vn.txt','construction_pesada.txt'],output_name='apc_abs08_vn_pesada.idf')

# idf_bundler(input_files=['apc_geom_abs02.txt','apc_cob_out.txt','apc_floor_int.txt','apc_ac.txt','construction_ref.txt'],output_name='apc_abs02_ac_ref.idf')
# idf_bundler(input_files=['apc_geom_abs02.txt','apc_cob_out.txt','apc_floor_int.txt','apc_ac.txt','construction_leve.txt'],output_name='apc_abs02_ac_leve.idf')
# idf_bundler(input_files=['apc_geom_abs02.txt','apc_cob_out.txt','apc_floor_int.txt','apc_ac.txt','construction_pesada.txt'],output_name='apc_abs02_ac_pesada.idf')

# idf_bundler(input_files=['apc_geom_abs08.txt','apc_cob_out.txt','apc_floor_int.txt','apc_ac.txt','construction_ref.txt'],output_name='apc_abs08_ac_ref.idf')
# idf_bundler(input_files=['apc_geom_abs08.txt','apc_cob_out.txt','apc_floor_int.txt','apc_ac.txt','construction_leve.txt'],output_name='apc_abs08_ac_leve.idf')
# idf_bundler(input_files=['apc_geom_abs08.txt','apc_cob_out.txt','apc_floor_int.txt','apc_ac.txt','construction_pesada.txt'],output_name='apc_abs08_ac_pesada.idf')


# idf_bundler(input_files=['apm_geom.txt','apm_cob_int.txt','apm_floor_int.txt','apm_vn.txt','construction_ref.txt'],output_name='apm_inter_vn_ref.idf')
# idf_bundler(input_files=['apm_geom.txt','apm_cob_int.txt','apm_floor_int.txt','apm_vn.txt','construction_leve.txt'],output_name='apm_inter_vn_leve.idf')
# idf_bundler(input_files=['apm_geom.txt','apm_cob_int.txt','apm_floor_int.txt','apm_vn.txt','construction_pesada.txt'],output_name='apm_inter_vn_pesada.idf')

# idf_bundler(input_files=['apm_geom.txt','apm_cob_out.txt','apm_floor_int.txt','apm_vn.txt','construction_ref.txt'],output_name='apm_cob_vn_ref.idf')
# idf_bundler(input_files=['apm_geom.txt','apm_cob_out.txt','apm_floor_int.txt','apm_vn.txt','construction_leve.txt'],output_name='apm_cob_vn_leve.idf')
# idf_bundler(input_files=['apm_geom.txt','apm_cob_out.txt','apm_floor_int.txt','apm_vn.txt','construction_pesada.txt'],output_name='apm_cob_vn_pesada.idf')

# idf_bundler(input_files=['apm_geom.txt','apm_cob_int.txt','apm_floor_out.txt','apm_vn.txt','construction_ref.txt'],output_name='apm_terreo_vn_ref.idf')
# idf_bundler(input_files=['apm_geom.txt','apm_cob_int.txt','apm_floor_out.txt','apm_vn.txt','construction_leve.txt'],output_name='apm_terreo_vn_leve.idf')
# idf_bundler(input_files=['apm_geom.txt','apm_cob_int.txt','apm_floor_out.txt','apm_vn.txt','construction_pesada.txt'],output_name='apm_terreo_vn_pesada.idf')

'''
## EXEMPLES ##

idf_bundler(input_files=['apm_geom.txt','apm_cob_int.txt','apm_floor_int.txt','apm_vn.txt','construction_ref.txt'],output_name='apm_inter_vn_ref.idf')
idf_bundler(input_files=['apm_geom.txt','apm_cob_int.txt','apm_floor_int.txt','apm_vn.txt','construction_leve.txt'],output_name='apm_inter_vn_leve.idf')
idf_bundler(input_files=['apm_geom.txt','apm_cob_int.txt','apm_floor_int.txt','apm_vn.txt','construction_pesada.txt'],output_name='apm_inter_vn_pesada.idf')

idf_bundler(input_files=['apm_geom.txt','apm_cob_out.txt','apm_floor_int.txt','apm_vn.txt','construction_ref.txt'],output_name='apm_cob_vn_ref.idf')
idf_bundler(input_files=['apm_geom.txt','apm_cob_out.txt','apm_floor_int.txt','apm_vn.txt','construction_leve.txt'],output_name='apm_cob_vn_leve.idf')
idf_bundler(input_files=['apm_geom.txt','apm_cob_out.txt','apm_floor_int.txt','apm_vn.txt','construction_pesada.txt'],output_name='apm_cob_vn_pesada.idf')

idf_bundler(input_files=['apm_geom.txt','apm_cob_int.txt','apm_floor_out.txt','apm_vn.txt','construction_ref.txt'],output_name='apm_terreo_vn_ref.idf')
idf_bundler(input_files=['apm_geom.txt','apm_cob_int.txt','apm_floor_out.txt','apm_vn.txt','construction_leve.txt'],output_name='apm_terreo_vn_leve.idf')
idf_bundler(input_files=['apm_geom.txt','apm_cob_int.txt','apm_floor_out.txt','apm_vn.txt','construction_pesada.txt'],output_name='apm_terreo_vn_pesada.idf')

'''
