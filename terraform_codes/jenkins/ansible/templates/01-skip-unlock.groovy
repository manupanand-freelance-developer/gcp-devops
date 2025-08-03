import jenkins.model.*
import jenkins.install.*

def instance = Jenkins.getInstance()
instance.setInstallState(InstallState.INITIAL_SETUP_COMPLETED)
instance.save()

// copy file to location /var/lib/jenkins/init.groovy.d  directory, owner jenkins, group jenkins