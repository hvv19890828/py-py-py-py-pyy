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
  - name: pysql
    image: mysql
    env:
    - name: MYSQL_DATABASE
      value: "hvv"
    - name: MYSQL_ROOT_PASSWORD
      value: "user1!"
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
        }
    }

    options {
       buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
    }

    environment {
         VERS    = sh(returnStdout:  true, script: 'git tag | grep -E "^v[[:digit:]]{1,3}\\.[[:digit:]]{1,3}\\.[[:digit:]]{1,3}$" | sort -V | tail -1').trim()
         FULL_BN = sh(returnStdout:  true, script: 'SIMPLE_BN=${BUILD_NUMBER} ; ZERO_DIGIT_AMOUNT=$((4-${#SIMPLE_BN})) ; i=1 ; while [ $i -le $ZERO_DIGIT_AMOUNT ] ; do PREF=$PREF"0" ; i=$(( i + 1 )) ; done ; echo $PREF$SIMPLE_BN').trim()
         WEBHOOK_URL                 = credentials('teamsconnectionstr')
    }

    stages {
        stage('Tests') {
            parallel {
                stage('Windows Agent Test Step') {
                    agent {
                       label 'windows'
                    }
                    steps {
                       bat 'C:\\Users\\ViacheslavHudzovskyi\\AppData\\Local\\Programs\\Python\\Python39\\python.exe test.py 3'
                    }
                }
                stage('Linux Agent Test Step') {
                    steps {
                       container('python') {
                          sh 'pip3 install mysql-connector-python && pip3 install requests'
                          sh 'python3 test.py 3'
                       }
                    }
                }
            }
        }
        stage('Image Build') {
            when { expression { env.GIT_BRANCH.startsWith("hvv19890828/master") == true } }
            steps {
                container(name: 'kaniko', shell: '/busybox/sh') {
                    sh '''#!/busybox/sh
                    /kaniko/executor --context `pwd` \
                        --destination hvv19890828/py-py-py-py-pyy:${VERS}-${FULL_BN} \
                        --destination hvv19890828/py-py-py-py-pyy:latest
                    '''
                }
            }
        }
    }
    post {
        always {
             chuckNorris()
             publishHTML (target : [allowMissing: false,
                         alwaysLinkToLastBuild: true,
                         keepAll: true,
                         reportDir: 'coverage-report/html',
                         reportFiles: 'index.html',
                         reportName: 'My Reports',
                         reportTitles: 'The Report'])
             office365ConnectorSend webhookUrl: "${WEBHOOK_URL}"
        }
    }
}
