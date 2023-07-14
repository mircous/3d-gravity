class Mapmanager():
    def __init__(self): #block model,texture,color,model
        self.land = render.attachNewNode("Land")
        self.model = 'block.egg' # the cube model is in block.egg file
        self.texture = 'block.png' # cube texture
        self.lscolor = [(0.5, 0.3, 0.0, 1),
                    (0.2, 0.2, 0.3, 1),
                    (0.5, 0.5, 0.2, 1),
                    (0.0, 0.6, 0.0, 1)]#rgba
        #self.addBlock((0, 10, 0))
        self.color = (0.5, 0.3, 0.0, 1)

    def startNew(self):#Creating a node for the map
        self.land = render.attachNewNode("Land")

    def clear(self):
        self.land.removeNode()
        self.startNew()

    def addBlock(self,position):


        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.getColor(position[2])
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

    def getColor(self, z):
        if z < len(self.lscolor):
            return self.lscolor[z]
        else:
            return self.lscolor[len(self.lscolor) - 1]


    def loadLand(self,filename):
        self.clear
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(" ")
                for z in line:
                    for z0 in range(int(z)+1):
                        block = self.addBlock((x, y ,z0))
                    x += 1
                y += 1
