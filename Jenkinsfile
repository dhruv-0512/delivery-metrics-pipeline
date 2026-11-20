pipeline {
    agent any

    stages {
        stage('Source Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
    steps {
        sh 'python3 -m venv venv'
        sh 'venv/bin/pip install -r requirements.txt'
    }
}git add Jenkinsfile
git commit -m "Use Python virtual environment in Jenkins"
git push

        stage('Test') {
    steps {
        sh 'python3 -m unittest test_app.py'
    }
}

        stage('Deploy') {
            steps {
                sh 'mkdir -p deployment'
                sh 'cp app.py requirements.txt deployment/'
                sh 'cp test_app.py deployment/'
            }
        }
    }

    post {
        success {
            echo 'Metrics exporter pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check stage logs.'
        }
    }
}