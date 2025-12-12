# state file generated using paraview version 6.0.1
import paraview
import sys
import math
paraview.compatibility.major = 6
paraview.compatibility.minor = 0

#### minimal conditions (Fichier longitude et latitude en arguments. ficher ".nc", longitude et latitude == float, tt les autres argv == float) 

ShowIsolines = False
if (len(sys.argv) >= 5) :
	ShowIsolines = True


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
    ViewSize=[1920, 1080],
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
    ViewSize=[1920, 1080],
    InteractionMode='2D',
    CenterOfRotation=[2.0, 46.45000076293945, 0.0],
    CameraPosition=[2.0, 46.45000076293945, 64.20057971900172],
    CameraFocalPoint=[2.0, longitude, latitude],
    CameraFocalDisk=1.0,
    CameraParallelScale=8.950149718542106, # zoom
    OSPRayMaterialLibrary=materialLibrary1,
)

# ----------------------------------------------------------------
# Create two separate layouts, one for each render view
# ----------------------------------------------------------------

# Create first layout for the first window (layout1)
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
#layout1.SetSize(961, 479)

# Create second layout for the second window (layout2)
layout2 = CreateLayout(name='Layout #2')
layout2.AssignView(0, renderView2)
#layout2.SetSize(961, 479)

# ----------------------------------------------------------------
# restore active view to the first render view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the selections
# ----------------------------------------------------------------

# create a new 'Composite Data ID Selection Source'
selection_sources11971 = CreateSelection(proxyname='CompositeDataIDSelectionSource', registrationname='selection_sources.11971', IDs=[1, 0, 0, 2, 0, 0, 4, 0, 0, 5, 0, 0, 6, 0, 3, 6, 0, 6, 8, 0, 0, 9, 0, 0, 11, 0, 0, 13, 0, 1, 13, 0, 8, 13, 0, 27, 13, 0, 30, 13, 0, 60, 14, 0, 1, 15, 0, 0, 17, 0, 13, 17, 0, 14, 17, 0, 15, 17, 0, 16, 17, 0, 17, 18, 0, 0, 19, 0, 0, 20, 0, 1, 21, 0, 10, 21, 0, 12, 21, 0, 15, 21, 0, 19, 21, 0, 29, 21, 0, 30, 21, 0, 32, 21, 0, 55, 21, 0, 56, 21, 0, 87, 21, 0, 93, 21, 0, 94, 21, 0, 106, 21, 0, 128, 21, 0, 141, 21, 0, 151, 21, 0, 154, 22, 0, 0, 23, 0, 0, 24, 0, 0, 25, 0, 0, 26, 0, 0, 27, 0, 0, 28, 0, 7, 28, 0, 20, 28, 0, 53, 28, 0, 84, 28, 0, 86, 28, 0, 91, 28, 0, 99, 28, 0, 109, 28, 0, 120, 28, 0, 121, 28, 0, 157, 28, 0, 169, 28, 0, 185, 28, 0, 186, 28, 0, 188, 28, 0, 189, 28, 0, 191, 29, 0, 2, 29, 0, 12, 29, 0, 26, 29, 0, 36, 29, 0, 53, 30, 0, 10, 30, 0, 13, 30, 0, 17, 31, 0, 0, 32, 0, 0, 33, 0, 0, 34, 0, 4, 34, 0, 5, 34, 0, 6, 35, 0, 1, 36, 0, 2, 36, 0, 24, 36, 0, 38, 36, 0, 42, 37, 0, 0, 38, 0, 0, 39, 0, 0, 40, 0, 2, 41, 0, 0, 42, 0, 0, 43, 0, 0, 44, 0, 0, 45, 0, 6, 46, 0, 0, 47, 0, 0, 48, 0, 0, 49, 0, 0, 50, 0, 0, 51, 0, 18, 51, 0, 24, 51, 0, 29, 51, 0, 44, 51, 0, 55, 51, 0, 59, 52, 0, 0, 53, 0, 0, 54, 0, 0, 55, 0, 2, 56, 0, 0, 56, 0, 1, 56, 0, 2, 57, 0, 2, 57, 0, 4, 57, 0, 7, 57, 0, 14, 57, 0, 21, 57, 0, 26, 57, 0, 81, 57, 0, 86, 57, 0, 89, 57, 0, 94, 58, 0, 0, 59, 0, 0, 60, 0, 1, 61, 0, 3, 62, 0, 0, 62, 0, 1, 63, 0, 0, 63, 0, 1, 64, 0, 0, 65, 0, 20, 66, 0, 0, 66, 0, 1, 66, 0, 2, 67, 0, 0, 67, 0, 1, 68, 0, 0, 69, 0, 0, 70, 0, 0, 71, 0, 0, 72, 0, 0, 72, 0, 2, 73, 0, 0, 74, 0, 0, 75, 0, 0, 77, 0, 0, 78, 0, 0, 79, 0, 0, 80, 0, 0, 81, 0, 8, 82, 0, 0, 83, 0, 0, 84, 0, 1, 84, 0, 11, 84, 0, 19, 84, 0, 21, 84, 0, 22, 84, 0, 32, 85, 0, 0, 85, 0, 1, 86, 0, 1, 86, 0, 3, 86, 0, 4, 87, 0, 0, 88, 0, 0, 89, 0, 0, 90, 0, 0, 91, 0, 0, 92, 0, 0, 93, 0, 0, 94, 0, 0, 95, 0, 0, 96, 0, 0])

# create a new 'Append Selections'
selection_filter12016 = CreateSelection(proxyname='AppendSelections', registrationname='selection_filter.12016', Input=selection_sources11971,
    Expression='s0',
    SelectionNames=['s0'])

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
a12dec6hnc = NetCDFReader(registrationName='12dec6h.nc', FileName=fileName)
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
    UpperThreshold=3.0,
    ThresholdMethod='Above Upper Threshold',
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

if (ShowIsolines) :
	# create a new 'Contour'
	temperatureIsolines = Contour(registrationName='TemperatureIsolines', Input=tempratureSubdivision)
	temperatureIsolines.Set(
		ContourBy=['POINTS', 'Temperature'],
		Isosurfaces=[float(i) for i in sys.argv[4:]],
	)

# create a new 'GDAL Vector Reader'
departements20140306100mshp = GDALVectorReader(registrationName='departements-20140306-100m.shp', FileName='/home/pierre/Documents/Info5/Visu/VISU_DONNEES_INFO5/Projet/departements-20140306-100m-shp/departements-20140306-100m.shp')

# create a new 'Extract Selection'
extractSelection1 = ExtractSelection(registrationName='ExtractSelection1', Input=departements20140306100mshp,
    Selection=selection_filter12016)

# ----------------------------------------------------------------
# setup the visualization in the first render view
# ----------------------------------------------------------------

# show data from extractSelection1
extractSelection1Display = Show(extractSelection1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
extractSelection1Display.Set(
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

if (ShowIsolines) :
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
    AmbientColor=[0.6, 0.6, 0.6],
    ColorArrayName=[None, ''],
    DiffuseColor=[0.6, 0.6, 0.6],
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

if (ShowIsolines) :
	# show color legend
	temperatureIsolinesDisplay.SetScalarBarVisibility(renderView1, True)
	
	
# ----------------------------------------------------------------
# setup the visualization in the second render view
# ----------------------------------------------------------------

# show data from extractSelection1
extractSelection1Display2 = Show(extractSelection1, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
extractSelection1Display2.Set(
    Representation='Surface',
    AmbientColor=[0.0, 0.0, 0.0],
    ColorArrayName=['POINTS', ''],
    DiffuseColor=[0.0, 0.0, 0.0],
    LineWidth=1.5,
    Assembly='Hierarchy',
)

# show data from tempratureSubdivision
tempratureSubdivisionDisplay2 = Show(tempratureSubdivision, renderView2, 'GeometryRepresentation')

# get color transfer function/color map for 'Temperature'
temperatureLUT2 = GetColorTransferFunction('Temperature')
temperatureLUT2.Set(
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
tempratureSubdivisionDisplay2.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 'Temperature'],
    LookupTable=temperatureLUT,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
tempratureSubdivisionDisplay2.ScaleTransferFunction.Points = [-16.690899077217523, 0.0, 0.5, 0.0, 17.2422944288289, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
tempratureSubdivisionDisplay2.OpacityTransferFunction.Points = [-16.690899077217523, 0.0, 0.5, 0.0, 17.2422944288289, 1.0, 0.5, 0.0]

if (ShowIsolines) :
	# show data from temperatureIsolines
	temperatureIsolinesDisplay2 = Show(temperatureIsolines, renderView2, 'GeometryRepresentation')

	# trace defaults for the display properties.
	temperatureIsolinesDisplay2.Set(
		Representation='Surface',
		ColorArrayName=['POINTS', 'Temperature'],
		LookupTable=temperatureLUT,
		LineWidth=3.0,
	)

	# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
	temperatureIsolinesDisplay2.ScaleTransferFunction.Points = [0.27569767580568616, 0.0, 0.5, 0.0, 0.2757587134838104, 1.0, 0.5, 0.0]

	# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
	temperatureIsolinesDisplay2.OpacityTransferFunction.Points = [0.27569767580568616, 0.0, 0.5, 0.0, 0.2757587134838104, 1.0, 0.5, 0.0]

# show data from ventFleches
ventFlechesDisplay2 = Show(ventFleches, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
ventFlechesDisplay2.Set(
    Representation='Surface',
    AmbientColor=[0.6, 0.6, 0.6],
    ColorArrayName=[None, ''],
    DiffuseColor=[0.6, 0.6, 0.6],
    LineWidth=2.0,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
ventFlechesDisplay2.ScaleTransferFunction.Points = [5.01715033100156, 0.0, 0.5, 0.0, 9.782604853913682, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
ventFlechesDisplay2.OpacityTransferFunction.Points = [5.01715033100156, 0.0, 0.5, 0.0, 9.782604853913682, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for temperatureLUT in view renderView1
temperatureLUTColorBar2 = GetScalarBar(temperatureLUT, renderView2)
temperatureLUTColorBar2.Set(
    WindowLocation='Upper Right Corner',
    Title='Temperature',
    ComponentTitle='',
)

# set color bar visibility
temperatureLUTColorBar2.Visibility = 1

# show color legend
tempratureSubdivisionDisplay2.SetScalarBarVisibility(renderView2, True)

if (ShowIsolines) :
	# show color legend
	temperatureIsolinesDisplay2.SetScalarBarVisibility(renderView2, True)
	
# Fit all visible data in view 1
renderView2.ResetCamera()

# ----------------------------------------------------------------
# setup color maps and opacity maps used 
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'Temperature'
temperaturePWF = GetOpacityTransferFunction('Temperature')
temperaturePWF.Set(
    Points=[-16.690899077217523, 0.0, 0.5, 0.0, 17.56668549908852, 1.0, 0.5, 0.0],
    ScalarRangeInitialized=1,
)

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes for the first render view
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
# setup animation scene, tracks and keyframes for the second render view
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get the time-keeper
timeKeeper2 = GetTimeKeeper()

# initialize the timekeeper

# get time animation track
timeAnimationCue2 = GetTimeTrack()

# initialize the animation track

# get animation scene
animationScene2 = GetAnimationScene()

# initialize the animation scene
animationScene2.Set(
    ViewModules=renderView2,
    Cues=timeAnimationCue2,
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
RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
Interact()
#
## Save a screenshot of both viex
SaveScreenshot("testParaview1.png", view=renderView1)
SaveScreenshot("testParaview2.png", view=renderView2)
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
