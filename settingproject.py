"""
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>deviceOrientationLandscapeLeft</key>
	<true/>
	<key>deviceOrientationLandscapeRight</key>
	<true/>
	<key>deviceOrientationPortrait</key>
	<false/>
	<key>deviceOrientationUpsideDown</key>
	<false/>
	<key>exporter</key>
	<string>ccbi</string>
	<key>fileType</key>
	<string>CocosBuilderProject</string>
	<key>fileVersion</key>
	<integer>1</integer>
	<key>flattenPaths</key>
	<false/>
	<key>generatedSpriteSheets</key>
	<dict/>
	<key>javascriptBased</key>
	<false/>
	<key>javascriptMainCCB</key>
	<string></string>
	<key>needRepublish</key>
	<false/>
	<key>onlyPublishCCBs</key>
	<false/>
	<key>publishDirectory</key>
	<string>../../res</string>
	<key>publishDirectoryAndroid</key>
	<string>Published-Android</string>
	<key>publishDirectoryHTML5</key>
	<string>Published-HTML5</string>
	<key>publishEnabledAndroid</key>
	<false/>
	<key>publishEnabledHTML5</key>
	<false/>
	<key>publishEnablediPhone</key>
	<true/>
	<key>publishResolutionHTML5_height</key>
	<integer>320</integer>
	<key>publishResolutionHTML5_scale</key>
	<integer>1</integer>
	<key>publishResolutionHTML5_width</key>
	<integer>480</integer>
	<key>publishResolution_</key>
	<true/>
	<key>publishResolution_hd</key>
	<true/>
	<key>publishResolution_ipad</key>
	<true/>
	<key>publishResolution_ipadhd</key>
	<true/>
	<key>publishResolution_large</key>
	<true/>
	<key>publishResolution_medium</key>
	<true/>
	<key>publishResolution_small</key>
	<true/>
	<key>publishResolution_xlarge</key>
	<true/>
	<key>publishResolution_xsmall</key>
	<true/>
	<key>publishToZipFile</key>
	<false/>
	<key>resourceAutoScaleFactor</key>
	<integer>2</integer>
	<key>resourcePaths</key>
	<array>
		<dict>
			<key>path</key>
			<string>.</string>
		</dict>
	</array>
	<key>versionStr</key>
	<string>Version: 3.0-alpha5
GitHub: 76499877e8
</string>
</dict>
</plist>
"""

class ProjectSettings:
    projectPath = ""
    resourcePaths = []
    generatedSpriteSheets = {}
    breakpoints = {}
    
    publishDirectory = "Published-iOS"
    publishDirectoryAndroid = "Published-Android"
    publishDirectoryHTML5 = "Published-HTML5"
    
    publishEnablediPhone = True
    
    """
    NSString* projectPath;
    NSMutableArray* resourcePaths;
    NSMutableDictionary* generatedSpriteSheets;
    NSMutableDictionary* breakpoints;
    
    NSString* publishDirectory;
    NSString* publishDirectoryAndroid;
    NSString* publishDirectoryHTML5;
    
    BOOL publishEnablediPhone;
    BOOL publishEnabledAndroid;
    BOOL publishEnabledHTML5;
    
    BOOL publishResolution_;
    BOOL publishResolution_hd;
    BOOL publishResolution_ipad;
    BOOL publishResolution_ipadhd;
    BOOL publishResolution_xsmall;
    BOOL publishResolution_small;
    BOOL publishResolution_medium;
    BOOL publishResolution_large;
    BOOL publishResolution_xlarge;
    
    int publishResolutionHTML5_width;
    int publishResolutionHTML5_height;
    int publishResolutionHTML5_scale;
    
    BOOL isSafariExist;
    BOOL isChromeExist;
    BOOL isFirefoxExist;
    
    BOOL flattenPaths;
    BOOL publishToZipFile;
    BOOL javascriptBased;
    BOOL onlyPublishCCBs;
    NSString* exporter;
    NSMutableArray* availableExporters;
    NSString* javascriptMainCCB;
    BOOL deviceOrientationPortrait;
    BOOL deviceOrientationUpsideDown;
    BOOL deviceOrientationLandscapeLeft;
    BOOL deviceOrientationLandscapeRight;
    int resourceAutoScaleFactor;
    
    NSString* versionStr;
    BOOL needRepublish;   
    """
    def initWithSerialization(self, dictsettings):
        if dictsettings.get("fileType") != "CocosBuilderProject":
            return False
        
        # Read settings
        self.resourcePaths = dictsettings.get("resourcePaths")