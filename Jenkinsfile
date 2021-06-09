pipeline {
    agent {
        kubernetes {
            yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: shell
    image: python:3.8
    command:
    - sleep
    args:
    - infinity
'''
            defaultContainer 'shell'
        }
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/hvv19890828/py-py-py-py-pyy.git'
                sh 'pip3 install mysql-connector-python && pip3 install requests'
                sh 'python3 test.py'
            }
        }
        stage('Main') {
            steps {
                sh 'pip3 install mysql-connector-python && pip3 install requests'
                sh 'python3 test.py'
            }
        }
        stage('Chuck') {
            steps {
                chuckNorris()
            }
        }
    }
}
