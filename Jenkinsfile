pipeline {
    agent any
    
    triggers {
        // Poll GitHub every 2 minutes
        pollSCM('H/2 * * * *')
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/khamis9/csc263'
            }
        }
        
        stage('Build in Minikube Docker') {
            steps {
                bat '''
                REM === Switch Docker to Minikube Docker ===
                FOR /F "tokens=*" %%i IN ('minikube -p minikube docker-env --shell=cmd') DO %%i
                
                REM === Build Django image inside Minikube Docker ===
                docker build -t mydjangoapp:latest .
                '''
            }
        }
        
        stage('Deploy to Minikube') {
            steps {
                bat '''
                REM === Apply the updated deployment manifest ===
                minikube -p minikube kubectl -- apply -f deployment.yaml
                
                REM === Ensure the rollout completes ===
                minikube -p minikube kubectl -- rollout status deployment/django-deployment
                '''
            }
        }
    }
}