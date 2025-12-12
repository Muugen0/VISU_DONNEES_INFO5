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
    CenterOfRotation=[-2.9865554327534554, 17.00513539215395, 0.0],
    UseLight=0,
    CameraPosition=[4.482935863875653, 46.80327201197917, 271.4051587004233],
    CameraFocalPoint=[4.482935863875653, 46.80327201197917, 0.0],
    CameraFocalDisk=1.0,
    CameraParallelScale=10.441445490874104,
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
a12dec6hnc = NetCDFReader(registrationName='12dec6h.nc', FileName=['/home/pierre/Documents/Info5/Visu/Projet/ParaviewData/12dec/12dec6h.nc'])
a12dec6hnc.Set(
    Dimensions='(latitude, longitude)',
    SphericalCoordinates=0,
)

# create a new 'GDAL Vector Reader'
departements20140306100mshp = GDALVectorReader(registrationName='departements-20140306-100m.shp', FileName='/home/pierre/Documents/Info5/Visu/Projet/departements-20140306-100m-shp/departements-20140306-100m.shp')

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from a12dec6hnc
a12dec6hncDisplay = Show(a12dec6hnc, renderView1, 'StructuredGridRepresentation')

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
a12dec6hncDisplay.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 't2m'],
    LookupTable=t2mLUT,
)

# show data from departements20140306100mshp
departements20140306100mshpDisplay = Show(departements20140306100mshp, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
departements20140306100mshpDisplay.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', ''],
    Assembly='Hierarchy',
)

# setup the color legend parameters for each legend in this view

# get color legend/bar for t2mLUT in view renderView1
t2mLUTColorBar = GetScalarBar(t2mLUT, renderView1)
t2mLUTColorBar.Set(
    WindowLocation='Upper Right Corner',
    Title='t2m',
    ComponentTitle='',
)

# set color bar visibility
t2mLUTColorBar.Visibility = 1

# show color legend
a12dec6hncDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 't2m'
t2mPWF = GetOpacityTransferFunction('t2m')
t2mPWF.Set(
    Points=[256.45910092278245, 0.0, 0.5, 0.0, 290.7166854990885, 1.0, 0.5, 0.0],
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