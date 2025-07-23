pipeline {
    agent any
    triggers {
        pollSCM('*/2 * * * *')
    }
    stages {
        stage  ('Build') {
            steps {
                echo "Build phase"
                powershell '''
                cd calculator-app
                python -m pip install -r requirements.txt
                '''
            }
        }
        stage ('Test') {
            steps {
                echo "test phase"
                powershell '''
                cd calculator-app
                python calculator.py --test 5 3
                python calculator.py --test 515151551515 525252252848887889154841 
                '''
            }
        }
        stage ("deliver") {
            steps {
                echo "successfully delivered"
            }
        }
    }
}