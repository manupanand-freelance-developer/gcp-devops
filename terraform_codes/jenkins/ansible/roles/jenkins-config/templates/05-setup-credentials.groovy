import jenkins.model.*
import com.cloudbees.plugins.credentials.*
import com.cloudbees.plugins.credentials.impl.*
import com.cloudbees.plugins.credentials.domains.*
import com.cloudbees.plugins.credentials.CredentialsScope

// Path to your JSON key file
def keyFilePath = "/var/lib/jenkins/gcp-service-key.json"
def keyFile = new File(keyFilePath)
if (!keyFile.exists()) {
    println("Key file not found at ${keyFilePath}")
    return
}

// Create a new Secret File credential
def credentialsStore = Jenkins.instance.getExtensionList(
        'com.cloudbees.plugins.credentials.SystemCredentialsProvider'
    )[0].getStore()

def secretFile = new FileCredentialsImpl(
    CredentialsScope.GLOBAL,
    "gcp-service-key",          // ID
    "GCP Service Account Key",  // Description
    keyFile
)

credentialsStore.addCredentials(Domain.global(), secretFile)
println("Added GCP service account key as Jenkins credential")
