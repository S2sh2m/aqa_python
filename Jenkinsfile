pipeline {
    agent any

    environment {
        PYTHONPATH = "${WORKSPACE}"
        DB_HOST     = "host.docker.internal"
        DB_PORT     = "5439"
        DB_NAME     = "testdb"
        DB_USER     = "testuser"
        DB_PASSWORD = "testpassword"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Клон репо"
                checkout scm
            }
        }

        stage('Start PostgreSQL') {
            steps {
                echo "PostgreSQL"
                sh '''
                    docker rm -f pg_test || true

                    docker run -d --name pg_test \
                        -e POSTGRES_USER=${DB_USER} \
                        -e POSTGRES_PASSWORD=${DB_PASSWORD} \
                        -e POSTGRES_DB=${DB_NAME} \
                        -p ${DB_PORT}:5432 \
                        postgres:15

                    echo "Очікуємо PostgreSQL..."
                    sleep 8
                '''
            }
        }

        stage('Install Python') {
            steps {
                echo "Install Python"
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-pip python3-venv
                '''
            }
        }

        stage('Install deps') {
            steps {
                echo "Install dependencies"
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r lesson_29/requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                echo "Run pytest"
                sh '''
                    export PYTHONPATH=$PWD
                    . .venv/bin/activate
                    pytest lesson_29/tests --alluredir=allure-results
                '''
            }
        }

        stage('Allure') {
            steps {
                echo "Generate Allure"
            }
            post {
                always {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        results: [[path: 'allure-results']]
                    ])
                }
            }
        }
    }

    post {
        always {
            echo "Stop PostgreSQL"
            sh 'docker rm -f pg_test || true'
        }
    }
}
#Додані зміни - комент щоб було видко бо було мільярд правок (ну його в сраку)