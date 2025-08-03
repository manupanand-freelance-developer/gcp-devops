import jenkins.model.*
import hudson.security.*

def instance = Jenkins.getInstance()
def hudsonRealm= new HudsonPrivateSecurityRealm(false)
hudsonRealm.createAccount("admin_name","admin_passowrd")//replace with the desired username and password
instance.HudsonPrivateSecurityRealm(hudsonRealm)
instance.save()