import paraview
paraview.compatibility.major = 6
paraview.compatibility.minor = 0
import sys
import math

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

fileName = sys.argv[1]
longitude = float(sys.argv[2])
latitude = float(sys.argv[3])

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create the first 'Render View' (for the first window)
renderView1 = CreateView('RenderView')
renderView1.Set(
    ViewSize=[961, 479],
    InteractionMode='2D',
    CenterOfRotation=[2.0, 46.45000076293945, 0.0],
    CameraPosition=[2.0, 46.45000076293945, 64.20057971900172],
    CameraFocalPoint=[2.0, longitude, latitude],
    CameraFocalDisk=1.0,
    CameraParallelScale=1.616332737900287,
    OSPRayMaterialLibrary=materialLibrary1,
)

# Create the second 'Render View' (for the second window)
renderView2 = CreateView('RenderView')
renderView2.Set(
    ViewSize=[961, 479],
    InteractionMode='2D',
    CenterOfRotation=[2.0, 46.45000076293945, 0.0],
    CameraPosition=[2.0, 46.45000076293945, 64.20057971900172],
    CameraFocalPoint=[2.0, 45.2815517, 5.8441357],
    CameraFocalDisk=1.0,
    CameraParallelScale=16.616332737900287, # zoom
    OSPRayMaterialLibrary=materialLibrary1,
)

# ----------------------------------------------------------------
# Create two separate layouts, one for each render view
# ----------------------------------------------------------------

# Create first layout for the first window (layout1)
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(961, 479)

# Create second layout for the second window (layout2)
layout2 = CreateLayout(name='Layout #2')
layout2.AssignView(0, renderView2)
layout2.SetSize(961, 479)

# ----------------------------------------------------------------
# restore active view to the first render view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
a12dec6nc = NetCDFReader(registrationName='12dec6.nc', FileName=[fileName])
a12dec6nc.Set(
    Dimensions='(latitude, longitude)',
    SphericalCoordinates=0,
)

# ----------------------------------------------------------------
# setup the visualization in the first render view
# ----------------------------------------------------------------

# show data from a12dec6nc in the first render view
a12dec6ncDisplay = Show(a12dec6nc, renderView1, 'RectilinearGridRepresentation')

# get color transfer function/color map for 't2m'
t2mLUT = GetColorTransferFunction('t2m')
t2mLUT.Set(
    RGBPoints=GenerateRGBPoints(
        range_min=256.45910092278245,
        range_max=290.7166854990885,
    ),
    ScalarRangeInitialized=1.0,
)

# trace defaults for the display properties.
a12dec6ncDisplay.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 't2m'],
    LookupTable=t2mLUT,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
a12dec6ncDisplay.ScaleTransferFunction.Points = [-19.355923744141002, 0.0, 0.5, 0.0, -19.352018356323242, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
a12dec6ncDisplay.OpacityTransferFunction.Points = [-19.355923744141002, 0.0, 0.5, 0.0, -19.352018356323242, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in the second render view
# ----------------------------------------------------------------

# show data from a12dec6nc in the second render view
a12dec6ncDisplay2 = Show(a12dec6nc, renderView2, 'RectilinearGridRepresentation')

# get color transfer function/color map for 't2m'
t2mLUT2 = GetColorTransferFunction('t2m')
t2mLUT2.Set(
    RGBPoints=GenerateRGBPoints(
        range_min=256.45910092278245,
        range_max=290.7166854990885,
    ),
    ScalarRangeInitialized=1.0,
)

# trace defaults for the display properties for the second view
a12dec6ncDisplay2.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 't2m'],
    LookupTable=t2mLUT2,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction' in second view
a12dec6ncDisplay2.ScaleTransferFunction.Points = [-19.355923744141002, 0.0, 0.5, 0.0, -19.352018356323242, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction' in second view
a12dec6ncDisplay2.OpacityTransferFunction.Points = [-19.355923744141002, 0.0, 0.5, 0.0, -19.352018356323242, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# restore active source
SetActiveSource(a12dec6nc)
# ----------------------------------------------------------------

##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
RenderAllViews()
#
## Interact with the view, useful when running from pvpython
Interact()
#
## Save a screenshot of the active view
SaveScreenshot("testParaview.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/nightly/python/
##--------------------------------------------

