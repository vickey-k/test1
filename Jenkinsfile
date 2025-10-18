pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Get code from GitHub
                git branch: 'main', url: 'https://github.com/vickey-k/test1.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'python setup.py build'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'pytest tests/'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh './deploy.sh'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}
