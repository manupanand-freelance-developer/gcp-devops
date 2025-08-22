import jenkins.model.*
import hudson.model.*
import hudson.PluginWrapper

def pluginsToInstall = [
    "workflow-multibranch",
    "git",
    "pipeline-stage-view",
    "blueocean",
    "generic-webhook-trigger",
    "cloudbees-credentials",
    "plain-credentials",
    "credentials-binding",
    "email-ext",
    "google-source-plugin",
    "credentials",
    "google-kubernetes-engine",
    "github-branch-source",
    "github",
    "github-pullrequest",
    "nodejs"
]

// Reference Jenkins Plugin Manager and Update Center
def pluginManager = Jenkins.instance.pluginManager
def updateCenter = Jenkins.instance.updateCenter

pluginsToInstall.each { pluginName ->
    // Check if the plugin is already installed
    if (!pluginManager.getPlugin(pluginName)) {
        println "Installing plugin: ${pluginName}"
        def plugin = updateCenter.getPlugin(pluginName)

        if (plugin) {
            // Deploy plugin and wait for completion
            plugin.deploy(true).get()
            println "Successfully installed ${pluginName}"
        } else {
            println "Plugin ${pluginName} not found in update center"
        }
    } else {
        println "Plugin ${pluginName} is already installed"
    }
}

// Optionally save the Jenkins config if needed (not usually required for plugins)
Jenkins.instance.save()
