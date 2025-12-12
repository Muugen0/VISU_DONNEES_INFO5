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
    CenterOfRotation=[2.0, 46.45000076293945, 0.0],
    CameraPosition=[3.039810611739514, 46.37270127095975, 64.20057971900172],
    CameraFocalPoint=[3.039810611739514, 46.37270127095975, 0.0],
    CameraFocalDisk=1.0,
    CameraParallelScale=11.349178838809015,
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

# create a new 'GDAL Vector Reader'
departements20140306100mshp = GDALVectorReader(registrationName='departements-20140306-100m.shp', FileName='/home/pierre/Documents/Info5/Visu/VISU_DONNEES_INFO5/Projet/departements-20140306-100m-shp/departements-20140306-100m.shp')

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=a12dec6hnc)
calculator1.Set(
    ResultArrayName='Temperature',
    Function='t2m - 273.15',
)

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=calculator1)
calculator2.Set(
    ResultArrayName='VentVecteur',
    Function='u10*iHat+v10*jHat',
)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from departements20140306100mshp
departements20140306100mshpDisplay = Show(departements20140306100mshp, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
departements20140306100mshpDisplay.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', ''],
    Assembly='Hierarchy',
)

# show data from calculator2
calculator2Display = Show(calculator2, renderView1, 'RectilinearGridRepresentation')

# get color transfer function/color map for 'VentVecteur'
ventVecteurLUT = GetColorTransferFunction('VentVecteur')
ventVecteurLUT.Set(
    RGBPoints=GenerateRGBPoints(
        range_min=0.006810075996320468,
        range_max=20.409033997143062,
    ),
    ScalarRangeInitialized=1.0,
)

# trace defaults for the display properties.
calculator2Display.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 'VentVecteur'],
    LookupTable=ventVecteurLUT,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
calculator2Display.ScaleTransferFunction.Points = [-16.690899077217523, 0.0, 0.5, 0.0, 17.56668549908852, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
calculator2Display.OpacityTransferFunction.Points = [-16.690899077217523, 0.0, 0.5, 0.0, 17.56668549908852, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for ventVecteurLUT in view renderView1
ventVecteurLUTColorBar = GetScalarBar(ventVecteurLUT, renderView1)
ventVecteurLUTColorBar.Set(
    Title='VentVecteur',
    ComponentTitle='Magnitude',
)

# set color bar visibility
ventVecteurLUTColorBar.Visibility = 1

# show color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'VentVecteur'
ventVecteurPWF = GetOpacityTransferFunction('VentVecteur')
ventVecteurPWF.Set(
    Points=[0.006810075996320468, 0.0, 0.5, 0.0, 20.409033997143062, 1.0, 0.5, 0.0],
    ScalarRangeInitialized=1,
)

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation scene

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper

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

# ----------------------------------------------------------------
# restore active source
SetActiveSource(calculator2)
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