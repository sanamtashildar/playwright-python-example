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
        UV_PYTHON_VERSION = '3.12'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Bootstrap Python') {
            steps {
                sh '''
                    set -eux

                    if ! command -v uv >/dev/null 2>&1; then
                        if command -v curl >/dev/null 2>&1; then
                            curl -LsSf https://astral.sh/uv/install.sh -o uv-install.sh
                        elif command -v wget >/dev/null 2>&1; then
                            wget -qO uv-install.sh https://astral.sh/uv/install.sh
                        else
                            echo "Neither python3 nor uv is available, and curl/wget is missing."
                            echo "Install Python 3.10+ on the Jenkins agent or add curl/wget so the pipeline can bootstrap Python."
                            exit 1
                        fi
                        sh uv-install.sh
                    fi

                    uv --version
                    uv python install ${UV_PYTHON_VERSION}
                    uv venv --clear --python ${UV_PYTHON_VERSION} .venv

                    . .venv/bin/activate
                    python --version
                    uv pip install poetry
                    poetry --version
                '''
            }
        }

        stage('Setup Python Dependencies') {
            steps {
                sh '''
                    set -eux
                    . .venv/bin/activate
                    poetry --version
                    poetry install --no-interaction --no-root
                '''
            }
        }

        stage('Verify Playwright') {
            steps {
                sh '''
                    set -eux
                    . .venv/bin/activate
                    poetry run playwright --version
                    poetry run playwright install ${BROWSER}
                '''
            }
        }

        stage('Quality Checks') {
            parallel {
                stage('Black') {
                    steps {
                        sh '''
                            set -eux
                            . .venv/bin/activate
                            poetry run black --check .
                        '''
                    }
                }
                stage('isort') {
                    steps {
                        sh '''
                            set -eux
                            . .venv/bin/activate
                            poetry run isort --check-only .
                        '''
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    set -eux
                    . .venv/bin/activate
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
