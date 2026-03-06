pipeline {
    agent any

    environment {
        IMAGE_NAME = "semantic-search"
        CONTAINER_NAME = "semantic-search-container"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker run -d \
                -p 8000:8000 \
                --name $CONTAINER_NAME \
                $IMAGE_NAME
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker ps'
            }
        }
    }
}
