# state file generated using paraview version 6.0.1
import paraview
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

paraview.compatibility.major = 6
paraview.compatibility.minor = 0

#### minimal conditions (Fichier longitude et latitude en arguments. ficher ".nc", longitude et latitude == float, tt les autres argv == float) 

def usageprint() :
	print("usage : <chemin vers le fichier> <longitude> <latitude> <t1> <t2> ... <tn>")
	print("en sachant que :")
	print("le fichier doit être de type '.nc'")
	print("longitude et latitude doivent être des nombres")
	print("t1, t2, ..., tn sont les valeurs de températures pour les courbes iso-valeurs et doivent être des nombres")
	exit()


ShowIsolines = False
if (len(sys.argv) >= 5) :
	ShowIsolines = True
	
if ((len(sys.argv) < 4) or (sys.argv[1].split("/")[-1].split(".")[-1] != "nc") or ()) :
	print("File error")
	usageprint()


#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

fileName = sys.argv[1]

try:
	longitude = float(sys.argv[2])
except ValueError:
	print("Longitude Error")
	usageprint()

try:
	latitude = float(sys.argv[3])
except ValueError:
	print("Latitude Error")
	usageprint()

try:
	for i in sys.argv[4:] :
		float(i) 
except ValueError:
	print("Temperature Error")
	usageprint()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create the first 'Render View' (for the first window)
renderView1 = CreateView('RenderView')
renderView1.Set(
    ViewSize=[1920, 1080],
    InteractionMode='2D',
    CenterOfRotation=[latitude, longitude, 0.0],
    CameraPosition=[latitude, longitude, 64.20057971900172],
    CameraFocalPoint=[latitude, longitude, 0.0],
    CameraFocalDisk=1.0,
    CameraParallelScale=0.616332737900287, #zoomé
    OSPRayMaterialLibrary=materialLibrary1,
)

# Create the second 'Render View' (for the second window)
renderView2 = CreateView('RenderView')
renderView2.Set(
    ViewSize=[1920, 1080],
    InteractionMode='2D',
    CenterOfRotation=[2.0, 46.0, 0.0],
    CameraPosition=[2.0, 46.0, 34.20057971900172],
    CameraFocalPoint=[2.0, 46.0, 5.8441357],
    CameraFocalDisk=1.0,
    CameraParallelScale=5.5,
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
    ResultArrayName='VentVecteurMs',
    Function='u10*iHat+v10*jHat',
)

# create a new 'Calculator'
ventCalculatorKmH = Calculator(registrationName='VentCalculatorKmH', Input=ventCalculator)
ventCalculatorKmH.Set(
    ResultArrayName='VentVecteur',
    Function='VentVecteurMs*3.6',
)

# create a new 'Extract Subset'
ventSubset = ExtractSubset(registrationName='VentSubset', Input=ventCalculatorKmH)
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
departements20140306100mshp = GDALVectorReader(registrationName='departements-20140306-100m.shp', FileName='departements-20140306-100m-shp/departements-20140306-100m.shp')

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

# get color transfer function for 'Temperature'
temperatureLUT = GetColorTransferFunction("Temperature_View1")

# Get actual temperature range
vmin, vmax = temperatureSubset.GetPointDataInformation().GetArray('Temperature').GetRange()
rgb_points = []

if ShowIsolines:
    # Define isoline thresholds including min/max
    seuils_temperature = [vmin] + sorted([float(i) for i in sys.argv[4:] if vmin <= float(i) <= vmax]) + [vmax]

    # Number of intervals
    N = len(seuils_temperature) - 1

    # Colormap
    cmap = plt.get_cmap("coolwarm", N)

    for i in range(N):
        val_start = seuils_temperature[i]
        val_end = seuils_temperature[i+1]
        r, g, b, _ = cmap(i)
        
        # Start of interval
        rgb_points.extend([val_start, r, g, b])
        # Just before end of interval
        rgb_points.extend([val_end, r, g, b])
    
    # Apply to LUT
    temperatureLUT.RGBPoints = rgb_points
    temperatureLUT.ColorSpace = "RGB"
    temperatureLUT.Discretize = N
    temperatureLUT.RescaleTransferFunction(seuils_temperature[0], seuils_temperature[-1])

else:
    temperatureLUT.NumberOfTableValues = 12
    temperatureLUT.RescaleTransferFunction(vmin,vmax)

# Assign to display
tempratureSubdivisionDisplay.LookupTable = temperatureLUT
tempratureSubdivisionDisplay.ColorArrayName = ['POINTS', 'Temperature']
tempratureSubdivisionDisplay.SetScalarBarVisibility(renderView1, True)

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
    AmbientColor=[1.0, 1.0, 1.0],
    ColorArrayName=[None, ''],
    DiffuseColor=[1.0, 1.0, 1.0],
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
temperatureLUTColorBar.LabelFormat = "%-2.1f"
temperatureLUTColorBar.RangeLabelFormat = "%-2.1f"

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
temperatureLUT2 = GetColorTransferFunction('Temperature_View2')

if (ShowIsolines):    
    temperatureLUT2.RGBPoints = rgb_points
    temperatureLUT2.ColorSpace = "RGB"
    temperatureLUT2.Discretize = N
    temperatureLUT2.RescaleTransferFunction(seuils_temperature[0], seuils_temperature[-1])
else:
    temperatureLUT2.NumberOfTableValues = 12
    temperatureLUT2.RescaleTransferFunction(vmin,vmax)

# trace defaults for the display properties.
tempratureSubdivisionDisplay2.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 'Temperature'],
    LookupTable=temperatureLUT2,
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
		LookupTable=temperatureLUT2,
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
    AmbientColor=[1.0, 1.0, 1.0],
    ColorArrayName=[None, ''],
    DiffuseColor=[1.0, 1.0, 1.0],
    LineWidth=2.0,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
ventFlechesDisplay2.ScaleTransferFunction.Points = [5.01715033100156, 0.0, 0.5, 0.0, 9.782604853913682, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
ventFlechesDisplay2.OpacityTransferFunction.Points = [5.01715033100156, 0.0, 0.5, 0.0, 9.782604853913682, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for temperatureLUT in view renderView1
temperatureLUTColorBar2 = GetScalarBar(temperatureLUT2, renderView2)
temperatureLUTColorBar2.Set(
    WindowLocation='Upper Right Corner',
    Title='Temperature',
    ComponentTitle='',
)

temperatureLUTColorBar2.LabelFormat = "%-2.1f"
temperatureLUTColorBar2.RangeLabelFormat = "%-2.1f"


# set color bar visibility
temperatureLUTColorBar2.Visibility = 1

# show color legend
tempratureSubdivisionDisplay2.SetScalarBarVisibility(renderView2, True)

if (ShowIsolines) :
	# show color legend
	temperatureIsolinesDisplay2.SetScalarBarVisibility(renderView2, True)

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
# Add listener to change frame
# ----------------------------------------------------------------

timesteps = timeKeeper2.TimestepValues
current = {'i': 0}

def next_frame(obj, event):
    key = obj.GetKeySym()

    if key != 'n':
        return

    current['i'] = (current['i'] + 1) % len(timesteps)
    timeKeeper2.Time = timesteps[current['i']]
    timeKeeper1.Time = timesteps[current['i']]
    RenderAllViews()

    print("Frame:", current['i'])

renderView1.GetInteractor().AddObserver("KeyPressEvent", next_frame)
renderView2.GetInteractor().AddObserver("KeyPressEvent", next_frame)


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
## Save a screenshot of both viex
SaveScreenshot("testParaview1.png", view=renderView1)
SaveScreenshot("testParaview2.png", view=renderView2)
#
## Interact with the view, usefull when running from pvpython
Interact()
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
