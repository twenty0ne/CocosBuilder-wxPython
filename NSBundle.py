# Mac NSBundle clone

# TODO:@twenty0ne
# CocosBuilder-mac use NSBundle to manager Plugins
# 1.create my nsbundler class?
# 2.use plugins path array directly?
"""
plugInPaths = ("bundles/CCLabelBMFont", 
               "bundles/CCLabelTTF", 
               "bundles/CCLayer",
               "bundles/CCLayerColor",
               "bundles/CCLayerGradient",
               "bundles/CCMenu",
               "bundles/CCMenuItemImage",
               "bundles/CCNode",
               "bundles/CCParticleSystem",
               "bundles/CCScale9Sprite",
               "bundles/CCScrollView",
               "bundles/CCSprite")
"""

class NSBundle:
    def __init__(self):
        self._plugInPaths = ("bundles/CCLabelBMFont", 
                             "bundles/CCLabelTTF", 
                             "bundles/CCLayer",
                             "bundles/CCLayerColor",
                             "bundles/CCLayerGradient",
                             "bundles/CCMenu",
                             "bundles/CCMenuItemImage",
                             "bundles/CCNode",
                             "bundles/CCParticleSystem",
                             "bundles/CCScale9Sprite",
                             "bundles/CCScrollView",
                             "bundles/CCSprite")
        