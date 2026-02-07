pipeline {
  agent {
    docker {
      image 'python:3.11-slim'
      args '-u root'
    }
  }

  options {
    timestamps()
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install dependencies') {
      steps {
        sh '''
          python --version
          python -m venv .venv
          . .venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Run tests') {
      steps {
        sh '''
          . .venv/bin/activate
          pytest -q
        '''
      }
    }
  }
}
