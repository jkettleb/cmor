import _cmip6_cv
atts = """
CMOR_MAX_STRING
CMOR_MAX_ELEMENTS
CMOR_MAX_AXES
CMOR_MAX_VARIABLES
CMOR_MAX_GRIDS
CMOR_MAX_DIMENSIONS
CMOR_MAX_ATTRIBUTES
CMOR_MAX_ERRORS
CMOR_MAX_TABLES
CMOR_MAX_GRID_ATTRIBUTES
CMOR_QUIET
CMOR_EXIT_ON_MAJOR
CMOR_EXIT
CMOR_EXIT_ON_WARNING
CMOR_VERSION_MAJOR
CMOR_VERSION_MINOR
CMOR_VERSION_PATCH
CMOR_CF_VERSION_MAJOR
CMOR_CF_VERSION_MINOR
CMOR_WARNING
CMOR_NORMAL
CMOR_CRITICAL
TABLE_CONTROL_FILENAME
GLOBAL_CV_FILENAME
CMOR_DEFAULT_PATH_TEMPLATE
CMOR_DEFAULT_FILE_TEMPLATE
CMOR_DEFAULT_FURTHERURL_TEMPLATE
FILE_PATH_TEMPLATE
FILE_NAME_TEMPLATE
GLOBAL_ATT_FURTHERINFOURLTMPL
"""

for att in atts.split():
    attnm = att
    exec("%s = _cmip6_cv.getCMOR_defaults_include('%s')" % (att, att))
