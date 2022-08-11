pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git 'https://github.com/JerryGB7/flask-demo.git'

                // Run venv
                sh "python3 -m venv .venv"

                // Run pip install
                sh "pip3 install -r requirements-dev.txt"
                
                // Run pytest
                sh "python3 -m pytest app-test.py"
            }
        }
        stage('docker'){
            steps{
                withCredentials([string(credentialsId: 'Dockerpw', variable: 'DOCKER')]) {
                    sh "docker login -u jerrygb7 -p {Docker}"
                }
            }
        }
    }
}
