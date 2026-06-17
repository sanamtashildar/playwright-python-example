pipeline {
    agent any

    options {
        timestamps()
        buildDiscarder(logRotator(numToKeepStr: '20'))
        disableConcurrentBuilds()
    }

    parameters {
        choice(
            name: 'BROWSER',
            choices: ['chromium', 'firefox', 'webkit'],
            description: 'Browser used by pytest-playwright.'
        )
        booleanParam(
            name: 'HEADLESS',
            defaultValue: true,
            description: 'Run browser tests in headless mode.'
        )
    }

    environment {
        POETRY_VIRTUALENVS_IN_PROJECT = 'true'
        PIP_DISABLE_PIP_VERSION_CHECK = '1'
        PATH = "${env.HOME}/.local/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Agent Prerequisites') {
            steps {
                sh '''
                    set -eux

                    if ! command -v python3 >/dev/null 2>&1; then
                        echo "Python 3 is not installed on this Jenkins agent."
                        echo "Run this once on the Jenkins machine as root/admin:"
                        echo "  sudo apt-get update"
                        echo "  sudo apt-get install -y python3 python3-pip python3-venv"
                        exit 1
                    fi

                    python3 --version
                    python3 -m pip --version
                '''
            }
        }

        stage('Setup Python Dependencies') {
            steps {
                sh '''
                    set -eux

                    if ! command -v poetry >/dev/null 2>&1; then
                        python3 -m pip install --user poetry
                    fi

                    poetry --version
                    poetry install --no-interaction --no-root
                '''
            }
        }

        stage('Verify Playwright') {
            steps {
                sh '''
                    set -eux
                    poetry run playwright --version
                    poetry run playwright install ${BROWSER}
                '''
            }
        }

        stage('Quality Checks') {
            parallel {
                stage('Black') {
                    steps {
                        sh 'poetry run black --check .'
                    }
                }
                stage('isort') {
                    steps {
                        sh 'poetry run isort --check-only .'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    set -eux
                    mkdir -p reports allure-results

                    HEADLESS_FLAG=""
                    if [ "${HEADLESS}" = "false" ]; then
                        HEADLESS_FLAG="--headed"
                    fi

                    poetry run pytest \
                        --browser ${BROWSER} \
                        ${HEADLESS_FLAG} \
                        --junitxml=reports/junit.xml \
                        --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/junit.xml'
            archiveArtifacts allowEmptyArchive: true, artifacts: 'reports/**, allure-results/**, trace.zip'
        }
        success {
            echo 'CI pipeline completed successfully.'
        }
        failure {
            echo 'CI pipeline failed. Check the test report and archived artifacts.'
        }
    }
}
