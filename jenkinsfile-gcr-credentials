pipeline {
    agent any
    stages {
        stage('Checkout CSR') {
            steps {
                withCredentials([file(credentialsId: 'gcp-service-key', variable: 'GCP_KEY_FILE')]) {
                    sh '''
                        export GOOGLE_APPLICATION_CREDENTIALS="$GCP_KEY_FILE"
                        gcloud auth activate-service-account --key-file="$GOOGLE_APPLICATION_CREDENTIALS"
                        gcloud source repos clone REPO_NAME --project=PROJECT_ID
                        cd REPO_NAME
                        git checkout my-branch
                    '''
                }
            }
        }
    }
}


