pipeline{
    environment {
        registry = "jerrygb7/flask"
        registryCredential = 'Dockerhub'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Cloning our Git'){
            steps{
                git 'https://github.com/JerryGB7/flask-demo.git'
            }
        }
        stage('Build the image'){
            steps{
                script{
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Deploy our image'){
            steps{
                script{
                    docker.withRegistry('', registryCredential){
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Run our image'){
            steps{
                script{
                    docker.withRegistry('', registryCredential){
                        dockerImage.run()
                    }
                }
            }
        }
    }
}
