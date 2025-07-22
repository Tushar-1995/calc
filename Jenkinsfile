pipeline {
    agent any
    triggers {
        pollSCM('H/2 * * * *')
    }
    stages {
        stage  ('Build') {
            steps {
                echo "Build phase"
            }
        }
        stage ('Test') {
            steps {
                echo "test phase"
            }
        }
        stage ("deploy") {
            steps {
                echo "deliver phase"
            }
        }
    }
}