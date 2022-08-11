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
        stage('Stop existing containers'){
            steps{
                catchError{
                    sh 'docker stop flask-app'
                }
                catchError{
                    sh 'docker stop flask-app'
                }
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
                        sh "docker run -d -p 5000:5000 --name flask-app $registry:$BUILD_NUMBER"
                    }
                }
            }
        }
    }
}
