pipeline{
    environment {
        registry = "jerrygb7/flask"
        registryCredential = 'Dockerhub'
        dockerImage = ''
        PATH = "$PATH:/opt/maven"
    }
    agent any
    stages {
        stage('Cloning our Git'){
            steps{
                git 'https://github.com/JerryGB7/flask-demo.git'
            }
        }
        stage ('Start running docker'){
            steps{
                catchError(buildResult: 'SUCCESS'){
                    sh 'systemctl start docker'
                }
            }
        }
        stage('Stop existing containers'){
            steps{
                catchError(buildResult: 'SUCCESS'){
                    sh 'docker stop flask-app'
                }
                catchError(buildResult: 'SUCCESS'){
                    sh 'docker rm -f flask-app'
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
        stage('SonarQube analysis') {
//    def scannerHome = tool 'SonarScanner 4.0';
            steps{
                withSonarQubeEnv('sonarqube-8.9.9') { 
               
                    sh "mvn sonar:sonar"
                }
            }
        }
    }
}
