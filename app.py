import os
from settingproject import *
import biplist

class App(object):
    def __init__(self):
        object.__init__(self)
        self.projectSettings = None
    
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