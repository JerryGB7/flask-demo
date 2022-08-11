pipeline{
    environment {
        registry = "jerrygb7/flask"
        registryCredential = 'Dockerhub'
        dockerImage = ''
        PATH = "$PATH:/opt/maven/bin"
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
        stage('Cleaning up'){
            steps{
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
        stage('SonarQube analysis') {
            steps{
                withSonarQubeEnv('sonarqube-8.9.9') { 
                // If you have configured more than one global server connection, you can specify its name
                    sh "mvn sonar:sonar"
                }
            }
        }
    }
}
