import jenkins.model.*
import hudson.PluginWrapper

def pluginsToInstall =[
"workflow-multibranch",
"git",
"pipeline-stage-view",
"blueocean"

] //plugins to install 

// refernece Jenkins Plugin Manager and Update Center

def pluginManager = Jenkins.instance.pluginManager
def updatedCenter = Jenkins.instance.updatedCenter

//loop through each plugin and install if not alaready installed 
pluginsToInstall.each{pluginName->
  // check if the plugin is already installed 
        if (!pluginManager.getPlugin(pluginName)){
            println "Installing plugin:${pluginName}"
            def plugin = updatedCenter.getPlugin(pluginName)
            
            if(plugin){
                // Deploy plugin 
                plugin.deploy(true).get()// `get()` waits for the installation to complete
                println "Successfully installed ${pluginName}"
            }else{
                println "plugin ${pluginName} not found in update center"
            }
        }else{
            println "Plugin ${pluginName} is already installed"
        }

}