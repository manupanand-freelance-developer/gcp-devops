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
        stage('compile'){
            print 'compile'
        
        }
        stage('Test Cases'){
            print 'test case'
        
        }
    }
    
    
}