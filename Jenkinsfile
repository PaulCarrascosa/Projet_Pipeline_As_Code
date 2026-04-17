pipeline {
    agent any

    options {
        timeout(time: 1, unit: 'HOURS')
        timestamps()
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo '========== Checking out source code =========='
                    checkout scm
                }
            }
        }

        stage('Environment Setup') {
            steps {
                script {
                    echo '========== Setting up environment =========='
                    sh '''
                        python --version
                        python -m pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Lint') {
            steps {
                script {
                    echo '========== Running code linting =========='
                    sh '''
                        pip install flake8 pylint
                        flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics || true
                        pylint src --fail-under=7.0 || true
                    '''
                }
            }
        }

        stage('Unit Tests') {
            steps {
                script {
                    echo '========== Running unit tests =========='
                    sh '''
                        pip install pytest pytest-cov pytest-asyncio
                        pytest tests/ -v --cov=src --cov-report=xml --cov-report=html --junitxml=test-results.xml
                    '''
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    echo '========== Running SonarQube analysis =========='
                    sh '''
                        pip install sonarcube-python-client
                        sonar-scanner \
                            -Dsonar.projectKey=library-app \
                            -Dsonar.sources=src \
                            -Dsonar.tests=tests \
                            -Dsonar.host.url=${SONAR_HOST_URL} \
                            -Dsonar.login=${SONAR_LOGIN} \
                            -Dsonar.python.coverage.reportPaths=coverage.xml \
                            -Dsonar.exclusions=venv/**,alembic/**,.git/**
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo '========== Building Docker image =========='
                    sh '''
                        docker build -t library-app:${BUILD_NUMBER} .
                        docker tag library-app:${BUILD_NUMBER} library-app:latest
                    '''
                }
            }
        }

        stage('Push to Nexus') {
            steps {
                script {
                    echo '========== Pushing artifact to Nexus =========='
                    sh '''
                        # Tag the image with Nexus registry
                        docker tag library-app:${BUILD_NUMBER} ${NEXUS_REGISTRY}/library-app:${BUILD_NUMBER}
                        docker tag library-app:latest ${NEXUS_REGISTRY}/library-app:latest
                        
                        # Push to Nexus (credentials from Jenkins secrets)
                        echo ${NEXUS_PASSWORD} | docker login -u ${NEXUS_USER} --password-stdin ${NEXUS_REGISTRY}
                        docker push ${NEXUS_REGISTRY}/library-app:${BUILD_NUMBER}
                        docker push ${NEXUS_REGISTRY}/library-app:latest
                    '''
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                script {
                    echo '========== Deploying application =========='
                    sh '''
                        docker-compose -f docker-compose.yml up -d --build
                    '''
                }
            }
        }
    }

    post {
        always {
            script {
                echo '========== Publishing test results =========='
                junit 'test-results.xml'
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'htmlcov',
                    reportFiles: 'index.html',
                    reportName: 'Code Coverage Report'
                ])
            }
        }
        success {
            echo '========== Pipeline succeeded =========='
        }
        failure {
            echo '========== Pipeline failed =========='
        }
    }
}
