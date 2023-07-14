from direct.showbase.ShowBase import ShowBase
from direct.task.Task import Task
from mapmanager import *
from hero import *

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager () #create a map
        #self.model = loader.loadModel('models/environment')
        #self.model = loader.loadModel('Boeing707.egg')
        #self.model.reparentTo(render)
        #self.model.setScale(0.1)
        #self.model.setPos(-2, 25, -3)
        self.land.loadLand("land.txt")
        base.camLens.setFov(90)

        self.hero = Hero((5,5,5),self.land)
        self.taskMgr.add(self.update)

        
    def update(self, task):
        dt = globalClock.getDt()  # Get the time since the last frame
        self.hero.update(task)  # Call the update method in the Hero class

        # Additional update logic for your game...

        return Task.cont



base = Game()

base.run()
