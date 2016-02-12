import pyglet

def setSpriteFrameForNode(node, prop, spriteFile, spriteSheetFile):
    # TODO:@twenty0ne
    # CCSpriteFrame
    # spriteFrame = None
    if spriteFile and spriteFile != "":
        # Create a sprite frame for the single image file
        # TODO:@twenty0ne
        fileName = "test/" + spriteFile
        image = pyglet.resource.image(fileName)
        node.image = image