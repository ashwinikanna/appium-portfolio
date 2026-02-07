pipeline {
  agent any

  options {
    timestamps()
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup venv + Install deps') {
      steps {
        sh '''
          set -e
          python3 --version
          python3 -m venv .venv
          . .venv/bin/activate
          python -m pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Run tests') {
      steps {
        sh '''
          set -e
          . .venv/bin/activate
          pytest -q
        '''
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: '**/.pytest_cache/**', allowEmptyArchive: true
    }
  }
}
