pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/johnzama/barcode-ci-cd.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('barcode-generator')
                }
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests (if you have any tests defined)'
                // Implement test scripts here
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Run the container
                    docker.image('barcode-generator').run('-it')
                }
            }
        }
    }

    post {
        always {
            cleanWs() // Clean up the workspace after the build
        }
    }
}
