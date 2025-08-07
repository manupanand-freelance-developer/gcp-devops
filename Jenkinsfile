node {
    def branch = env.BRANCH_NAME
    def user = currentBuild.getBuildCauses('hudson.model.Cause$UserIdCause')[0]?.getUserId()

 
    if (branch.startsWith("feature/")) {
        stage('Checkout') {
            checkout scm
            echo "Branch: ${branch}"
            echo "Triggered by: ${user}"
            echo "trigeged"
        }

        stage('Build & Test') {
            echo "Building feature branch..."
        }

        stage('Deploy to Test') {
            echo "Deploying to test environment..."
        }

    } else if (branch == "master" || env.TAG_NAME) {
        stage('Build') {
            echo "Building production code..."
        }

        stage('Approval') {
            // Only admindev or admininfra can approve
            input message: "Approve deployment to PROD?", 
                  submitter: 'admindev,admininfra'
        }

        stage('Deploy to Production') {
            echo "Deploying to production..."
        }
    } else {
        echo "No matching deployment rule for this branch."
    }
}
