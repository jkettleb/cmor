
import cmor
import numpy

def cmor_initialisation():
    cmor.setup(inpath='/net/home/h03/hadju/Projects/MipTables/cmip5-cmor-tables/Tables',
               netcdf_file_action = cmor.CMOR_REPLACE_3,
               create_subdirectories = 0)
    cmor.dataset('pre-industrial control', 'ukmo', 'HadCM3', '360_day',
                 institute_id = 'ukmo',
                 model_id = 'HadCM3',
                 history = 'some global history',
                 forcing = 'N/A',
                 parent_experiment_id = 'N/A',
                 parent_experiment_rip = 'N/A',
                 branch_time = 0.,
                 contact = 'bob',
                 outpath = '/data/local/hadju/test')

def setup_data():
    axes = [ {'table_entry': 'time1',
              'units': 'days since 2000-01-01 00:00:00'
              },
             {'table_entry': 'latitude',
              'units': 'degrees',
              'coord_vals': [0],
              'cell_bounds': [-0.5, 0.5]},
             {'table_entry': 'longitude',
              'units': 'degrees',
              'coord_vals': [1],
              'cell_bounds': [0.5, 1.5]},
             ]

    values = numpy.array([215., 215.], numpy.float32)
    return values, axes

def cmor_define_and_write(values, axes):
    table = 'CMIP5_3hr'
    cmor.load_table(table)

    axis_ids = list()
    for axis in axes:
       axis_ids.append(cmor.axis(**axis))
                    
    varid = cmor.variable('tas',
                          'K',
                          axis_ids,
                          history = 'variable history',
                          missing_value = -99,
                          positive = ''
                          )

    time = [15, 25]
    cmor.write(varid, values, time_vals = time)
    
def version(cmor):
   return '%s.%s.%s' % (cmor.CMOR_VERSION_MAJOR,
                        cmor.CMOR_VERSION_MINOR,
                        cmor.CMOR_VERSION_PATCH)
    
def main():
    assert version(cmor) == '2.8.3'
    cmor_initialisation()
    values, axes = setup_data()
    cmor_define_and_write(values, axes)
    cmor.close()
    
if __name__ == '__main__':

    main()
