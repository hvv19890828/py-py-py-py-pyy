pipeline {
    agent {
        kubernetes {
            yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: python
    image: python:3.8
    command:
    - sleep
    args:
    - infinity
  - name: kaniko
    workingDir: /tmp/jenkins
    image: gcr.io/kaniko-project/executor:debug
    imagePullPolicy: Always
    command:
    - /busybox/cat
    tty: true
    volumeMounts:
      - name: jenkins-docker-cfg
        mountPath: /kaniko/.docker
  volumes:
  - name: jenkins-docker-cfg
    projected:
      sources:
      - secret:
          name: jendocksec
          items:
            - key: .dockerconfigjson
              path: config.json
'''
            defaultContainer 'python'
        }
    }
    stages {
        stage('Main') {
            steps {
                sh 'pip3 install mysql-connector-python && pip3 install requests'
                sh 'python3 test.py'
            }
        }
        VERS = sh(returnStdout:  true, script: "git tag --sort=-creatordate | head -n 1").trim()
        stage('Get GIT Tag') {
            steps {
                container("alpine") {
                    sh 'export VERS=`git tag | grep -E "^x[[:digit:]]{1,3}\\.[[:digit:]]{1,3}$" | sort -V | tail -1`'
                }
            }
        }
        stage('Image Build') {
            steps {
                container(name: 'kaniko', shell: '/busybox/sh') {
                    sh '''#!/busybox/sh
                    /kaniko/executor --context `pwd` \
                        --destination hvv19890828/py-py-py-py-pyy:${VERS}
                    '''
                }
            }
        }
        stage('Chuck') {
            steps {
                chuckNorris()
            }
        }
    }
}
