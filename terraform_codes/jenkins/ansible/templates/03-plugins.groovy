def plugins =[
"workflow-multibranch"] #

def instance = Jenkins.getInstance()
def pm = instance.getPluginmanager()
def uc = instance.getUpdateCenter()

plugins.each{ pluginName->
    if(!pm.getPlugin(pluginName)){
        def plugin= uc.getPlugin(pluginName)
        if(plugin){
            println("Installing"+pluginName)
            plugin.deploy()
        } 
    }

}
instance.save()
instance.doSafeRestart()