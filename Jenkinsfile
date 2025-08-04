pipeline {
    agent any
    stages{
        stage('Compile'){
            steps{
                sh 'echo build/compile'
            }
        }
        stage('Test Cases'){
            steps{
                sh 'echo test cases'
            }
        }
        stage('Docker build'){
            steps{
                sh 'echo docker build'
            }
        }
        stage('Docker push images'){
            steps{
                sh 'echo docker push images'
            }
        }
        stage('Deploy to dev env'){
            when{
                expression{ env.BRANCH_NAME != 'main'}
            }
            steps{
                sh 'echo deploy to dev env'
            }
        }
        
    }

}