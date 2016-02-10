#import sys
#import os
#sys.path.insert(0, os.path.join(os.path.dirname(__file__), './cocos/'))
#import cocos

from ProjectSettings import *
import biplist
from CCBDocument import CCBDocument
from PlugInManager import *
import CCBReaderInternal

#TODO:@twenty0ne
# if import CocosScene here, will freeze
import CocosScene
#import CocosScene

class App(object):
    def __init__(self):
        object.__init__(self)
        self.projectSettings = None
        
        self._currentDocument = None
        
        # Load plug-ins
        thePlugIn.loadPlugIns()
    
    def openProject(self, filename):
        """
        // Close currently open project
        [self closeProject];
        
        // Add to recent list of opened documents
        [[NSDocumentController sharedDocumentController] noteNewRecentDocumentURL:[NSURL fileURLWithPath:fileName]];
        
        NSMutableDictionary* projectDict = [NSMutableDictionary dictionaryWithContentsOfFile:fileName];
        if (!projectDict)
        {
            [self modalDialogTitle:@"Invalid Project File" message:@"Failed to open the project. File may be missing or invalid."];
            return NO;
        }
        
        ProjectSettings* project = [[[ProjectSettings alloc] initWithSerialization:projectDict] autorelease];
        if (!project)
        {
            [self modalDialogTitle:@"Invalid Project File" message:@"Failed to open the project. File is invalid or is created with a newer version of CocosBuilder."];
            return NO;
        }
        project.projectPath = fileName;
        [project store];
        self.projectSettings = project;
        
        [self updateResourcePathsFromProjectSettings];
        
        BOOL success = [self checkForTooManyDirectoriesInCurrentProject];
        
        if (!success) return NO;
        
        // Load autocompletions for all JS files
        NSArray* jsFiles = [CCBFileUtil filesInResourcePathsWithExtension:@"js"];
        for (NSString* jsFile in jsFiles)
        {
            [[JavaScriptAutoCompleteHandler sharedAutoCompleteHandler] loadLocalFile:[resManager toAbsolutePath:jsFile]];
        }
        
        // Update the title of the main window
        [window setTitle:[NSString stringWithFormat:@"CocosBuilder - %@", [fileName lastPathComponent]]];
    
        // Start local web server
        NSString* docRoot = [projectSettings.publishDirectoryHTML5 absolutePathFromBaseDirPath:[projectSettings.projectPath stringByDeletingLastPathComponent]];
        [[CCBHTTPServer sharedHTTPServer] start:docRoot];
        
        // Open ccb file for project if there is only one
        NSArray* resPaths = project.absoluteResourcePaths;
        if (resPaths.count > 0)
        {
            NSString* resPath = [resPaths objectAtIndex:0];
            
            NSArray* resDir = [[NSFileManager defaultManager] contentsOfDirectoryAtPath:resPath error:NULL];
            
            int numCCBFiles = 0;
            NSString* ccbFile = NULL;
            for (NSString* file in resDir)
            {
                if ([file hasSuffix:@".ccb"])
                {
                    ccbFile = file;
                    numCCBFiles++;
                    
                    if (numCCBFiles > 1) break;
                }
            }
            
            if (numCCBFiles == 1)
            {
                // Open the ccb file
                [self openFile:[resPath stringByAppendingPathComponent:ccbFile]];
            }
        }
        
        return YES;   
        """
        # TODO:@twenty0ne
        # Close currently open project
        plist = biplist.readPlist(filename)
        project_setting = ProjectSettings()
        project_setting.initWithSerialization(plist)
        self.projectSettings = project_setting
        
        self.updateResourcePathsFromProjectSettings()
        
        
        
    def updateResourcePathsFromProjectSettings(self):
        pass
    
    def openFile(self, fileName):
        doc = biplist.readPlist(fileName)
        newDoc = CCBDocument()
        newDoc.fileName
        newDoc.docData = doc
        newDoc.exportPath = doc.get("exportPath")
        newDoc.exportPlugIn = doc.get("exportPlugIn")
        newDoc.exportFlattenPaths = doc.get("exportFlattenPaths")
        
        self.switchToDocument(newDoc)
        
        self.addDocument(newDoc)
        self.hasOpenedDocument = True
        
        # Remove selections
        self.setSelectedNodes(None)
        
        # Make sure timeline is up to date
        
    def switchToDocument(self, document, forceReload=False):
        if not forceReload and self._currentDocument and \
           document.filename == self._currentDocument.fileName:
            return
        
        self.prepareForDocumentSwitch()
        self._currentDocument = document
        
        self.replaceDocumentData(document.docData)
        
        self.updateResolutionMenu()
        self.updateTimelineMenu()
        self.updateStateOriginCenteredMenu()
        
        # TODO:@twenty0ne
        # CocosScene* cs = [CocosScene cocosScene]
        # [cs setStageZoom:document.stageZoom]
        # [cs setScrollOffset:document.stageScrollOffset]
    
    def addDocument(self, document):
        pass
    
    def setSelectedNodes(self, selection):
        pass
    
    def prepareForDocumentSwitch(self):
        pass
    
    def replaceDocumentData(self, doc):
        # TODO:@twenty0ne
        # Process contents
        loadedRoot = CCBReaderInternal.nodeGraphFromDocumentDictionary(doc, (650,650))
        
        # Replace open document
        self._selectedNodes = None
        CocosScene.theCocosScene.replaceRootNodeWith(loadedRoot)
        
    def updateResolutionMenu(self):
        pass
    
    def updateTimelineMenu(self):
        pass
    
    def updateStateOriginCenteredMenu(self):
        pass
#
theApp = App()