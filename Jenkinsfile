pipeline {
    agent any
    trigger {
        pollSCM('H/5 * * * *')
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