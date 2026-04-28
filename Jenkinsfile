pipeline {
    agent any

    stages {
        stage('Run Analyzer') {
            steps {
                bat 'python analyzer.py'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.txt', fingerprint: true
            }
        }
    }
}
