pipeline {
    agent any;
    stages {
        stage('Code Quality') {
            steps {
                sh 'echo Checking code quality'
            }            
        }
        stage('Unit Test') {
            steps {
               sh 'echo Testing the Applications'
            }
        }
        stage('Build') {
            steps {
               sh 'echo Creating application Package'
            }
        }
        stage('Delivery') {
            steps {
               sh 'echo Uploading the artifact to a repository'
            }
        }
        stage('Deploy') {
            steps {
               sh 'echo Deploying the Application'
            }
        }
    }
}
