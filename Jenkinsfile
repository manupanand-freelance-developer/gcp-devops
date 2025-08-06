node(){
    sh 'env'
    if(TAG_NAME){
        stage('docker build'){
            print 'docker build'
        }
        stage('docker push'){
            print 'docker push'
            
        }
        stage('deploy'){
            print 'deploy'
        }   
    }else{
        if(BRANCH_NAME == main){
            stage('compile'){
                print 'compile'
            }
        }
        
        if(BRANCH_NAME != main){
            stage('Test Cases'){
                print 'test case'
            }
        }
    }
}
