pipeline {
    agent {
        kubernetes {
            yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
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

    environment {
         VERS = sh(returnStdout:  true, script: 'git tag | grep -E "^x[[:digit:]]{1,3}\\.[[:digit:]]{1,3}$" | sort -V | tail -1').trim()
    }

    stages {
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
