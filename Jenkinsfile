pipeline {
    agent any

    environment {
        PYTHONPATH = "${WORKSPACE}"
        DB_HOST     = "localhost"
        DB_PORT     = "5432"
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
                echo "Старт PostgreSQL (host network)"
                sh '''
                    docker rm -f pg_test || true

                    docker run -d --network=host --name pg_test \
                        -e POSTGRES_USER=${DB_USER} \
                        -e POSTGRES_PASSWORD=${DB_PASSWORD} \
                        -e POSTGRES_DB=${DB_NAME} \
                        postgres:15

                    echo "Запуск PostgreSQL"
                    sleep 5
                '''
            }
        }

        stage('Install Python') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-pip python3-venv
                '''
            }
        }

        stage('Install deps') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r lesson_29/requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    export PYTHONPATH=$PWD
                    . .venv/bin/activate
                    pytest lesson_29/tests --alluredir=allure-results
                '''
            }
        }

        stage('Allure') {
            steps {
                echo "Allure "
            }
            post {
                always {
                    allure([
                        results: [[path: 'allure-results']]
                    ])
                }
            }
        }
    }

    post {
        always {
            echo "Стоп PostgreSQL"
            sh 'docker rm -f pg_test || true'
        }
    }
}
