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

    environment {
         VERS    = sh(returnStdout:  true, script: 'git tag | grep -E "^v[[:digit:]]{1,3}\\.[[:digit:]]{1,3}\\.[[:digit:]]{1,3}$" | sort -V | tail -1').trim()
         FULL_BN = sh(returnStdout:  true, script: 'BNMB=${BUILD_NUMBER} ; ZERO_DIGIT_AMOUNT=$((4-${#BNMB})) ; i=1 ; while [ $i -le $ZERO_DIGIT_AMOUNT ] ; do PREF=$PREF"0" ; i=$(( i + 1 )) ; done ; echo $PREF$BNMB').trim()
    }

    stages {
        stage('Test') {
            when { expression { env.GIT_BRANCH.startsWith("hvv19890828/ma") == false } }
            steps {
                sh 'pip3 install mysql-connector-python && pip3 install requests'
                sh 'python3 test.py'
            }
        }
        stage('Image Build') {
            when { expression { env.GIT_BRANCH == 'hvv19890828/master' } }
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
