pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull your code from Git
                git branch: 'main', url: 'https://github.com/vickey-k/test1.git'
            }
        }

        stage('Run Script') {
            steps {
                echo 'Running test.py...'
                sh 'python3 test.py'
		sh 'python3 prime.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed!'
        }
    }
}