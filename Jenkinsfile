pipeline {
    agent any

    stages {
        stage('Run Analyzer') {
            steps {
                bat '"C:\\Users\\ejyas\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" analyzer.py'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.txt', fingerprint: true
            }
        }
    }
}
