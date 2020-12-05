from mcpi.minecraft import Minecraft
mc=Minecraft.create() 
while True:

    temp=mc.events.pollBlockHits()
    if len(temp)>0:
        hit=temp[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        block=mc.getBlock(x,y,z)
        if block == 1:
            mc.setBlock(x,y,z,41)