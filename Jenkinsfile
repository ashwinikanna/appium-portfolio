pipeline {
  agent any

  options { timestamps() }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Python check') {
      steps {
        sh '''
          set -e
          which python3
          python3 --version
        '''
      }
    }

    stage('Setup venv + install') {
      steps {
        sh '''
          set -e
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
}
