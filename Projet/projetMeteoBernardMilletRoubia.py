# state file generated using paraview version 6.0.1
import paraview
paraview.compatibility.major = 6
paraview.compatibility.minor = 0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.Set(
    ViewSize=[1418, 779],
    InteractionMode='2D',
    CenterOfRotation=[2.0, 46.441402435302734, 0.0],
    CameraPosition=[2.0, 46.441402435302734, 63.87260524857851],
    CameraFocalPoint=[2.0, 46.441402435302734, 0.0],
    CameraFocalDisk=1.0,
    CameraParallelScale=16.531446698647343,
    OSPRayMaterialLibrary=materialLibrary1,
)

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1418, 779)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
a12dec6hnc = NetCDFReader(registrationName='12dec6h.nc', FileName=['/home/pierre/Documents/Info5/Visu/VISU_DONNEES_INFO5/Projet/ParaviewData/12dec/12dec6h.nc'])
a12dec6hnc.Set(
    Dimensions='(latitude, longitude)',
    SphericalCoordinates=0,
)

# create a new 'Calculator'
temperatureCalculator = Calculator(registrationName='TemperatureCalculator', Input=a12dec6hnc)
temperatureCalculator.Set(
    ResultArrayName='Temperature',
    Function='t2m - 273.15',
)

# create a new 'Extract Subset'
temperatureSubset = ExtractSubset(registrationName='TemperatureSubset', Input=temperatureCalculator)
temperatureSubset.Set(
    VOI=[0, 1120, 0, 716, 0, 0],
    SampleRateI=10,
    SampleRateJ=10,
)

# create a new 'Calculator'
ventCalculator = Calculator(registrationName='VentCalculator', Input=a12dec6hnc)
ventCalculator.Set(
    ResultArrayName='VentVecteur',
    Function='u10*iHat+v10*jHat',
)

# create a new 'Extract Subset'
ventSubset = ExtractSubset(registrationName='VentSubset', Input=ventCalculator)
ventSubset.Set(
    VOI=[0, 1120, 0, 716, 0, 0],
    SampleRateI=25,
    SampleRateJ=25,
)

# create a new 'Threshold'
ventThreshold = Threshold(registrationName='VentThreshold', Input=ventSubset)
ventThreshold.Set(
    Scalars=['POINTS', 'VentVecteur'],
    LowerThreshold=3.0,
    UpperThreshold=11.704658914463328,
)

# create a new 'Glyph'
ventFleches = Glyph(registrationName='VentFleches', Input=ventThreshold,
    GlyphType='2D Glyph')
ventFleches.Set(
    OrientationArray=['POINTS', 'VentVecteur'],
    ScaleArray=['POINTS', 'No scale array'],
    ScaleFactor=0.5,
)

# create a new 'Extract Surface'
temparatureSurface = ExtractSurface(registrationName='TemparatureSurface', Input=temperatureSubset)

# create a new 'Triangulate'
temperatureTriagulate = Triangulate(registrationName='TemperatureTriagulate', Input=temparatureSurface)

# create a new 'Loop Subdivision'
tempratureSubdivision = LoopSubdivision(registrationName='TempratureSubdivision', Input=temperatureTriagulate)
tempratureSubdivision.NumberofSubdivisions = 2

# create a new 'Contour'
temperatureIsolines = Contour(registrationName='TemperatureIsolines', Input=tempratureSubdivision)
temperatureIsolines.Set(
    ContourBy=['POINTS', 'Temperature'],
    Isosurfaces=[0.0, 5.0, 10.0],
)

# create a new 'GDAL Vector Reader'
departements20140306100mshp = GDALVectorReader(registrationName='departements-20140306-100m.shp', FileName='/home/pierre/Documents/Info5/Visu/VISU_DONNEES_INFO5/Projet/departements-20140306-100m-shp/departements-20140306-100m.shp')

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from departements20140306100mshp
departements20140306100mshpDisplay = Show(departements20140306100mshp, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
departements20140306100mshpDisplay.Set(
    Representation='Surface',
    AmbientColor=[0.0, 0.0, 0.0],
    ColorArrayName=['POINTS', ''],
    DiffuseColor=[0.0, 0.0, 0.0],
    LineWidth=1.5,
    Assembly='Hierarchy',
)

# show data from tempratureSubdivision
tempratureSubdivisionDisplay = Show(tempratureSubdivision, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'Temperature'
temperatureLUT = GetColorTransferFunction('Temperature')
temperatureLUT.Set(
    RGBPoints=[
        # scalar, red, green, blue
        -16.690899077217523, 0.0564, 0.0564, 0.47,
        -10.812571624600016, 0.243, 0.46035, 0.81,
        -6.4653183994513554, 0.356814, 0.745025, 0.954368,
        -1.8872033118429687, 0.6882, 0.93, 0.91791,
        0.71268630027771, 0.899496, 0.944646, 0.768657,
        3.4603028677646783, 0.957108, 0.833819, 0.508916,
        7.499785953079805, 0.927521, 0.621439, 0.315357,
        12.34719991304253, 0.8, 0.352, 0.16,
        17.56668549908852, 0.59, 0.0767, 0.119475,
    ],
    NumberOfTableValues=12,
    ScalarRangeInitialized=1.0,
)

# trace defaults for the display properties.
tempratureSubdivisionDisplay.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 'Temperature'],
    LookupTable=temperatureLUT,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
tempratureSubdivisionDisplay.ScaleTransferFunction.Points = [-16.690899077217523, 0.0, 0.5, 0.0, 17.2422944288289, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
tempratureSubdivisionDisplay.OpacityTransferFunction.Points = [-16.690899077217523, 0.0, 0.5, 0.0, 17.2422944288289, 1.0, 0.5, 0.0]

# show data from temperatureIsolines
temperatureIsolinesDisplay = Show(temperatureIsolines, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
temperatureIsolinesDisplay.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 'Temperature'],
    LookupTable=temperatureLUT,
    LineWidth=3.0,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
temperatureIsolinesDisplay.ScaleTransferFunction.Points = [0.27569767580568616, 0.0, 0.5, 0.0, 0.2757587134838104, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
temperatureIsolinesDisplay.OpacityTransferFunction.Points = [0.27569767580568616, 0.0, 0.5, 0.0, 0.2757587134838104, 1.0, 0.5, 0.0]

# show data from ventFleches
ventFlechesDisplay = Show(ventFleches, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
ventFlechesDisplay.Set(
    Representation='Surface',
    AmbientColor=[0.7411764860153198, 0.7411764860153198, 0.7411764860153198],
    ColorArrayName=[None, ''],
    DiffuseColor=[0.7411764860153198, 0.7411764860153198, 0.7411764860153198],
    LineWidth=2.0,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
ventFlechesDisplay.ScaleTransferFunction.Points = [5.01715033100156, 0.0, 0.5, 0.0, 9.782604853913682, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
ventFlechesDisplay.OpacityTransferFunction.Points = [5.01715033100156, 0.0, 0.5, 0.0, 9.782604853913682, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for temperatureLUT in view renderView1
temperatureLUTColorBar = GetScalarBar(temperatureLUT, renderView1)
temperatureLUTColorBar.Set(
    WindowLocation='Upper Right Corner',
    Title='Temperature',
    ComponentTitle='',
)

# set color bar visibility
temperatureLUTColorBar.Visibility = 1

# show color legend
tempratureSubdivisionDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
temperatureIsolinesDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'Temperature'
temperaturePWF = GetOpacityTransferFunction('Temperature')
temperaturePWF.Set(
    Points=[-16.690899077217523, 0.0, 0.5, 0.0, 17.56668549908852, 1.0, 0.5, 0.0],
    ScalarRangeInitialized=1,
)

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.Set(
    ViewModules=renderView1,
    Cues=timeAnimationCue1,
    AnimationTime=1104027.0,
    StartTime=1104027.0,
    EndTime=1104033.0,
    PlayMode='Snap To TimeSteps',
)

# initialize the animation scene

# ----------------------------------------------------------------
# restore active source
SetActiveSource(a12dec6hnc)
# ----------------------------------------------------------------


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
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