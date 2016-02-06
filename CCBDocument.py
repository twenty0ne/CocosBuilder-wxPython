class CCBDocument():
    fileName = ""
    exportPath = ""
    exportPlugIn = ""
    exportFlattenPaths = False
    docData = {}
    lastEditedProperty = ""
    isDirty = False
    stageScrollOffset = (0,0)
    stageZoom = 1
    
    resolutions = []
    currentResolution = 0
    
    sequences = []
    currentSequenceId = 0